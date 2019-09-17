"""TheOnePiece URL Configuration

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
from django.contrib import admin
from  blog.views import RegisterViews,LoginViews
from  blog.views.LoginoutViews import login_out
from django.conf.urls import include

from blog.views.valid_code import get_valid_img
# 导入media
from django.views.static import serve
from django.conf import settings
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/$',RegisterViews.register.as_view(),name='register'),
    url(r'^login/$',LoginViews.login.as_view(),name='login'),
    url(r'^blog/',include('blog.urls')),
    url(r'^login_out/$',login_out.as_view(),name='login_out'),

    # 验证码
    url(r'^valid_code/',get_valid_img),
    # 直接访问图片
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
