from django.urls import path

from users.views.views import UserCreate, UserList

urlpatterns = [
    path('create/', UserCreate.as_view()),
    path('list/', UserList.as_view())

]