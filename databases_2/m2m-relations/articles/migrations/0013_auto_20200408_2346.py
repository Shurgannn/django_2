# Generated by Django 2.2.9 on 2020-04-08 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_auto_20200406_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationship',
            name='is_main',
            field=models.BooleanField(verbose_name='Основной'),
        ),
    ]