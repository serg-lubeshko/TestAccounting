from rest_framework import generics, status
from rest_framework.response import Response

from accounting.serializers.transaction_serializers import TransactionCreateSerializer
from x1Lubeshko.settings import REPLY_TEXTS


class TransactionCreate(generics.CreateAPIView):
    """ Пользователь может  создавать свои транзакции """

    serializer_class = TransactionCreateSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        return context