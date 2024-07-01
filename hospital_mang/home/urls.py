from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.show_index,name='home'),
    path('about',views.show_about,name='about'),
    path('doctors',views.show_doctors,name='doctors'),
    path('booking',views.show_booking,name='booking'),
    path('contact',views.show_contact,name='contact'),
    path('department',views.show_department,name='department'),
]
