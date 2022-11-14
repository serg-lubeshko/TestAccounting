from django.urls import path

from users.views import UserCreate

urlpatterns = [
    path('create/', UserCreate.as_view()),
    # path('update/<int:user_id>', UserUpdate.as_view()),

]