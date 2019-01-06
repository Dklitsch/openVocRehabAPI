from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response


@api_view(http_method_names=['POST'])
def login(request):
    user = authenticate(username=request.data.get("username"), password=request.data.get("password"))
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key
        }, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
