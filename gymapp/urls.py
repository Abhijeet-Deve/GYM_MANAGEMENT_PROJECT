"""
URL configuration for ajpower project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from gymapp import views


urlpatterns = [
   
    path('', views.Home),
    path('signup',views.signup,name="signup"),
    path('login',views.handlelogin,name="handlelogin"),
    path('logout/', views.handleLogout, name="handleLogout"),

    path('contact',views.contact,name="contact"),
    path('join',views.enroll,name="enroll"),
    path('profile/',views.profile,name="profile"),
    path('gallery',views.gallery,name="gallery"),
    path('attendance',views.attendance,name="attendance"),
    path('about',views.about,name="about"),
    path('Biceps_Triceps',views.Biceps_Triceps,name="Biceps_Triceps"),
    path('Back_workout',views.Back_workout,name="Back_workout"),
    path('shoulder_workout',views.shoulder_workout,name="shoulder_workout"),
    path('Chest_workout',views.Chest_workout,name="Chest_workout"),
    path('Leg_workout',views.Leg_workout,name="Leg_workout"),
    path("services",views.services,name="sevices")


]
