from rest_framework import serializers

from accounting.models import Category


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'category_name',
            'update_date'
        )
