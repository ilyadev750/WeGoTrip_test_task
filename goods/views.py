from .models import Good
from .serializers import GoodSerializer
from rest_framework.generics import ListAPIView


class GoodView(ListAPIView):
    serializer_class = GoodSerializer

    def get_queryset(self):
        return Good.objects.all()
