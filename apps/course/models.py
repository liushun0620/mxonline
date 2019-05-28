from django.db import models


class Courses(models.Model):
    name = models.CharField("课程名称", max_length=50, default='')
    desc = models.CharField("课程描述", max_length=500, default='')
    detail = models.TextField("课程详情", default='')
    degree = models.CharField("课程级别", choices=(('1', '初级'), ('2', '中级'), ("3", "高级")), default="1", max_length=50)
    learns_times = models.IntegerField("学习时长(分钟数)", default=0,)
    students = models.IntegerField("学习人数", default=0,)
    fav_nums = models.IntegerField("收藏人数", default=0,)
    image = models.ImageField("封面图", upload_to="course/", default='course/default.png', height_field=None, width_field=None, max_length=100)
    click_nums = models.IntegerField("点击数", default=0)
    add_time = models.DateTimeField("添加时间", auto_now=False, auto_now_add=True)


    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name


class Lesson(models.Model):
    """
    章节
    """
    # 在这里注意foreignKey的连接方式是: app.Model. 要指定某个应用下model
    course = models.ForeignKey(
        "course.Courses", verbose_name="课程名称", on_delete=models.CASCADE)
    name = models.CharField('章节名称', max_length=50)
    add_time = models.DateTimeField("添加时间", auto_now=False, auto_now_add=True)


    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name




class Video(models.Model):
    lesson = models.ForeignKey(
        "course.Lesson", verbose_name="章节", on_delete=models.CASCADE)
    name = models.CharField("视频名称", max_length=100)
    add_time = models.DateTimeField("添加时间", auto_now=False, auto_now_add=True)


    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name


class CourseResource(models.Model):
    course = models.ForeignKey("course.Courses", verbose_name="课程", on_delete=models.CASCADE)
    name = models.CharField("名称", max_length=50)
    download = models.FileField("课程资源", upload_to='course/resource/', max_length=100)
    add_time = models.DateTimeField("添加时间", auto_now=False, auto_now_add=True)
    

    class Meta:
        verbose_name = '课程资源'
        verbose_name_plural = verbose_name
