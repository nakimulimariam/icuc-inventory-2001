"""
URL configuration for blogger project.

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
from django.urls import path, include

from blog.views import index_view, blog_list_view, add_author_view, edit_author_view, delete_author_view, sign_up_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , index_view, name='index_page'),
    path('sign_up/' , sign_up_view, name='sign_up_page'),
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('blog_list/' , blog_list_view, name='blog_list_page'),
    path('add_author/', add_author_view, name="add_author_page"),
    path('edit_author/<int:author_id>/', edit_author_view, name="edit_author_page"),
    path('delete/<int:author_id>/', delete_author_view, name="delete_author_page"),
    
]