from django.db import models


class Thematics(models.Model):
    topic = models.CharField(max_length=30, verbose_name='Раздел')
    topic2 = models.TextField(max_length=30, verbose_name='Раздел2', default=0)

    class Meta:
        verbose_name = 'Тематика статьи'
        verbose_name_plural = 'Тематики статьи'

    def __str__(self):
        return self.topic


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    scopes = models.ManyToManyField(Thematics, through='Relationship',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Relationship(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    thematics = models.ForeignKey(Thematics, on_delete=models.CASCADE, verbose_name='РАЗДЕЛ',)
    is_main = models.BooleanField(verbose_name='Основной',)
