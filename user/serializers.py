from rest_framework import serializers

from user.models import User


class RegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(
        style={'input-type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'name', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = User(
            email=self.validated_data['email'],
            name=self.validated_data['name']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Senhas precisam ser iguais'})
        user.set_password(password)
        user.save()
        return user
