from rest_framework import viewsets, generics
from .models import *
from .serializers import *


class ControleCaixaViewSet(viewsets.ModelViewSet):
    queryset = ControleCaixa.objects.all()
    serializer_class = ControleCaixaSerializer


class CaixaViewSet(viewsets.ModelViewSet):
    queryset = Caixa.objects.all()
    serializer_class = CaixaSerializer


class DespesaTipoViewSet(viewsets.ModelViewSet):
    queryset = DespesaTipo.objects.all()
    serializer_class = DespesaTipoSerializer


class DespesaViewSet(viewsets.ModelViewSet):
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer

         
class DespesaByCaixaList(generics.ListAPIView):
    serializer_class = DespesaSerializer

    def get_queryset(self):
        """
        This view should return a list of all models by
        the maker passed in the URL
        """
        caixa = self.kwargs['caixa_id']
        return Despesa.objects.all().filter(cd_Caixa=caixa)


class EntradaByCaixaList(generics.ListAPIView):
    serializer_class = EntradaSerializer

    def get_queryset(self):
        """
        This view should return a list of all models by
        the maker passed in the URL
        """
        caixa = self.kwargs['caixa_id']
        return Entrada.objects.all().filter(cd_Caixa=caixa)


class SangriaByCaixaList(generics.ListAPIView):
    serializer_class = SangriaSerializer

    def get_queryset(self):
        """
        This view should return a list of all models by
        the maker passed in the URL
        """
        caixa = self.kwargs['caixa_id']
        return Sangria.objects.all().filter(cd_Caixa=caixa)


class EntradaViewSet(viewsets.ModelViewSet):
    queryset = Entrada.objects.all()
    serializer_class = EntradaSerializer


class SangriaViewSet(viewsets.ModelViewSet):
    queryset = Sangria.objects.all()
    serializer_class = SangriaSerializer