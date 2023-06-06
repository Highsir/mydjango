# 设置APP(user)的中文名

from django.apps import AppConfig
import os
# from .models import MyUser

default_app_connfig = 'user.IndexConfig'

def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]

# 重写类IndexConfig
class IndexConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = '用户管理'