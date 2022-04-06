from django.db import models


class PersonInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "人员信息表"


class Vocation(models.Model):
    id = models.AutoField(primary_key=True)
    job = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    payment = models.IntegerField(null=True, blank=True)
    persion = models.ForeignKey(PersonInfo, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = '职业信息'


class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        app_label = "index"
        db_table = "city"
        verbose_name = "城市信息表"


