from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
   path('', views.index, name='index'),
   path('books/', views.getSlotInput, name='books1'),
   path('end/', views.logoutr, name='books'),
   

]
