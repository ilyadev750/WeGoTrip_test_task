from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Order
from goods.models import Good


class OrderTest(APITestCase):
    def test_create_order(self):
        """ Тест на создание заказа """

        url = reverse('create-order')
        Good.objects.create(
            name='TV Hisence',
            image='media/images/hisense_h75n5800_5.jpg',
            content='Хороший телевизор',
            price=40000
        )

        data = { 
            "order" : [
                {
                    "good_pk": "1",
                    "quantity": "2"
                }
            ]
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['ID нового заказа'], 1)
        self.assertEqual(response.data['Сумма заказа'], 80000)
