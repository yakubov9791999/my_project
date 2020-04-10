from django.db import models


# Create your models here.
class PizzaShop(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название Магазина')
    desc = models.TextField(verbose_name='Описание')
    rating = models.FloatField(default=0, verbose_name='Рейтинг')
    url = models.URLField(verbose_name='Индернет адрес мазазин')

    class Meta:
        verbose_name='Пиццерия'
        verbose_name_plural='Пиццерии'

    def __str__(self):
        return self.name

class Pizza(models.Model):

    pizzashop = models.ForeignKey(PizzaShop, verbose_name='Название Магазина', on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name='Название Пицца')
    desc = models.TextField(verbose_name='Описание')
    price = models.IntegerField(default=0, verbose_name='Цена')
    photo = models.ImageField(verbose_name='Фото', default='', upload_to='my_app/photos/', blank=True)

    class Meta:
        verbose_name = 'Пицца'
        verbose_name_plural = 'Пиццы'
        ordering = ['price']

    def __str__(self):
        return self.name