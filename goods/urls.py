from django.urls import path
from .views import GoodView


urlpatterns = [
    path("", GoodView.as_view(), name='goods-list')
]
