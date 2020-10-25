from django.db import models
#from user.models import User
from django.conf import settings


class ControleCaixa(models.Model):
    cd_ControleCaixa = models.AutoField(primary_key=True, null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, on_delete=models.DO_NOTHING)
    dt_AberturaCaixa = models.DateTimeField(null=False, auto_now_add=True)
    dt_FechamentoCaixa = models.DateTimeField(null=False, auto_now_add=True)
    ds_TurnoCaixa = models.CharField(max_length=5, null=False, default=0)


class Caixa(models.Model):
    cd_Caixa = models.AutoField(primary_key=True, null=False)
    cd_ControleCaixa = models.OneToOneField(ControleCaixa, null=False, on_delete=models.DO_NOTHING)
    vl_CaixaInicial = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    vl_Dinheiro = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    vl_CartaoCredito = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    vl_CartaoDebito = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    vl_Refeicao = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    vl_ValeFuncionario = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    vl_Online = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    vl_Sangrias = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    vl_Despesas = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    vl_Entradas = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    vl_Faturamento = models.DecimalField(max_digits=12, decimal_places=2, default=0)


class DespesaTipo(models.Model):
    cd_DespesaTipo = models.AutoField(primary_key=True, null=False)
    ds_DespesaTipo = models.CharField(max_length=45, null=False)


class DespesaCaixa(models.Model):
    cd_Despesa = models.AutoField(primary_key=True, null=False)
    cd_Caixa = models.ForeignKey(Caixa, null=False, on_delete=models.DO_NOTHING)
    cd_DespesaTipo = models.ForeignKey(DespesaTipo, null=False, on_delete=models.DO_NOTHING)
    vl_Despesa = models.DecimalField(max_digits=12, decimal_places=2, default=0)


class Entrada(models.Model):
    cd_Entrada = models.AutoField(primary_key=True, null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, on_delete=models.DO_NOTHING)
    cd_Caixa = models.ForeignKey(Caixa, null=False, on_delete=models.DO_NOTHING)
    vl_Entrada = models.DecimalField(max_digits=12, decimal_places=2, default=0)


class Sangria(models.Model):
    cd_Sangria = models.AutoField(primary_key=True, null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, on_delete=models.DO_NOTHING)
    cd_Caixa = models.ForeignKey(Caixa, null=False, on_delete=models.DO_NOTHING)
    vl_Sangria = models.DecimalField(max_digits=12, decimal_places=2, default=0)


class ValesFuncionarios(models.Model):
    cd_ValeFuncionario = models.AutoField(primary_key=True, null=False)
    cd_Caixa = models.ForeignKey(Caixa, null=False, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, on_delete=models.DO_NOTHING)
    vl_ValeFuncionario = models.DecimalField(max_digits=12, decimal_places=2, default=0)
