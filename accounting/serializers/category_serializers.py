from rest_framework import serializers

from accounting.models import Category


class CategorySerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = (
            'category_id',
            'category_name',
            'update_date'
        )


class CategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'category_name',
        )
