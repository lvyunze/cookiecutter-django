"""
URL configuration for <<cookiecutter.project_name|upper >> project.

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
from django.urls import path, include, re_path
from django.shortcuts import redirect
from two_factor.urls import urlpatterns as tf_urls
from two_factor.admin import AdminSiteOTPRequired

# 不要立即替换默认的admin站点为OTP保护的站点
# 先确保登录正常后再启用这个功能
admin.site.__class__ = AdminSiteOTPRequired

def redirect_to_login(request):
    return redirect('two_factor:login')

urlpatterns = [
    # 根路径重定向到登录页面
    path('', redirect_to_login),
    path('admin/', admin.site.urls),
    # 两因素认证URL
    path('', include(tf_urls)),
    # 兼容 Django 默认的后台登录跳转路径
    re_path(r'^accounts/login/$', redirect_to_login),
]