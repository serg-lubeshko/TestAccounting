from rest_framework import serializers

from accounting.models import Card


class BalanceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = (
            'card_name',
            'beg_balance',
        )


class BalanceListSerializer(serializers.ModelSerializer):
    cur_balance = serializers.CharField(source='card.sum_cur')

    class Meta:
        model = Card
        fields = (
            'card_id',
            'card_name',
            'beg_balance',
            'cur_balance',
        )
