from django.test import TestCase
from django.urls import reverse

from accounting.management.data import сategory_data
from accounting.models import Transactions, Category, Card, Organization
from users.models import MyUser


class TransactionViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        transaction_type_1 = 5
        transaction_type_2 = 3
        sum = 100
        categ = 1
        org = 1

        for item in range(1, 3):
            obj = MyUser.objects.create_user(
                username=f"user{item}",
                password=f"user{item}",
                email=f"user{item}@tut.by"
            )

        for item in range(1, 10):
            obj = Card.objects.create(
                card_name=f"card{item}",
                beg_balance=10000,
                user_id=1
            )

            obj = Organization.objects.create(
                organization_name=f"org{item}",
                user_id=1
            )

            # CardBalance.objects.create(
            #     card_id=obj.pk,
            #     sum_cur=10000
            # )

        for item in сategory_data.categories:
            Category.objects.create(**item | {'user_id': 1})

        for item in range(transaction_type_1):
            Transactions.objects.create(
                transaction_summ=sum,
                category_id=categ,
                organization_id=org,
                operation_type=1,
                card_id=1,
                user_id=1
            )
            sum += 50
            org += 1
            categ += 1

        for item in range(transaction_type_2):
            Transactions.objects.create(
                transaction_summ=sum,
                category_id=categ,
                organization_id=org,
                operation_type=2,
                card_id=1,
                user_id=1
            )

            sum += 30
            org += 1
            categ += 1

    def test_logged_in_with_permission(self):
        self.client.login(username='user1', password='user1')
        resp = self.client.get(reverse("category-list"))
        print(resp.json())
        self.assertEqual(resp.status_code, 200)
