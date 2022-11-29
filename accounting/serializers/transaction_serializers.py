from rest_framework import serializers

from accounting.models import Transactions, Organization, Category, Card


class TransactionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = (
            'transaction_summ',
            'category',
            'organization',
            'info',
            'operation_type',
        )

    def validate_organization(self, attrs):
        request = self.context.get("request")
        if Organization.objects.filter(organization_id=attrs.pk).filter(user_id=request.user.pk).exists():
            return attrs
        raise serializers.ValidationError("Сheck the organization")

    def validate_category(self, attrs):
        request = self.context.get("request")
        if Category.objects.filter(category_id=attrs.pk).filter(user_id=request.user.pk).exists():
            return attrs
        raise serializers.ValidationError("Сheck the category")




class TransactionCreateSerializer(TransactionUpdateSerializer):
    transaction_summ = serializers.DecimalField(max_digits=10, decimal_places=2, min_value=0)
    class Meta:
        model = Transactions
        fields = (
            'transaction_summ',
            'category',
            'organization',
            'info',
            'operation_type',
            'card'
        )

    def create(self, validated_data: dict):
        user = self.context['user']
        return Transactions.objects.create(**validated_data | {'user': user})

    def validate_card(self, attrs):
        request = self.context.get("request")
        if Card.objects.filter(card_id=attrs.pk).filter(user_id=request.user.pk).exists():
            return attrs
        raise serializers.ValidationError("Сheck the card")


class TransactionListSerializer(TransactionCreateSerializer):
    class Meta:
        model = Transactions
        fields = (
            'transaction_id',
            'transaction_summ',
            'category',
            'organization',
            'info',
            'operation_type',
            'date_operation'
        )
