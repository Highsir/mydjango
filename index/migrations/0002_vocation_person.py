# Generated by Django 3.2.17 on 2023-06-05 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('index', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vocation',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.personinfo'),
        ),
    ]