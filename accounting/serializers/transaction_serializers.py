from rest_framework import serializers

from accounting.models import Transactions, Organization, Category


class TransactionCreateSerializer(serializers.ModelSerializer):
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

    def validate(self, attrs):
        request = self.context.get("request")
        try:
            org = attrs['organization']
            cat = attrs['category']
        except KeyError:
            if request.method == 'PATCH':
                return attrs

        if Organization.objects.filter(organization_id=attrs['organization'].pk).filter(
                user_id=request.user.pk).exists() and \
                Category.objects.filter(category_id=attrs['category'].pk).filter(user_id=request.user.pk).exists():
            return attrs
        else:
            raise serializers.ValidationError("Сheck the organization or category")

    def create(self, validated_data: dict):
        user = self.context['user']
        operation_type = validated_data.get('operation_type', None)
        if operation_type == 2:
            validated_data['transaction_summ'] = validated_data['transaction_summ'] * (-1)
        return Transactions.objects.create(**validated_data | {'user': user})


class TransactionUpdateSerializer(TransactionCreateSerializer):
    class Meta:
        model = Transactions
        fields = (
            'transaction_summ',
            'category',
            'organization',
            'info',
            'operation_type',
        )
