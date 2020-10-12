from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


from user.serializers import RegistrationSerializer

@api_view(['POST',])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=resquest.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "Usuário registrado com sucesso."
            data['email'] = user.email
            data['name'] = user.name
        else:
            data = serializer.errors
        return Response(data)
# Create your views here.
