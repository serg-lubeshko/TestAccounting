from rest_framework import generics

from accounting.models import Card
from accounting.serializers.card_serializers import BalanceCreateSerializer, \
    BalanceListSerializer2
from accounting.serializers.com_view import CommonCreate


class BalanceCreate(CommonCreate):
    """ User can create balance and card """

    serializer_class = BalanceCreateSerializer


class BalanceList(generics.ListAPIView):
    """ User can get list of card balances """

    serializer_class = BalanceListSerializer2

    def get_queryset(self):
        user = self.request.user.pk
        return Card.objects.filter(user=user)

