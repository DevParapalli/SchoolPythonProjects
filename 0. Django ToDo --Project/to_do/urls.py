from django.urls import path, re_path
from .views import to_do, remove



urlpatterns = [
    path('', to_do, name='to_do'),
    path('delete/<identifier>', remove, name='delete'), 
    
]