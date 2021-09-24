from django.urls import path
from .views import studentDetail, crud_methods

urlpatterns = [
    path('crud', crud_methods , name="crud_methods"),
    path('crud/<int:pk>', studentDetail , name="studentDetail"),

]