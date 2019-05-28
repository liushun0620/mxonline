from django.contrib import admin
from django.urls import path


from .apps import UsersConfig

# 必须配置的
app_name = UsersConfig.name

urlpatterns = [
    # path('', ),
]
