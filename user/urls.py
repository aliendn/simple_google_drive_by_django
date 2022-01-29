from .views import get_name
from django.urls import path

urlpatterns = [
    path('form/', get_name, name='form')
]
