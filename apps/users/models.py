from django.db import models

from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, default='昵称', verbose_name='用户昵称')
    birthday = models.DateField("生日", null=True, blank=True, auto_now=False, auto_now_add=False)
    gender = models.CharField('性别', choices=(('male', '男'),('female', '女')), default='female', max_length = 6)
    address = models.CharField('地址',default='',  max_length=50)
    mobile = models.CharField('手机号码', max_length=11, null=True, blank=True)
    image = models.ImageField('头像', upload_to='image/users/', default='image/default.png',  height_field=None, width_field=None, max_length=None)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.nick_name

class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name='验证码')
    email = models.EmailField('邮箱', max_length=54)
    send_type = models.CharField("发送类型", choices=(('register', '注册'), ('forget', '忘记密码')), max_length=50)
    # auto_now = 是指用户实例化的时间, 比如频繁操作的最后一次时间,,可以用来表示 updatetime
    # auto_now_add 是指用户首次添加的时间, 一般用来表示create_time
    sent_time = models.DateTimeField("发送时间", auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = '邮箱验证'
        verbose_name_plural = verbose_name


class Banner(models.Model):
    title = models.CharField('标题', max_length=50)
    image = models.ImageField('轮播图', upload_to="banner/", height_field=None, width_field=None, max_length=None)
    url = models.URLField('访问地址', max_length=200)
    index = models.IntegerField(default=100, verbose_name='顺序')
    create_time = models.DateTimeField("添加时间", auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name
        
