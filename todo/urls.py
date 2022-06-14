from django import views
from django.urls import path,include
from . import views

urlpatterns = [
  path('',views.index,name='home'),
  path('delete/<str:pk>',views.delete,name='del'),
  path('edit/<str:pk>',views.edit,name='edit'),
  path('login',views.loginPage,name='login'),
  path('register',views.register,name='register'),
  path('logout',views.logoutUser,name='logout'),



]
