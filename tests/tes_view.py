from django.test import TestCase
from django.urls import reverse

from accounting.management.data import сategory_data
from accounting.models import Transactions, Category, Card


class TransactionViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        transaction_type_1 = 5
        transaction_type_2 = 5
        sum = 100
        categ = 1
        org = 1

        for item in range(3):
            obj = Card.objects.create(
                card_name=f"card{item}",
                beg_balance=10000
            )


        for item in сategory_data.categories:
            Category.objects.create(**item)

        for item in range(transaction_type_1):
            Transactions.objects.create(
                transaction_summ=sum,
                category=categ,
                organization=org,
                operation_type=1,
                card=1
            )
            sum += 50
            org += 1
            categ += 1
