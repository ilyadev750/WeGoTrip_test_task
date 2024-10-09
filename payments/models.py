from django.db import models
from orders.models import Order

class Payment(models.Model):
    STATUS_CHOICES = [
        ("не оплачен", "Не оплачен"),
        ("оплачен", "Оплачен"),
    ]
    PAYMENT_CHOICES = [
        ("наличные", "Наличные"),
        ("карта", "Карта")
    ]

    total_sum = models.IntegerField(verbose_name='Сумма платежа')
    status = models.CharField(verbose_name='Статус заказа', choices=STATUS_CHOICES, max_length=100)
    payment_type = models.CharField(verbose_name='Тип оплаты', choices=PAYMENT_CHOICES, max_length=100)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Заказ")

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'

    def __str__(self):
        return f'{self.pk}'
