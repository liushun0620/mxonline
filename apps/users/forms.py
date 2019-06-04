from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    """
    登录表单验证
    """
    username = forms.CharField(required=True)
    password = forms.CharField(min_length=5, required=True)


class RegisterForm(forms.Form):
    """
    注册表单验证
    """
    email = forms.EmailField(required=True)
    password = forms.CharField(min_length=5, required=True)
    captcha = CaptchaField(error_messages={
        "invalid": "验证码错误"
    })


class ForgetpwdForm(forms.Form):
    """
    忘记密码表单验证
    """
    email = forms.EmailField(required=True)
    # email = forms.CharField(required=True)
    captcha = CaptchaField(error_messages={
        "invalid": "验证码错误"
    })


class ResetpwdForm(forms.Form):
    """
    修改密码表单验证
    """
    password = forms.CharField(min_length=5, required=True)
    password2 = forms.CharField(min_length=5, required=True)

