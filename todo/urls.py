from django import views
from django.urls import path,include
from . import views

urlpatterns = [
  path('',views.index,name='home'),
  path('delete/<str:pk>',views.delete,name='del')
]
