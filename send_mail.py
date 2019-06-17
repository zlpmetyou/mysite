import os

from django.core.mail import send_mail


os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':
    send_mail('welcome',
              '欢迎啊',
              'zlp_go@sina.com',
              ['389797999@qq.com'])
