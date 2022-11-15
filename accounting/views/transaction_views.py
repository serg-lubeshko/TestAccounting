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

    # def post(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save(user=request.user)
    #         return Response({
    #             "message": REPLY_TEXTS[1],
    #             "data": serializer.data
    #         }, status=status.HTTP_201_CREATED, )
    #     else:
    #         return Response({
    #             "fieldErrors": serializer.errors
    #         },
    #             status=status.HTTP_400_BAD_REQUEST
    #         )