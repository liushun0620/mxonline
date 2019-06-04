from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend  
from django.views.generic.base import View  # 用以编写应用的基类view, 
from django.db.models import Q  # 用以让用户使用多种账户登录比如使用邮箱 ,手机号码和用户名来登录
from django.contrib.auth.decorators import login_required  # 用退出登录使用的模块
from django.contrib.auth.hashers import make_password
from apps.users.models import UserProfile, EmailVerifyRecord
from apps.users.forms import LoginForm, RegisterForm, ForgetpwdForm, ResetpwdForm
from apps.utils.email_send import send_email


class ResetpwdView(View):
    """
    重置密码
    """

    def get(self, request, reset_code):
        records = EmailVerifyRecord.objects.filter(
            code=reset_code, send_type='forgetpwd')
        print(1)
        if records:
            print(2)
            for record in records:
                email = record.email
                print(email)
                return render(request, 'password_reset.html', {
                    'email': email,
                    'msg': '已经通过验证，请设置新密码',
                })
        else:
            print(3)
            return render(request, 'password_reset.html', {
                'msg': "链接已经失效",
            })

    def post(self, request, reset_code):
        # 这里的request.POST是必填的, 否则表单验证不通过.
        resetpwd_form = ResetpwdForm(request.POST)
        if resetpwd_form.is_valid():
            email = request.POST.get('email', '')
            password = request.POST.get('password', '')
            password2 = request.POST.get('password2', '')
            if password == password2:
                password = make_password(password)
                UserProfile.objects.filter(email=email).update(password=password)
                return render(request, 'login.html', {
                    'msg': '密码已经重置完成, 请登录',
                })
            else:
                return render(request, 'forgetpwd.html', {
                    'msg': '两次密码不一致,请重新输出',
                    'email': email,
                })
        else:
            return render(request, 'forgetpwd.html', {
                'resetpwd_form': resetpwd_form,
            })

class ForgetpwdView(View):
    """
    忘记密码
    """

    def get(self, request):
        forgetpwd_form = ForgetpwdForm()
        return render(request, 'forgetpwd.html', {
            'forget_form': forgetpwd_form
        })


    def post(self, request):
        forgetpwd_form = ForgetpwdForm(request.POST)
        if forgetpwd_form.is_valid():
            email = request.POST.get('email', '')
            if UserProfile.objects.filter(email=email):
                send_email(email, 'forgetpwd')
                print('邮箱验证正确, 正在发送邮件...')
                return render(request, 'forgetpwd.html', {
                    'msg': '重置密码的链接已经发送您的邮箱, 请注意查收',
                    'forget_form': forgetpwd_form,
                })
            else:
                return render(request, 'forgetpwd.html', {
                    'msg': '邮箱不存在',
                    'forget_form': forgetpwd_form,
                })
        else:
            return render(request, 'forgetpwd.html', {
                'forget_form': forgetpwd_form
            })



class ActiveView(View):
    """
    注册邮箱激活
    """
    def get(self, request, acitve_code):
        codes = EmailVerifyRecord.objects.filter(code=acitve_code)
        if codes is not None:
            for code in codes:
                email = code.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
            return render(request, 'login.html', {
                "msg": "验证成功, 请登录"
            })
        else:
            # TODO 配置个active.html页面
            return render(request, 'active.html', {
                "msg": "链接已经失效"
            })



class RegisterView(View):
    """
    注册
    """
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {
            'register_form': register_form,
        })

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = request.POST.get("username", '')
            email = request.POST.get('email', '')
            password = request.POST.get('password', '')
            has_eamil = UserProfile.objects.filter(email=email)
            if has_eamil:
                return render(request, 'register.html', {
                    "msg": "该邮箱已经被注册"
                })
            has_username = UserProfile.objects.filter(username=username)
            if has_username:
                return render(request, 'register.html', {
                    "msg": "该用户名已经被注册"
                })
            user = UserProfile()
            user.username = username
            user.email = email
            user.is_avtive = False
            user.password = make_password(password)
            user.save()
            send_email(email, 'register')
            return render(request, 'login.html', {
                "register_form": register_form,
                "msg": "激活账户的邮件已经发至您的邮箱,请先激活再来登录"
            })
        else:
            print(3)
            return render(request, 'register.html', {
                "register_form": register_form
            })


@login_required
def logout_user(request):
    """
    退出登录
    """
    logout(request)
    return render(request, 'login.html')


class LoginView(View):
    """
    用户登录视图
    """
    template_name = "login.html"

    def get(self, request):
        return render(request, self.template_name,)

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user_profile = UserProfile.objects.filter(email=user_name)
            # if not user_profile:
            #     return render(request, self.template_name, {
            #     "msg": '您还没有注册'
            # })
            user = authenticate(username=user_name, password=password)
            print(user)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'index.html', {
                        'login_form':login_form
                    })
                else:
                    return render(request, 'login.html', {
                        "msg":  '您还没有激活!'
                    })

            else:
                return render(request, self.template_name, {
                    "msg": '用户名或密码错误!'
                })
        else:
            return render(request, self.template_name, {
                "login_form": login_form
            })

class CustomBackend(ModelBackend):
    """
    这个方法相当于重写了authenticate方法,增加以下两项功能 
    以验证用户登录
    使用多种账户登录
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Q用来使用多种账户登录
            user = UserProfile.objects.get(Q(username=username) | Q(email=username) | Q(mobile=username))
            # check_password 用来验证密码,若通过验证则返回true
            if user.check_password(password):
                return user
        except Exception as e:
            print(e)
            return None
