from rest_framework import serializers
from .models import Good


class GoodSerializer(serializers.ModelSerializer):
    """ Сериализатор товара """

    class Meta:
        model = Good
        fields = '__all__'
