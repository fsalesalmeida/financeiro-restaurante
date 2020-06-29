from rest_framework import routers
from caixa.viewsets import *

router = routers.DefaultRouter()
router.register(r'controle', ControleCaixaViewSet)
router.register(r'caixa', CaixaViewSet)
router.register(r'despesa/tipo', DespesaTipoViewSet)
router.register(r'despesa', DespesaViewSet)
router.register(r'entrada', EntradaViewSet)
router.register(r'sangria', SangriaViewSet)