from django.urls import path

from .views import (
  UserCreateView,
  CustomObtaionAuthTokenView,
  )

urlpatterns = [
  path('register/', UserCreateView.as_view(), name='register'),
  path('token/', CustomObtaionAuthTokenView.as_view(), name='token'), 
]