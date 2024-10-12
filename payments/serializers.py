from rest_framework import serializers
from .models import Payment
from django.core.exceptions import ObjectDoesNotExist
from orders.models import Order
from rest_framework.exceptions import ValidationError


class PaymentSerializer(serializers.Serializer):
    order_id = serializers.IntegerField(
        required=True)

    payment_type = serializers.CharField(
        required=True,
        max_length=50)

    def create(self, request):
        """ Создать новый платеж, привязать его к заказу """
        try:
            order = Order.objects.get(
                pk=int(self.validated_data.get("order_id"))
            )

        except (ObjectDoesNotExist, TypeError):
            raise ValidationError(
                'Данного заказа не существует!')

        if order.payment_id:
            raise ValidationError(
                'Платеж у выбранного заказа уже существует!')
        
        payment_type = self.validated_data.get("payment_type")
        checked_payment_type = None

        for type in Payment.PAYMENT_CHOICES:
            if payment_type == type[0]:
                checked_payment_type = payment_type

        if not checked_payment_type:
            raise ValidationError(
                'Неверный тип платежа!'
            )

        payment = Payment.objects.create(
            total_sum=order.total_sum,
            status="не оплачен",
            payment_type=checked_payment_type,
        )

        order.payment_id = payment
        order.save()

        return payment
