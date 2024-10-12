from django.db import models


class Good(models.Model):
    """ Модель товара """
    name = models.CharField(verbose_name="Название товара", max_length=255)
    image = models.ImageField(upload_to='images', verbose_name="Изображение")
    content = models.TextField(max_length=3000, verbose_name="Описание товара")
    price = models.IntegerField(verbose_name='Стоимость товара')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.name}'
