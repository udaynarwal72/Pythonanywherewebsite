"""
URL configuration for Studease_main project.

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
from django.urls import path,include
from studease import views

urlpatterns = [
    path('',views.homepage,name="homepage"),
    path('login',views.loginUser, name="login"), 
    path('logout',views.logoutUser, name="logout"),
    path('signup',views.signUpUser, name="signUp"), # type: ignore
    path('test', views.test, name="test"),
    path('usertimetable',views.usertimetable,name="usertimetable"),
    path('base',views.base,name='base'),
    path('index',views.index,name='index'),
    path('webtest',views.testweb,name='webtest'),
    path('usertimetableindex',views.usertimetableindex,name='usertimetableindex'),
    path('buddyship',views.buddyship,name='buddyship'),
    path('serviceworker', views.serviceworker,name='serviceworker'),
    path('vacantvenue',views.vacantvenues,name='vacantvenue'),
    path('resultvacantvenue',views.resultvacantvenue,name='resultvacantvenue'),
    path('resultbuddyship',views.resultbuddyship,name='resultbuddyship'),
    path('roomrover',views.roomrover,name='roomrover'),
    path('explainedvenue',views.explainedvenue,name='explainedvenue'),
    path('userattendance',views.userattendance,name='userattendance'),
    path("storetoken", views.storePushToken, name="storePushToken"),
    path("getclassdetailbysectioname", views.getSectionWiseToken, name="getclassdetailbysectioname"),
    path("usercalculatedattendance", views.userCalculatedAttendance, name="calculatedattendance"),
    #'<int:id>' this is a path convertor that allows to create dynamic urls
]
