from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from .models import Payment
from .serializers import PaymentSerializer
from rest_framework.response import Response


class PaymentView(APIView):
    parser_classes = [JSONParser]

    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        payment = serializer.create(request)

        return Response(status=201,
                        data={'Успех!': "Платеж успешно создан!",
                              'ID платежа': payment.pk})


class SetPaymentAsPaid(APIView):

    def patch(self, request, payment_id):
        payment = Payment.objects.get(pk=payment_id)
        payment.status = 'оплачен'
        payment.save()

        return Response(status=201,
                        data={'Успех!': "Платеж успешно оплачен!",
                              'ID платежа': payment.pk})
