from django.core.mail import send_mail

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from users.serializers import UserSerializer


def registration_email(first_name, last_name, email):
    subject = "Successful registration"
    message =   """
                Dear {first_name} {last_name}!
                Congratulations on your successful registration!
                """.format(first_name=first_name,
                            last_name=last_name)
    send_mail(
        subject=subject,
        message=message,
        from_email="bincha.1997@gmail.com",
        recipient_list=[email,],
        fail_silently=False)

    return True

class UserCreateView(APIView):

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            first_name = user.first_name
            last_name = user.last_name
            email = user.email
            user = serializer.save()
            if user and registration_email(first_name, last_name, email):
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserLogInView(ObtainAuthToken):

    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)

class UserLogOutView(APIView):

    permission_classes = (permissions.IsAuthenticated)

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
