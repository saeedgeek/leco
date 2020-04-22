from django.urls import path

from .views import Register
from .views import StudentExtra, BirthCertificateImage

urlpatterns = [
    path("register", Register.as_view()),
    path("extra", StudentExtra.as_view()),
    path("birth_certificate", BirthCertificateImage.as_view())
]
