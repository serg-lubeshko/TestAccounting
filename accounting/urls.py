from django.urls import path

from accounting.views import CategoryCreate, CategoryList

urlpatterns = [
    path('category/create/', CategoryCreate.as_view()),
    path('category/list/', CategoryList.as_view()),

]
