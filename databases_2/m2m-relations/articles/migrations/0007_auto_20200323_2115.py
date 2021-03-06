# Generated by Django 2.2.9 on 2020-03-23 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20200323_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationship',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article', verbose_name='ТЕМАТИКИ СТАТЬИ'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='thematics',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Thematics', verbose_name='РАЗДЕЛ'),
        ),
    ]
