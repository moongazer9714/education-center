from django.urls import path
from .views import about_us, index
urlpatterns = [
    path('about/', about_us, name='about'),
    path('', index, name='index'),
]