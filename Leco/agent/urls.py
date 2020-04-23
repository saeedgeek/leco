from django.urls import path
from .views import CreateAgent
urlpatterns = [
    path("create_agent", CreateAgent.as_view())
]
