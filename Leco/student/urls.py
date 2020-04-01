from django.urls import path
from .views import StudentExtra, BirthCertificateImage
from .views import Register

urlpatterns = [
path("register",Register.as_view()),
path("extra", StudentExtra.as_view()),
path("birth_certificate", BirthCertificateImage.as_view())
]
