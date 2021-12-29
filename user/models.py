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
