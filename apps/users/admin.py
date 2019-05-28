from django.contrib import admin

# Register your models here.
from apps.users.models import UserProfile, EmailVerifyRecord, Banner


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'nick_name',
        'birthday',
        'email',
        'gender',
        'address',
        'mobile',
        'image',
    )
    list_filter = (
        'gender',
        'birthday',
    )
    search_fields = (
        'username',
        'nick_name',
        'birthday',
        'email',
        'gender',
        'address',
        'mobile',
    )
    
@admin.register(EmailVerifyRecord)
class EmailVerifyRecordAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'email',
        'send_type',
        'sent_time',
    )
    list_filter = (
        'send_type',
        'sent_time',
    )
    search_fields = (
        'code',
        'email',
    )

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'image',
        'url',
        'index',
        'create_time',
    )
    search_fields = (
        'title',
        'image',
        'url',
        'index',
    )
