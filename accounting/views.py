from rest_framework import generics, status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from accounting.models import Category
from accounting.serializers.category_serializers import CategoryCreateSerializer, CategoryListSerializer
from x1Lubeshko.settings import REPLY_TEXTS


class CategoryCreate(generics.CreateAPIView):
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
    serializer_class = CategoryListSerializer

    def get_queryset(self):
        try:
            user = self.request.user
            queryset = Category.objects.filter(user=user)
        except:
            raise NotFound()
        return queryset
