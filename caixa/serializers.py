from rest_framework import serializers
from .models import *

class ControleCaixaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControleCaixa
        fields = '__all__'


class CaixaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caixa
        fields = '__all__'


class DespesaTipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DespesaTipo
        fields = '__all__'


class DespesaCaixaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DespesaCaixa
        fields = '__all__'


class EntradaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrada
        fields = '__all__'


class SangriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sangria
        fields = '__all__'
