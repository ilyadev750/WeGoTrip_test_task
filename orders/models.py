from django.db import models
from django.utils import timezone
from payments.models import Payment


class Order(models.Model):
    STATUS_CHOICES = [
        ("создан", "Создан"),
        ("подтвержден", "Подтвержден"),
    ]

    total_sum = models.IntegerField(
        verbose_name='Сумма заказа'
    )

    status = models.CharField(
        verbose_name='Статус заказа',
        choices=STATUS_CHOICES,
        max_length=100
    )

    time_of_creation = models.DateTimeField(
        verbose_name='Время создания',
        default=timezone.now
    )

    time_of_conformation = models.DateTimeField(
        verbose_name='Время подтверждения',
        default=None,
        null=True
    )

    payment_id = models.OneToOneField(
        Payment,
        verbose_name='Платеж',
        on_delete=models.SET_NULL,
        default=None,
        null=True
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.pk}'
