from django.urls import path
from .views import GetFieldList,GetLevelList
urlpatterns = [
    path('get_list_of_fields/', GetFieldList.as_view()),
    path('get_list_of_levels/', GetLevelList.as_view()),
]
