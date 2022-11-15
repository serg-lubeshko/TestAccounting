from django.urls import path

from accounting.views import CategoryCreate, CategoryList, CategoryDetail

urlpatterns = [
    path('category/create/', CategoryCreate.as_view()),
    path('category/list/', CategoryList.as_view()),
    path('category/detail/<int:category_id>', CategoryDetail.as_view()),

]
