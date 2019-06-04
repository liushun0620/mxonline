import re

from django import forms
from apps.operation.models import UserAsk


class UserAskForm(forms.ModelForm):
    class Meta:
        """
        注意这里的变量名, 必须是这样配置的, 一个字母都不能错, 这里区分大小写的
        """
        model = UserAsk
        fields = [
            'name',
            'mobile',
            'course_name',
        ]

    # 自定义表单验证
    def clean_mobile(self):
        """
        验证手机号码是否合法
        """
        mobile = self.cleaned_data['mobile']
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^17[76]\d{8}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError('手机号码非法', code='mobile_invalid')
