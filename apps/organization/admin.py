from django.contrib import admin


from apps.organization.models import CourseOrg, Teacher, CityDict
# Register your models here.

@admin.register(CourseOrg)
class CourseOrgAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'desc',
        'click_nums',
        'fav_nums',
        'image',
        'address',
        'city',
        'add_time',
    )
    list_filter = (
        'name',
        'desc',
        'click_nums',
        'fav_nums',
        'image',
        'address',
        'city',
        'add_time',
    )
    search_fields = (
        'name',
        'desc',
        'click_nums',
        'fav_nums',
        'image',
        'address',
        'city',
        'add_time',
    )

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        'org',
        'name',
        'work_years',
        'work_company',
        'work_position',
        'points',
        'students',
        'fav_nums',
        'image',
        'click_nums',
        'add_time',
    )
    list_filter = (
        'org',
        'name',
        'work_years',
        'work_company',
        'work_position',
        'points',
        'students',
        'fav_nums',
        'image',
        'click_nums',
        'add_time',
    )
    search_fields = (
        'org',
        'name',
        'work_years',
        'work_company',
        'work_position',
        'points',
        'students',
        'fav_nums',
        'image',
        'click_nums',
    )
    

@admin.register(CityDict)
class CityDictAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'desc',
        'add_time',
    )
    list_filter = (
        'name',
        'desc',
        'add_time',
    )
    search_fields = (
        'name',
        'desc',
    )
    
