from rest_framework import generics
from rest_framework.exceptions import NotFound

from accounting.models import Category
from accounting.permission.permissions import IsAnAuthor
from accounting.serializers.category_serializers import CategoryUpdateSerializer, CategorySerializer
from accounting.serializers.com_view import CommonCreate


class CategoryCreate(CommonCreate):
    """ User can create their own categories """

    serializer_class = CategorySerializer


class CategoryList(generics.ListAPIView):
    """ User can get a list of their categories """

    serializer_class = CategorySerializer

    def get_queryset(self):
        try:
            user = self.request.user
            queryset = Category.objects.filter(user=user)
        except Exception:
            raise NotFound()
        return queryset


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """ User can change/delete categories """

    permission_classes = [IsAnAuthor]
    queryset = Category.objects.all()
    serializer_class = CategoryUpdateSerializer
    lookup_url_kwarg = 'category_id'
