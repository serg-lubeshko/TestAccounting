from rest_framework import generics, status

from users.serializers.users_serializers import UserCreateSerializer


class UserCreate(generics.CreateAPIView):
    serializer_class = UserCreateSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
