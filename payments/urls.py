from django.urls import path
from .views import PaymentView, SetPaymentAsPaid


urlpatterns = [

    path("create",
         PaymentView.as_view(),
         name='create-payment'),

    path("paid/<int:payment_id>",
         SetPaymentAsPaid.as_view(),
         name='set-payment-as-paid')

]
