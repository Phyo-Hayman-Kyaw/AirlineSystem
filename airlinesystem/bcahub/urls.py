from django.contrib import admin
from django.urls import path, include


from bcahub.views import airline_views

urlpatterns = [
   
 
    path('pages/createtravel', airline_views.createtravel, name='createtravel'),
    path('portalpages/updateViewtravel/<int:pk>/',airline_views.updateViewtravel, name='updateViewtravel'),
    path('pages/updatetravel', airline_views.updatetravel, name='updatetravel'),
    path('pages/base', airline_views.base, name='base'),
    path('pages/store', airline_views.store, name='storename'),
   

    ]
