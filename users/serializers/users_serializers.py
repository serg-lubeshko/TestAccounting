from rest_framework import serializers

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
        return user
