from django.db import models


class Payment(models.Model):
    STATUS_CHOICES = [
        ("не оплачен", "Не оплачен"),
        ("оплачен", "Оплачен"),
    ]
    PAYMENT_CHOICES = [
        ("наличные", "Наличные"),
        ("карта", "Карта")
    ]

    total_sum = models.IntegerField(
        verbose_name='Сумма платежа')

    status = models.CharField(
        verbose_name='Статус платежа',
        choices=STATUS_CHOICES,
        max_length=100)

    payment_type = models.CharField(
        verbose_name='Тип оплаты',
        choices=PAYMENT_CHOICES,
        max_length=100)

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'

    def __str__(self):
        return f'{self.pk}'
