from django.db import models


from apps.users.models import UserProfile
from apps.course.models import Courses
from apps.organization.models import Teacher,CourseOrg




class UserAsk(models.Model):
    name = models.CharField("姓名", max_length=20)
    mobile = models.CharField("手机号码", max_length=11)
    course_name = models.CharField("课程名", max_length=50)
    add_time = models.DateTimeField("添加时间", auto_now=False, auto_now_add=True)
   

    class Meta:
        verbose_name = '用户咨询'
        verbose_name_plural = verbose_name

class CourseComments(models.Model):
    """
    用户对课程的评论
    """
    user = models.ForeignKey("users.UserProfile", verbose_name="用户", on_delete=models.CASCADE)
    course = models.ForeignKey("course.Courses", verbose_name="课程", on_delete=models.CASCADE)
    comments = models.CharField("评论", max_length=300)
    add_time = models.DateTimeField("添加时间", auto_now=False, auto_now_add=True)


    class Meta:
        verbose_name = '课程评论'
        verbose_name_plural = verbose_name

class UserFavorite(models.Model):
    """
    用户收藏
    """
    user = models.ForeignKey("users.UserProfile", verbose_name="用户", on_delete=models.CASCADE)
    fav_id = models.IntegerField("数据ID", default=0)
    fav_type = models.CharField('收藏类型', choices=((1, '课程'), (2, '课程机构'), (3, '讲师')),default=1, max_length=5)
    add_time = models.DateTimeField("添加时间", auto_now=False, auto_now_add=True)
    
    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    """
    用户消息
    第四章:01:30
    """
    user = models.IntegerField('用户ID', default=0,)
    message = models.CharField('消息', default='', max_length=500)
    is_readed = models.BooleanField("是否已读", default=False,)
    add_time = models.DateTimeField("添加时间", auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = '用户消息'
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    """ 
    用户课程
    """
    user = models.ForeignKey("users.UserProfile", verbose_name="用户", on_delete=models.CASCADE)
    course = models.ForeignKey("course.Courses", verbose_name="课程", on_delete=models.CASCADE)
    add_time = models.DateTimeField("添加时间", auto_now=False, auto_now_add=True)
    
    class Meta:
        verbose_name = '用户课程'
        verbose_name_plural = verbose_name
