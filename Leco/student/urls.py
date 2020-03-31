from django.urls import path
from .views import StudentExtra
from .views import Register

urlpatterns = [
path("register",Register.as_view()),
path("extra", StudentExtra.as_view())
]
