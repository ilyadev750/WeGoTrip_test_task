from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Good


class GoodTest(APITestCase):
    def test_create_good(self):
        """ Тест на создание товара """

        url = reverse('goods-list')
        Good.objects.create(
            name='TV Hisence',
            image='media/images/hisense_h75n5800_5.jpg',
            content='Хороший телевизор',
            price=40000
        )
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], 'TV Hisence')
        self.assertEqual(response.data[0]['content'], 'Хороший телевизор')