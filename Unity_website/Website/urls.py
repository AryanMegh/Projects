"""
URL configuration for Website project.

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
from W3Schoolspoint_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Signup, name='Signup'),
    path('Login/', views.Login, name='Login'),
    path('Login/Signup', views.Signup, name='Signup'),
    path('Login/Forgot_password', views.Forgot_password, name='Forgot_password'),
    path('Login/Dashboard', views.Dashboard, name='Dashboard'),
    path('Login/Index', views.Index, name='Index'),
    path('Login/Appointment_schedulling', views.Appointment_schedulling, name='Appointment_schedulling'),
    path('Login/Logout', views.Logout, name='Logout')
]