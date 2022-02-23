from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):

    def handle(self, *args, **options):
        User = get_user_model()
        if User.objects.filter(is_superuser=1).count() == 0:
            if os.environ.get('DJANGO_SU_NAME', None):
                DJANGO_SU_NAME = os.environ.get('DJANGO_SU_NAME')
                DJANGO_SU_EMAIL = os.environ.get('DJANGO_SU_EMAIL')
                DJANGO_SU_PASSWORD = os.environ.get('DJANGO_SU_PASSWORD')

                superuser = User.objects.create_superuser(
                    username=DJANGO_SU_NAME,
                    email=DJANGO_SU_EMAIL,
                    password=DJANGO_SU_PASSWORD)

                superuser.save()
                self.stdout.write('Created Admin account')
        else:
            self.stdout.write('Admin account can only be initialized if no Account exist')