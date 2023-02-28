from django.db import models


class Item(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=50
        )

    description = models.TextField(
        verbose_name='Описание',
        max_length=2000,
        null=True,
        )

    price = models.IntegerField(
        verbose_name='Цена'
        )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Order(models.Model):
    items = models.ManyToManyField(
        'Item',
        verbose_name='Предмет'
        )
