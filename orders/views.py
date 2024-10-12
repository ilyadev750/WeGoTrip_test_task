from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from goods.models import Good
from .models import Order
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist


class OrderView(APIView):
    parser_classes = [JSONParser]

    def post(self, request):
        """ Создать заказ. Пример тела запроса
        {
            "order" : [
                {
                    "good_pk": "1",
                    "quantity": "3",
                },
                {
                    "good_pk": "1",
                    "quantity": "2",
                }
            ]
        }
        """

        order_sum = 0
        data = request.data
        order_goods = data["order"]

        for good in order_goods:

            try:
                item = Good.objects.get(pk=int(good["good_pk"]))
                order_sum += item.price * int(good["quantity"])

            except (ObjectDoesNotExist, KeyError):
                return Response(
                    status=404,
                    data={'Ошибка': "Товар не найден или неверные данные!"}
                )

        order = Order.objects.create(
            total_sum=order_sum,
            status="создан"
        )

        return Response(status=201,
                        data={'Успех': "Заказ успешно создан!",
                              'ID нового заказа': order.pk,
                              'Сумма заказа': order.total_sum})
