"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from ecommerce_accounts import views
from django.shortcuts import redirect

urlpatterns = [
    path('createaccount', views.createaccount, name='create account'),
    path('create', views.create, name='create'),
    path('login', views.login, name = 'Login'),
    path('loginpage', views.loginpage, name = 'Login page'),
    path('logout', views.logout, name = 'Logout'),
    path('forgotpassword', views.forgot_password, name = 'Forgot password'),
    path('send-otp',views.send_otp, name = 'Send OTP'),
    path('index', lambda request: redirect('/')),
    path('shop', lambda request: redirect('/shop')),
    path('cart', lambda request: redirect('/cart')),
    path('checkout', lambda request: redirect('/checkout')),
    path('product-details', lambda request: redirect('/product-details')),
]
