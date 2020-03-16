# Generated by Django 3.0.4 on 2020-03-12 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thematics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Раздел')),
            ],
            options={
                'verbose_name': 'Тематика статьи',
                'verbose_name_plural': 'Тематики статьи',
            },
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article')),
                ('thematics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Thematics')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='thematic',
            field=models.ManyToManyField(through='articles.Relationship', to='articles.Thematics'),
        ),
    ]
