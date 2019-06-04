from django.contrib import admin
from django.urls import path


from .apps import UsersConfig
from apps.users.views import LoginView, logout_user, RegisterView, ActiveView, ForgetpwdView, ResetpwdView

# 必须配置的
app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('forgetpwd/', ForgetpwdView.as_view(), name='forgetpwd'),
    path('resetpwd/<str:reset_code>/', ResetpwdView.as_view(), name='resetpwd'),
    path('active/<str:acitve_code>/', ActiveView.as_view(), name='active'),  # 这种URL方式参考自官方文档
]
