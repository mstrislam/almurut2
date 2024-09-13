"""
URL configuration for almurut_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views

"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from market.views import ProductListView, HomeView, LoginView
from users.views import UserRegistrationView, UserMakeRegistrationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', ProductListView.as_view()),
    path('home/', HomeView.as_view()),
    path('registration/', UserRegistrationView.as_view(), name='registration-url'),
    path('login/', LoginView.as_view()),
    path('make-registration/', UserMakeRegistrationView.as_view(), name='make-registration-url')

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
