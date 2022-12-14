from django.urls import path
from .views import blog_list, blog_detail

urlpatterns = [
    path('', blog_list, name='blog-list'),
    path('blog/<int:pk>/', blog_detail, name='blog-detail'),
]