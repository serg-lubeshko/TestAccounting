from rest_framework import generics
from rest_framework.exceptions import NotFound

from accounting.models import Category
from accounting.permission.permissions import IsAnAuthor
from accounting.serializers.category_serializers import CategoryUpdateSerializer, CategorySerializer
from accounting.serializers.com_view import CommonCreate


class CategoryCreate(CommonCreate):
    """ Пользователь может  создавать свои категории """

    serializer_class = CategorySerializer


class CategoryList(generics.ListAPIView):
    """ Пользователь может получить список своих категорий """

    serializer_class = CategorySerializer

    def get_queryset(self):
        try:
            user = self.request.user
            queryset = Category.objects.filter(user=user)
        except Exception:
            raise NotFound()
        return queryset


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Пользователь может изменять/удалять категории """

    permission_classes = [IsAnAuthor]
    queryset = Category.objects.all()
    serializer_class = CategoryUpdateSerializer
    lookup_url_kwarg = 'category_id'
