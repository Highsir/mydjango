# Generated by Django 3.2.13 on 2022-04-14 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_rename_persion_vocation_person'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': '城市信息表', 'verbose_name_plural': '城市信息表'},
        ),
        migrations.AlterModelOptions(
            name='vocation',
            options={'verbose_name': '职业信息', 'verbose_name_plural': '职业信息'},
        ),
        migrations.AlterField(
            model_name='vocation',
            name='job',
            field=models.CharField(choices=[('软件开发', '软件开发'), ('软件测试', '软件测试'), ('需求分析', '需求分析'), ('项目管理', '项目管理')], max_length=20),
        ),
    ]
