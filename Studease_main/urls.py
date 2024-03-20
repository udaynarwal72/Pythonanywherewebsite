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
from django.conf import settings
from django.http import HttpResponse
import os
def staticView(request):
    response = HttpResponse(content_type='text/javascript')
    print(os.path.join(settings.BASE_DIR,"/firebase-messaging-sw.js"))
    with open('/Users/udaynarwal/Desktop/studease_main/Studease_main/firebase-messaging-sw.js') as fp:
        response.write(fp.read())
    return response
    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('firebase-messaging-sw.js',staticView),
    path('',include('studease.urls')),
]
