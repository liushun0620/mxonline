from django.contrib import admin


from apps.operation.models import UserAsk,UserCourse,UserFavorite,UserMessage,CourseComments
# Register your models here.
@admin.register(UserAsk)
class UserAskAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'mobile',
        'course_name',
        'add_time',
    )
    list_filter = (
        'name',
        'mobile',
        'course_name',
        'add_time',
    )
    search_fields = (
        'name',
        'mobile',
        'course_name',
    )


@admin.register(UserCourse)
class UserCourseAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'course',
        'add_time',
    )
    list_filter = (
        'user',
        'course',
        'add_time',
    )
    search_fields = (
        'user',
        'course',
    )


@admin.register(UserFavorite)
class UserFavoriteAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'fav_id',
        'fav_type',
        'add_time',
    )
    list_filter = (
        'user',
        'fav_id',
        'fav_type',
        'add_time',
    )
    search_fields = (
        'user',
        'fav_id',
        'fav_type',
    )

@admin.register(UserMessage)
class UserMessageAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'message',
        'is_readed',
        'add_time',
    )
    list_filter = (
        'user',
        'message',
        'is_readed',
        'add_time',
    )
    search_fields = (
        'user',
        'message',
        'is_readed',
    )
@admin.register(CourseComments)
class CourseCommentsAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'course',  
        'comments',
        'add_time',
    )
    list_filter = (
        'user',
        'course',  
        'comments',
        'add_time',
    )
    search_fields = (
        'user',
        'course',  
        'comments',
    )
