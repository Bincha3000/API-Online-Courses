from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.serializers import UserSerializer
from django.contrib.auth.models import User

class UserCreate(APIView):

    def post(self, request, format='json'):
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                if user:
                    return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




{
"username": "passsw",
"password": "123sdff",
"email": "bincha.1997@gmail.com",
"first_name": "vasya",
"last_name": "pridurok"
}