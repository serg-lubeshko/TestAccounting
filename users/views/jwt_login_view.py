from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import MyUser
from users.serializers.users_serializers import MyTokenObtainPairSerializer
from x1Lubeshko.settings import SIMPLE_JWT


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        data = serializer.validated_data
        obj = MyUser.objects.get(username=request.data['username'])
        data['username'] = obj.username
        data['id'] = obj.id
        res = Response(data=data, status=status.HTTP_200_OK)
        res = Response(data=data, status=status.HTTP_200_OK)
        res.set_cookie('refresh', data.get('refresh', None), max_age=SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'])
        res.set_cookie('access', data.get('access', None), max_age=SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'])
        res.set_cookie('username', data.get('username', None))
        res.set_cookie('id', data.get('id', None))
        return res

