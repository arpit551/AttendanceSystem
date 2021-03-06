"""attendance_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from rest_framework import routers
from Location import views as location_views
from Attendance import views as attendance_views
from MLendpoints import views as MLviews
from django.conf.urls import include
from django.contrib.auth import views as auth_views


urlpatterns = [
    # api view
    path('api/v1/train-video/', MLviews.TrainVideo.as_view()),
    path('api/v1/test-video/', MLviews.TestVideo.as_view()),
    path('api/v1/get-auth/', attendance_views.CustomAuthToken.as_view(), name='api_token_auth'),
    path('api/v1/create-auth/', attendance_views.register.as_view()),

    # django website views
    path("", include('Attendance.urls')),
    path('', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('admin/', admin.site.urls),

]