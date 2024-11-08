from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from datetime import datetime


@api_view(['POST'])
def custom_login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(request, username=username, password=password)

    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "user": {
                "username": user.username,
                "email": user.email,
            },
            "token": token.key
        })
    else:
        return Response({"error": "Invalid credentials"}, status=400)

@api_view(['POST'])
def logout_route(request):
    response = Response()
    response.set_cookie(
        key=JWT_AUTH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    response.set_cookie(
        key=JWT_AUTH_REFRESH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    return response


@api_view()
def root_route(request):
    return Response({
        "message": "Welcome to my drf API!"
    })


class YourDataView(APIView):
    def get(self, request):
        data = {
            "id": 1,
            "name": "Sample Item",
            "created": datetime.now(),
            "updated": datetime.now()
        }
        return Response(data)