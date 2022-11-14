from django.urls import path

from accounting.views import CategoryCreate

urlpatterns = [
    path('category/create/', CategoryCreate.as_view()),

]
