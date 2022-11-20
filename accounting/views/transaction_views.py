from decimal import Decimal

from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from rest_framework import generics, status
from rest_framework.response import Response

from accounting.models import Transactions
from accounting.permission.permissions import IsAnAuthor
from accounting.serializers.transaction_serializers import TransactionCreateSerializer, TransactionUpdateSerializer, \
    TransactionListSerializer
from accounting.service.ordering import CustomOrderFilter


@extend_schema_view(
    get=extend_schema(parameters=[
        OpenApiParameter(name='transaction_id', description="specify the number"),
        OpenApiParameter(name='date_operation', description="specify in format <yyyy-mm-dd format>"),
        OpenApiParameter(name='transaction_summ', description="specify transaction sum"),
        OpenApiParameter(name='category', description="specify category <int>"),
        OpenApiParameter(name='organization', description="specify organization <int>"),
        OpenApiParameter(name='info', description="specify info"),
        OpenApiParameter(name='operation_type', description="specify operation_type <int>"),
    ])
)
class TransactionList(generics.ListAPIView, CustomOrderFilter):
    """ Пользователь может  создавать свои транзакции """

    serializer_class = TransactionListSerializer
    filter_backends = [CustomOrderFilter]
    ordering = ['-transaction_id']

    custom_order_fields = {
        'transaction_id': 'transaction_id',
        'date_operation': 'date_operation',
        'transaction_summ': 'transaction_summ',
        'category': 'category',
        'organization': 'organization',
        'info': 'info',
        'operation_type': 'operation_type'
    }

    custom_filter_fields = {
        'transaction_id': 'transaction_id',
        'date_operation': 'date_operation__date',
        'transaction_summ': 'transaction_summ__icontains',
        'category': 'category',
        'organization': 'organization',
        'info': 'info__icontains',
        'operation_type': 'operation_type',
    }

    type = {
        'transaction_id': int,
        'date_operation__date': str,
        'transaction_summ': str,
        'category': int,
        'organization': int,
        'info__icontains': str,
        'operation_type': 1,
    }

    def get_queryset(self):
        user = self.request.user
        queryset = Transactions.objects.filter(user=user)
        return self.filter_queryset(queryset)


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
    # serializer_class = TransactionCreateSerializer
    permission_classes = [IsAnAuthor]


class TransactionUpdate(generics.RetrieveUpdateAPIView):
    """ Пользователь может  редактировать свои транзакции """

    queryset = Transactions.objects.all()
    lookup_url_kwarg = 'transaction_id'
    serializer_class = TransactionUpdateSerializer
    permission_classes = [IsAnAuthor]

    def _perform_update(self, transaction_elem):
        oper_type = transaction_elem.initial_data.get('operation_type', transaction_elem.instance.operation_type)
        Koef = 1 if oper_type == 1 else -1
        if new_cur_sum := transaction_elem.initial_data.get('transaction_summ', None):
            cur_sum_trans = transaction_elem.instance.transaction_summ
            obj_card = transaction_elem.instance.card
            obj_balance = obj_card.card
            cur_balance_card = obj_balance.sum_cur
            new_cur_bal = cur_balance_card - Decimal(cur_sum_trans) + Decimal(new_cur_sum) * Koef
            obj_balance.sum_cur = new_cur_bal
            obj_balance.save()
        return transaction_elem.save()

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
