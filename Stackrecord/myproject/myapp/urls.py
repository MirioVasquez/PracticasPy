from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_record, name='add_record'),
    path('add/success', views.success, name='success'),
    path('load_json/', views.load_json_and_save, name='load_json'),
]