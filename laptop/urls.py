from django.urls import path
from .views import laptops

urlpatterns = [
    path('', laptops, name='laptops')
]