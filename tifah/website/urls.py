"""
URL configuration for website project.

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
from website1.views import home_view, aboutus_view, gallery_view, services_view, contactus_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view,name='home_page'),
    path('aboutus/',aboutus_view,name='aboutus_page'),
    path('gallery/',gallery_view,name='gallery_page'),
    path('services/',services_view,name='services_page'),
    path('contactus/',contactus_view,name='contactus_page'),
]

