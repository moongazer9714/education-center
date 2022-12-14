from django.urls import path
from .views import contact_obj

urlpatterns = [
    path('', contact_obj, name='contact')
]