from django.contrib import admin

# Register your models here.
from apps.course.models import Courses, CourseResource, Video, Lesson

@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'desc',
        'detail',
        'degree',
        'learns_times',
        'students',
        'fav_nums',
        'image',
        'click_nums',
        'add_time',
    )
    list_filter = (
        'name',
        'desc',
        'detail',
        'degree',
        'learns_times',
        'students',
        'fav_nums',
        'image',
        'click_nums',
        'add_time',
    )
    search_fields = (
        'name',
        'desc',
        'detail',
        'degree',
        'learns_times',
        'students',
        'fav_nums',
        'image',
        'click_nums',
    )


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = (
        'course',
        'name',
        'add_time',
    )
    list_filter = (
        'course',
        'name',
        'add_time',
    )
    search_fields = (
        'course',
        'name',
    )


@admin.register(CourseResource)
class CourseResourceAdmin(admin.ModelAdmin):
    list_display = (
        'course',
        'name',
        'download',
        'add_time',
    )
    list_filter = (
        'course',
        'name',
        'download',
        'add_time',
    )
    search_fields = (
        'course',
        'name',
        'download',
    )


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = (
        'lesson',
        'name',
        'add_time',
    )
    list_filter = (
        'lesson',
        'name',
        'add_time',
    )
    search_fields = (
        'lesson',
        'name',
    )
