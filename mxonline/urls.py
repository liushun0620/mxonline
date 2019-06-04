"""mxonline URL Configuration

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
from django.urls import path, include
from django.views.generic import TemplateView
from apps.users.views import LoginView, logout_user


# 下面的两个引入是为了解决图片上传后之后不能在前端展示的问题
from mxonline.settings import MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

# import xadmin
# xadmin 安装命令
# 'pip install git+git://github.com/sshwsfc/xadmin.git@django2'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('test/', TemplateView.as_view(template_name='org_base.html'), name='test'),
    path('users/', include('users.urls', namespace='users')),
    path('org/', include('organization.urls', namespace='organization')),
    path('captcha/', include('captcha.urls')),


] + static(MEDIA_URL, document_root=MEDIA_ROOT,)  # 图片上传后之后不能在前端展示的解决方案
