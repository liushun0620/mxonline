from django.contrib import admin
from django.urls import path


from .apps import OrganizationConfig
from apps.organization.views import OrgListView, AddAskView, OrgHomeView

# 必须配置的
app_name = OrganizationConfig.name

urlpatterns = [
    path('', OrgListView.as_view(), name='org_list'),
    path('addask/', AddAskView.as_view(), name='addask'),
    path('home/<int:org_id>', OrgHomeView.as_view(), name='org_home'),
]
