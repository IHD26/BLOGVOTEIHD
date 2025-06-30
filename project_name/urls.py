"""
URL configuration for project_name project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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


# Importing the required modules

# The admin module is used to create the admin site for the application
# using the default django admin site module
from django.contrib import admin

# The path module is used to create the url patterns for the application
# to map the urls to the views
from django.urls import path

# The views module is used to import the views from the views.py file
from app_name import views

# The settings module is used to import the settings from the settings.py file
# to get the media, static files and other settings
from django.conf import settings

# The static module is used to import the static files from the settings.py file
from django.conf.urls.static import static


# The urlpatterns list is used to store the url patterns for the application
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.homeView, name='home'),
    path('register/', views.registrationView, name='registration'),
    path('login/', views.loginView, name='login'),
    path('dashboard/', views.dashboardView, name='dashboard'),
    path('logout/', views.logoutView, name='logout'),
    path('position/', views.positionView, name='position'),
    path('candidate/<int:pos>/', views.candidateView, name='candidate'),
    path('candidate/detail/<int:id>/', views.candidateDetailView, name='detail'),
    path('result/', views.resultView, name='result'),
    path('changepass/', views.changePasswordView, name='changepass'),
    path('editprofile/', views.editProfileView, name='editprofile'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)