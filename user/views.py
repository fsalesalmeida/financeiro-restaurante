from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from user.models import User
from user.serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken


@api_view(['POST', ])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "Usuário registrado com sucesso."
            data['email'] = user.email
            data['name'] = user.name
            token = Token.objects.get(user=User).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                       context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'cargo': user.CargoFuncionario.cd_CargoFuncionario
        })