from django.urls import path
from form_to_csv import views
urlpatterns = [
    path('', views.home_view, name='home_view'),
]