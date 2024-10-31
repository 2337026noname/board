"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from tkinter.font import names

from django.urls import path
from . import views


app_name = 'board'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:member_id>/', views.detail, name='detail'),
    path('input/', views.input, name='input'),
    path('create/', views.create, name='create'),
    path('delete/<int:member_id>/', views.delete, name='delete'),
    path('editform/<int:member_id>/', views.editform, name='editform'),
    path('edit/', views.edit, name='edit'),
    path('member_create/', views.member_create, name="member_create"),
]