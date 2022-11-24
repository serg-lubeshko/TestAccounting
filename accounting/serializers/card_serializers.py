from decimal import Decimal

from django.db.models import Sum
from rest_framework import serializers

from accounting.models import Card, Transactions


class BalanceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = (
            'card_name',
            'beg_balance',
        )


class BalanceListSerializer(serializers.ModelSerializer):
    card_name = serializers.CharField(source='card__card_name')
    card_beg_balance = serializers.CharField(source='card__beg_balance')
    cur_balance = serializers.CharField()

    class Meta:
        model = Transactions
        fields = (
            'card_id',
            'card_name',
            'card_beg_balance',
            'cur_balance',
        )


class BalanceListSerializer2(serializers.ModelSerializer):
    # card_name = serializers.CharField(source='card__card_name')
    # card_beg_balance = serializers.CharField(source='card__beg_balance')
    # cur_balance = serializers.CharField()

    class Meta:
        model = Card
        fields = (
            'card_id',
            'card_name',
            'beg_balance',
        )

    def get_sum_transaction(self, card) -> dict:
        try:
            sum_trans = (Transactions.objects.values('card').annotate(
                sum_tr=Sum('transaction_summ', default=0)
            ) \
                         .filter(card=card))[0]
            return sum_trans
        except IndexError:
            return {'sum_tr': 0}

    def to_representation(self, instance):
        data = super().to_representation(instance)
        beg_bal = instance.beg_balance
        sum_trans = self.get_sum_transaction(instance.card_id)
        try:
            data['current_balance'] = beg_bal + sum_trans['sum_tr']
        except TypeError:
            data['current_balance'] = beg_bal
        return data
