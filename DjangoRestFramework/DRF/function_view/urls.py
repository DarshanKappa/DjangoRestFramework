from django.urls import path
from .views import stu_api

urlpatterns = [
    path('crud', stu_api, name="stu_api")
]
