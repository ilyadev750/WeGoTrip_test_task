from django.core.management.base import BaseCommand
from goods.models import Good
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.images import ImageFile


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        goods = [
            {'name': 'Телевизор Sony',
             'image': 'test_images/sony-tv.jpg',
             'content': 'Отличный современный телевизор!',
             'price': 50000},

             {'name': 'Холодильник Gorenje',
             'image': 'test_images/gorenje-fridge.jpg',
             'content': 'Надежный словенский холодильник!',
             'price': 45000}
        ]

        for good in goods:
            try:
                Good.objects.get(name=good['name'])
            except ObjectDoesNotExist:
                image = ImageFile(open(good['image'], "rb")) 
                Good.objects.create(
                    name=good['name'],
                    image=image,
                    content=good['content'],
                    price=good['price']
                )