from django.urls import path
from .views import StudentAPI

urlpatterns = [
     path('crud', StudentAPI.as_view()),
     path('crud/<int:pk>', StudentAPI.as_view()),
]
