from decimal import Decimal

from django.db.models import Sum, F, Prefetch
from rest_framework import generics

from accounting.models import Transactions, Card
from accounting.serializers.card_serializers import BalanceListSerializer, BalanceCreateSerializer, \
    BalanceListSerializer2
from accounting.serializers.com_view import CommonCreate


class BalanceCreate(CommonCreate):
    """ Пользователь может создать баланса и карту"""

    serializer_class = BalanceCreateSerializer


class BalanceList(generics.ListAPIView):
    """ Пользователь может получить список баланса по картам """

    serializer_class = BalanceListSerializer2

    def get_queryset(self):
        user = self.request.user.pk
        return Card.objects.filter(user=user)

        # return (
        #     Transactions.objects.values(
        #         'card',
        #         'card__card_name',
        #         'card__beg_balance',
        #     ).annotate(sum_tr=Sum('transaction_summ')).filter(user=user)). \
        #     annotate(
        #         cur_balance=F('card__beg_balance') + F('sum_tr')
        # )


