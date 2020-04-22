from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import GetCityList, ProfileImage, UserProfile, ResetPassword, ChangePassword, GetInfo

urlpatterns = [
    path('get_list_of_cities', GetCityList.as_view()),
    path('get_info', GetInfo.as_view()),
    path('login', TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view()),
    path('profile_image', ProfileImage.as_view()),
    path('profile', UserProfile.as_view()),
    path('reset_pass', ResetPassword.as_view()),
    path('change_password', ChangePassword.as_view()),

]
