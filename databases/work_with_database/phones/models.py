from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.CharField(max_length=50)


