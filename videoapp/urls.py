"""
URL configuration for mypswebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views 

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('portfolio/', views.portfolio, name = 'portfolio'),
    path('services/', views.services, name = 'services'),
    path('contact/', views.contact, name = 'contact'),
    path('blog_details/', views.blog_details, name = 'blog_details'),
    path('blog/', views.blog, name = 'blog'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('register/', views.register, name = 'register'),
    path('products/', views.products, name = 'products'),
    path('forget_password/', views.forget_password, name = 'forget_password'),
    path('confirm/', views.confirm, name = 'confirm'),
    
    
  
    # path('main/', views.main, name = 'main'),
    
    
        
    
    
]
