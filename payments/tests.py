from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Payment
from orders.models import Order
from goods.models import Good


class PaymentTest(APITestCase):
    def test_create_payment_and_pay(self):
        """ Тест на создание платежа """

        create_order_url = reverse('create-order')
        Good.objects.create(
            name='TV Hisence',
            image='media/images/hisense_h75n5800_5.jpg',
            content='Хороший телевизор',
            price=40000
        )

        create_order_data = { 
            "order" : [
                {
                    "good_pk": "1",
                    "quantity": "1"
                }
            ]
        }

        self.client.post(
            create_order_url,
            create_order_data,
            format='json')
        
        create_payment_data = { 
            "order_id": "1",
            "payment_type": "наличные"
        }
        create_payment_url = reverse('create-payment')

        response = self.client.post(
            create_payment_url,
            create_payment_data,
            format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['ID платежа'], 1)
        self.assertEqual(response.data['Тип платежа'], "наличные")
        self.assertEqual(response.data['Сумма'], 40000)