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
