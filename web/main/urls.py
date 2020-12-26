from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('',  views.index, name="index"),
    path('add-data',  views.add_data, name="add_data"),
    path('collected-data',  views.collected_data, name="collected_data"),
    path('export-data',  views.export_data, name="export_data"),
]
