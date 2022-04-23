from django.db import models
from user.models import PersonInfo
from django.utils.html import format_html


# class PersonInfo(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=20)
#     age = models.IntegerField()
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = "人员信息表"


class Vocation(models.Model):
    JOB = (
        ('软件开发', '软件开发'),
        ('软件测试', '软件测试'),
        ('需求分析', '需求分析'),
        ('项目管理', '项目管理'),
    )
    id = models.AutoField(primary_key=True)
    job = models.CharField(max_length=20,choices=JOB)
    title = models.CharField(max_length=20)
    payment = models.IntegerField(null=True, blank=True)
    person = models.ForeignKey(PersonInfo, on_delete=models.CASCADE)
    recordTime = models.DateField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = '职业信息'
        verbose_name_plural = '职业信息'

    # 自定义函数, 设置字体颜色
    def colored_name(self):
        if 'Lucy' in self.person.name:
            color_code = 'red'
        else:
            color_code = 'blue'
        return format_html('<span style="color: {};">{}</span>',
                           color_code,
                           self.person.name)
    colored_name.short_decription = "带颜色的名字"


class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        app_label = "index"
        db_table = "city"
        verbose_name = "城市信息表"
        verbose_name_plural = "城市信息表"
