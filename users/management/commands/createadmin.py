from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        User = get_user_model()
        try:
            User.objects.create_superuser(
                    username = 'root',
                    email = 'root@root.com',
                    password = 'root'
                )
        except:
            print('Администратор уже существует!')