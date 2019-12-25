from django.db import models

# Create your models here.


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    operating_system = models.CharField(max_length=50)

# class Nokiaa(Phone):
#     flashlight = models.CharField(max_length=50)
#
#
# class Iphone(Phone):
#     finger_scaner = models.CharField(max_length=50)


