from rest_framework import generics, status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from accounting.models import Category
from accounting.permission.permissions import IsAnAuthor
from accounting.serializers.category_serializers import CategoryCreateSerializer, CategoryListSerializer, \
    CategoryUpdateSerializer
from x1Lubeshko.settings import REPLY_TEXTS


class CategoryCreate(generics.CreateAPIView):
    """ Пользователь может  создавать свои категории """

    serializer_class = CategoryCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({
                "message": REPLY_TEXTS[1],
                "data": serializer.data
            }, status=status.HTTP_201_CREATED, )
        else:
            return Response({
                "fieldErrors": serializer.errors
            },
                status=status.HTTP_400_BAD_REQUEST
            )


class CategoryList(generics.ListAPIView):
    """ Пользователь может получить список своих категорий """

    serializer_class = CategoryListSerializer

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
