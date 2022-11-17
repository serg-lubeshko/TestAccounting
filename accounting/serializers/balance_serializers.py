from rest_framework import serializers
from rest_framework.fields import DecimalField

from accounting.models import Transactions


class BalanceStatSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user__username')
    email = serializers.CharField(source='user__email')
    sum_income = DecimalField(max_digits=10, decimal_places=2)
    sum_consumption = DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Transactions
        fields = (
            'user',
            'email',
            'sum_income',
            'sum_consumption',
        )
