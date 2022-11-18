from django.urls import path

from users.views.views import UserCreate

urlpatterns = [
    path('create/', UserCreate.as_view()),

]