from apps.users.models import EmailVerifyRecord
import random
from django.core.mail import send_mail  # django 本身自带的发邮件模块,  未使用
from mxonline.settings import EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_FROM
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import formataddr
import smtplib
import traceback


def sendmail(title, content, to_emails, from_email=EMAIL_FROM, cc_emails=None, attachs=None):
    """
    定义了一个发送邮件的方法,
    """
    if cc_emails is None:
        cc_emails = []
    if attachs is None:
        attachs = []

    tos = ','.join(to_emails)
    ccs = ','.join(cc_emails)
    if not cc_emails:
        to_emails.extend(cc_emails)

    # 创建一个带附件的实例
    message = MIMEMultipart()
    from_name = from_email.split('@')[0].upper()  # .capitalize()
    message['From'] = formataddr([from_name, from_email])
    message['To'] = tos
    message['Cc'] = ccs
    message['Subject'] = Header(title, 'utf-8')

    # 邮件正文内容
    message.attach(MIMEText(content, 'html', 'utf-8'))

    try:
        smtpObj = smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT)
        smtpObj.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        smtpObj.sendmail(EMAIL_HOST_USER, to_emails, message.as_string())
        print("send success")
        return True
    except Exception as e:
        print("send fail")
        traceback.print_exc()
        return False



def random_str(randomlength=8):
    """
    在用(推荐)
    获取指定长度的随机字符串
    """
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.sample(chars, randomlength))


def random_str2(randomlength=8):
    """
    未使用
    获取指定长度的随机字符串 的第二种方法
    """
    code = ''
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for i in range(randomlength):
        code += random.choice(chars)
    return code
    

# def random_str3(randomlength=8):
#     """
#     未使用
#     获取指定长度的随机字符串的第三种方法
#     """
#     code = ''
#     chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
#     length = len(chars) - 1
#     random = Random()
#     for i in range(randomlength):
#         code += chars[random.randint(0, length)]
#     return code


def send_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()
    if send_type == 'register':
        email_title = '注册账户邮箱验证激活链接' # 邮件标题
        email_body = f'请点击下面的链接激活你的账号: http://127.0.0.1:8000/users/active/{code}'  # 邮件内容
        send_status = sendmail(
            title=email_title, content=email_body, to_emails=[email])
    if send_type == 'forgetpwd':
        email_title = '忘记密码邮箱验证激活链接' # 邮件标题
        email_body = f'请点击下面的链接重置您的密码: http://127.0.0.1:8000/users/resetpwd/{code}'  # 邮件内容
        send_status = sendmail(
            title=email_title, content=email_body, to_emails=[email])


