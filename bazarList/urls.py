"""todos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from bazar import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home, name='home'),

    path('signup', views.signupuser, name='signupuser'),
    path('logout', views.logoutuser, name='logoutuser'),
    path('login', views.loginuser, name='loginuser'),
    path('', views.loginuser, name='loginuser'),
    path('currentList', views.currentList, name='currentList'),
    path('list', views.list, name='list'),
    path('bazarlist/<int:bazar_pk>', views.viewBazar, name='bazarlist'),
     path('bazarlist/<int:bazar_pk>/compllete', views.completeBazar, name='complete'),


]
