from rest_framework import routers
from caixa.viewsets import *
from usuario.views import *
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'controle', ControleCaixaViewSet)
router.register(r'caixa', CaixaViewSet)
router.register(r'despesa/tipo', DespesaTipoViewSet)
router.register(r'despesa', DespesaViewSet)
router.register(r'entrada', EntradaViewSet)
router.register(r'sangria', SangriaViewSet)
router.register('users', UserViewSet, basename='user-list')
router.register('login', LoginView, basename='login')

urlpatterns = [
    path('', include(router.urls)),
    path('account/logout/', LogoutView.as_view(), name='logout')
]