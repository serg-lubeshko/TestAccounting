from django.core.management.base import BaseCommand

from accounting.management.data import users_data, сategory_data
from accounting.models import Category
from users.models import MyUser


class Command(BaseCommand):
    """ Class for loading the main project parameters into the database """

    def handle(self, *args, **options):
        if MyUser.objects.all().count() == 0:
            for item_user in users_data.user_admin:
                MyUser.objects.create_superuser(**item_user)

        if Category.objects.all().count() == 0:
            for item in сategory_data.categories:
                Category.objects.create(**item | {'user_id': 1})
