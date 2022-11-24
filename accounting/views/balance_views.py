from django.db.models import Sum, F
from rest_framework import generics

from accounting.models import Transactions
from accounting.serializers.card_serializers import BalanceListSerializer, BalanceCreateSerializer
from accounting.serializers.com_view import CommonCreate


class BalanceCreate(CommonCreate):
    """ Пользователь может создать баланса и карту"""

    serializer_class = BalanceCreateSerializer


class BalanceList(generics.ListAPIView):
    """ Пользователь может получить список баланса по картам """

    serializer_class = BalanceListSerializer

    def get_queryset(self):
        user = self.request.user.pk
        return (
            Transactions.objects.values(
                'card',
                'card__card_name',
                'card__beg_balance',
            ).annotate(sum_tr=Sum('transaction_summ')).filter(user=user)). \
            annotate(
                cur_balance=F('card__beg_balance') + F('sum_tr')
        )


# class BalanceStat(APIView):
#
#     def get(self, request):
#         data = Transactions.objects.values('user__username', 'user__email').annotate(
#             sum_income=Sum('transaction_summ', filter=Q(transaction_summ__gt=0), default=0),
#             sum_consumption=Sum('transaction_summ', filter=Q(transaction_summ__lte=0), default=0)
#         ).filter()
#         serializer = BalanceStatSerializer(data, many=True)
#         stat = serializer.data
#         return Response(serializer.data)
