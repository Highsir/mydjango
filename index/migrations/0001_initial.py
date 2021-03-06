# Generated by Django 3.2.13 on 2022-04-12 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': '城市信息表',
                'db_table': 'city',
            },
        ),
        migrations.CreateModel(
            name='Vocation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('job', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=20)),
                ('payment', models.IntegerField(blank=True, null=True)),
                ('recordTime', models.DateField(auto_now=True, null=True)),
                ('persion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.personinfo')),
            ],
            options={
                'verbose_name': '职业信息',
            },
        ),
    ]
