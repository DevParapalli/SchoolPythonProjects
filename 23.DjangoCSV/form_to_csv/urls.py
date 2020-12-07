from django.urls import path
from form_to_csv import views
urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('download_csv/', views.download_csv, name='download_csv'),
    path('add_data/', views.add_data, name='add_data'),
    path('wipe_database', views.wipe_database, name='wipe_database')
    
]