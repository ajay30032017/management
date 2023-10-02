"""scrap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from scrapapp.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',index,name='index'),
    path('price/',price,name='price'),
    path('list/',list,name='list'),
    path('update_list/',processOrder),
    path('pickup/',pickup,name="pickup"),
    path('process_request/',processRequest,name="processrequest"),
    path('login/',loginView,name='login'),
   
    path('signup/',SignUpView.as_view(),name='signup'),
    path('accounts/', include('django.contrib.auth.urls'),name='accounts'),
    path('user_select/',userType),
    path("buyer/",buyer,name="buyer"),
    path("search_area/",searchArea,name="searcharea"),
    
]
