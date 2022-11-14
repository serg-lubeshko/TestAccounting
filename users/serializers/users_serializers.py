from rest_framework import serializers

from accounting.management.data.сategory_data import categories
from accounting.models import Category
from users.models import MyUser


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = (
            'email',
            'username',
            'password',
        )
        extra_kwargs = {

            "password": {"write_only": True},
        }

    def create(self, validated_data: dict):
        passw = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(passw)
        user.save()
        list_categ_default = []
        for item in categories:
            ctegory_default = Category(
                category_name=item.get('category_name'),
                user=user
            )
            list_categ_default.append(ctegory_default)
        Category.objects.bulk_create(list_categ_default)
        return user
