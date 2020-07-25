"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path                                                    
from . import views                                                             

                                                                                

urlpatterns = [                                                                 

    path('', views.test, name='qa_list'),                                       

    path('login/', views.test, name='login'),                                   

    path('signup/', views.test, name='signup'),                                 

    path('question/<int:pk>/', views.test, name='question'),                    

    path('ask/', views.test, name='popular'),                                   

    path('new/', views.test, name='new'),                                       

]        


  #  url(r'

#/login/

#/signup/

#/question/<123>/    # вместо <123> - произвольный ID

#/ask/

#/popular/

#/new/




]
