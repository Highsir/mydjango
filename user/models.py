from django.contrib.auth.models import AbstractUser
from django.db import models


class PersonInfo(models.Model):
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=100)
    live = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        app_label = "user"
        db_table = "user"
        verbose_name = "个人信息表"
        verbose_name_plural = "个人信息表"

class MyUser(AbstractUser):
    qq = models.CharField('QQ号码', max_length=16)
    weChat = models.CharField('微信账号', max_length=100)
    mobile = models.CharField('手机号码', max_length=11)

    def __str__(self):
        return self.username
