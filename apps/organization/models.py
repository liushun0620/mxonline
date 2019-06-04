from django.db import models


class CourseOrg(models.Model):
    name = models.CharField("课程机构名称", default='', max_length=50)
    desc = models.TextField("课程机构描述", default='')
    click_nums = models.IntegerField("点击数", default=0)
    fav_nums = models.IntegerField("收藏人数", default=0,)
    students = models.IntegerField("学习人数", default=0,)
    course_nums = models.IntegerField("课程数", default=0,)
    image = models.ImageField("封面图", upload_to="org/", default='org/default.png',
                              height_field=None, width_field=None, max_length=100)
    address = models.CharField("机构地址", default='', max_length=150)
    city = models.ForeignKey("organization.CityDict", verbose_name="所在城市", on_delete=models.CASCADE)
    org_type = models.CharField("机构类别", choices=(
        ('1', '培训机构'), ('2', '高校'), ('3', '个人')), default='1',  max_length=20)
    add_time = models.DateTimeField("添加时间", auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = '机构'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Teacher(models.Model):
    org = models.ForeignKey("organization.CourseOrg", verbose_name="所属机构", on_delete=models.CASCADE)
    name = models.CharField("名称", default='', max_length=50)
    work_years = models.IntegerField("工作年限", default=0,)
    work_company = models.CharField("就职公司", default='',max_length=50)
    work_position = models.CharField("公司职位", default='', max_length=50)
    points = models.CharField("教学特点", default='', max_length=50)
    # course = models.ForeignKey(
    #     "course.Course", verbose_name="所授课程", on_delete=models.CASCADE)
    students = models.IntegerField("学习人数", default=0,)
    fav_nums = models.IntegerField("收藏人数", default=0,)
    image = models.ImageField("教师头像", upload_to="course/", default='course/default.png',
                              height_field=None, width_field=None, max_length=100)
    click_nums = models.IntegerField("点击数", default=0)
    add_time = models.DateTimeField("添加时间", auto_now=False, auto_now_add=True)

    
    class Meta:
        verbose_name = '教师管理'
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.name


class CityDict(models.Model):
    name = models.CharField("城市名", default='', max_length=50)
    desc = models.CharField("城市描述", default='', max_length=200)
    add_time = models.DateTimeField("添加时间", auto_now=False, auto_now_add=True)


    class Meta:
        verbose_name = '城市'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
