from decimal import Decimal

from django.db.models import F
from rest_framework import generics, status
from rest_framework.response import Response

from accounting.models import Transactions, CardBalance
from accounting.permission.permissions import IsAnAuthor
from accounting.serializers.transaction_serializers import TransactionCreateSerializer, TransactionUpdateSerializer


class TransactionCreate(generics.CreateAPIView):
    """ Пользователь может  создавать свои транзакции """

    serializer_class = TransactionCreateSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        return context


class TransactionDelete(generics.DestroyAPIView):
    """ Пользователь может  удалять свои транзакции """

    queryset = Transactions.objects.all()
    lookup_url_kwarg = 'transaction_id'
    # TODO заменить serializer
    serializer_class = TransactionCreateSerializer
    permission_classes = [IsAnAuthor]


class TransactionUpdate(generics.RetrieveUpdateAPIView):
    """ Пользователь может  удалять свои транзакции """

    queryset = Transactions.objects.all()
    lookup_url_kwarg = 'transaction_id'
    # TODO заменить serializer
    serializer_class = TransactionUpdateSerializer
    permission_classes = [IsAnAuthor]

    def _perform_update(self, elem):
        if new_cur_sum := elem.initial_data.get('transaction_summ', None):
            id_card = elem.instance.card_id
            cur_sum_trans = elem.instance.transaction_summ
            obj = CardBalance.objects.get(card=id_card)
            cur_balance_card = obj.sum_cur
            new_cur_bal = cur_balance_card-Decimal(cur_sum_trans)+Decimal(new_cur_sum)
            obj.sum_cur = new_cur_bal
            obj.save()

            print(new_cur_sum, 'tututututu')
        print(elem.initial_data, 'oooooooooo')
        print(elem.__dict__)
        elem.save()
        # inv_card_id = elm.pop("inv_card_id")
        # InvCard.objects.filter(inv_card_id=inv_card_id).update(**elm)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)

        if serializer.is_valid():
            self._perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({
            "fieldErrors": serializer.errors
        },
            status=status.HTTP_422_UNPROCESSABLE_ENTITY
        )
