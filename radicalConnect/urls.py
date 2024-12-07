"""
URL configuration for radicalSolutions project.

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
from django.contrib import admin
from django.urls import path

from radicalConnect import views
from radicalConnect.views import login_view

urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('index/', views.index, name='index'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('blog/',views.blog, name='blog'),
    path('base/',views.base, name='base'),
    path('signup/',views.signup, name='signup'),
    path('about0/',views.about0, name='about0'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('usersapi/',views.usersapi, name='usersapi'),
    path('mpesa/',views.mpesa, name='mpesa'),
    path('login_view',views.login_view,name='login_view'),
    path('course/',views.course, name='course'),
]
