from django.urls import path
from .views import CreateCenter
urlpatterns = [

    path("create_center", CreateCenter.as_view())

]
