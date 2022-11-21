from rest_framework import generics, status
from rest_framework.permissions import AllowAny

from users.models import MyUser
from users.serializers.users_serializers import UserCreateSerializer, UserListSerializer


class UserCreate(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny,]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UserList(generics.ListAPIView):
    serializer_class = UserListSerializer
    queryset = MyUser.objects.all()