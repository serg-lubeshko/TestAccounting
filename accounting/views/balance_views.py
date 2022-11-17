from django.db.models import Sum, Q
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from accounting.models import Card, Transactions
from accounting.serializers.balance_serializers import BalanceStatSerializer
from accounting.serializers.card_serializers import BalanceListSerializer


class BalanceList(generics.ListAPIView):
    """ Пользователь может получить список баланса по картам """

    serializer_class = BalanceListSerializer

    def get_queryset(self):
        user = self.request.user
        return Card.objects.filter(user=user).select_related('card')


class BalanceStat(APIView):

    def get(self, request):
        data = Transactions.objects.values('user__username', 'user__email').annotate(
            sum_income=Sum('transaction_summ', filter=Q(transaction_summ__gt=0), default=0),
            sum_consumption=Sum('transaction_summ', filter=Q(transaction_summ__lte=0), default=0)
        ).filter()
        serializer = BalanceStatSerializer(data, many=True)
        stat = serializer.data
        return Response(serializer.data)

    # def sen