"""market URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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

from user.views import user_login, reg_login, forget_password, infor, member_user, user_code, address, address_show

urlpatterns = [
    url(r'^login/$', user_login, name="登录"),
    url(r'^reg/$', reg_login, name="注册"),
    url(r'^fpaswd/$', forget_password, name="忘记"),
    url(r'^infor/$', infor, name="修改中心"),
    url(r'^member/$', member_user, name="个人中心"),
    url(r'^code/$', user_code, name="验证码"),
    url(r'^address/$', address_show, name="收货地址"),
    url(r'^addr/$', address, name="添加收货地址"),

]
