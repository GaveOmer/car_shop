from rest_framework.generics import CreateAPIView
from django.conf import settings
from .serializers import UserSerializer, AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

class UserCreateView(CreateAPIView):
  serializer_class = UserSerializer
  
  
  
class CustomObtaionAuthTokenView(ObtainAuthToken):
  serializer_class = AuthTokenSerializer
  
  def post(self, request, *args, **kwargs):
    response = super().post(request, *args, **kwargs)
    if response.status_code == 200:
      token = response.data.get('token')
      response.set_cookie(
        settings.AUTH_COOKIE,
        token,
        max_age=settings.AUTH_COOKIE_MAX_AGE,
        path=settings.AUTH_COOKIE_PATH,
        secure=settings.AUTH_COOKIE_SECURE,
        httponly=settings.AUTH_COOKIE_HTTPONLY,
        samesite=settings.AUTH_COOKIE_SAMESITE,
      )
      
    return response