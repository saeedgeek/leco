from django.urls import path
from  .views import GetCityList,ProfileImage,UserProfile
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('get_list_of_cities', GetCityList.as_view()),
    path('login', TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view()),
    path('profile_image', ProfileImage.as_view()),
    path('profile', UserProfile.as_view()),

]
