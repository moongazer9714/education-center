from django.urls import path
from .views import courses, course

urlpatterns = [
    path('', courses, name='course'),
    path('course/<int:pk>/', course, name='course-detail'),
]
