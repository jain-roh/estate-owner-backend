"""EstateByTheOwner URL Configuration

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
from django.conf.urls import include
from django.conf.urls import url
from .views import UserLogin,CreateUser,SellerDetails,UserUpdate
urlpatterns = [
    url(r'login', UserLogin.as_view()),
    url(r'create',CreateUser.as_view()),
    url(r'details',SellerDetails.as_view()),
    url(r'updatePassword',UserUpdate.as_view())
]
