from django.contrib import admin
from .models import Order
from django.utils.html import format_html
from django.urls import reverse
from django.shortcuts import redirect
from django import forms
from datetime import datetime
import requests
import os
from dotenv import load_dotenv


load_dotenv()


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['time_of_conformation'].required = False
        self.fields['payment_id'].required = False


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    form = OrderForm

    list_display = ('id',
                    'total_sum',
                    'status',
                    'time_of_creation',
                    'time_of_conformation',
                    'payment',
                    'conformation')

    def changeform_view(self,
                        request,
                        object_id,
                        form_url='',
                        extra_context=None):

        extra_context = extra_context or {}
        object = Order.objects.get(pk=object_id)

        if object.payment_id:
            if (object.payment_id.status == 'оплачен' and
                    object.status != 'подтвержден'):
                extra_context['custom_button'] = True

        return super().changeform_view(
            request,
            object_id,
            form_url,
            extra_context)

    def response_change(self, request, obj):

        if "_custom_button" in request.POST:
            obj.status = 'подтвержден'
            obj.time_of_conformation = datetime.now()
            obj.save()

            requests.post(
                os.environ['webhook_url'],
                data={
                    "id": obj.pk,
                    "amount": obj.total_sum,
                    "time_of_conformation": obj.time_of_conformation
                }
            )

            url = reverse('admin:orders_order_changelist')
            return redirect(url)

        else:
            return super().response_change(request, obj)

    def payment(self, obj):
        if obj.payment_id:

            url = reverse('admin:payments_payment_change',
                          args=(obj.payment_id.pk,))
            return format_html('<a class="button" href="{}">{}</a>',
                               url,
                               obj.payment_id.pk)

        else:
            return 'Не назначен'

    def conformation(self, obj):
        if obj.payment_id:

            status = obj.payment_id.status
            if status == 'оплачен':

                if obj.status == 'подтвержден':
                    return 'Подтвержден'
                else:
                    url = reverse(
                        'admin:orders_order_change',
                        args=(obj.pk, ))
                    return format_html(
                        '<a class="button" href="{}">{}</a>',
                        url,
                        'Подтвердить')

            else:
                return 'Невозможно'

        return 'Невозможно'

    conformation.short_description = "Подтверждение"
    payment.short_description = "Платеж"
