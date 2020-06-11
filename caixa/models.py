from django.db import models
from django.utils import timezone

# Create your models here.

class Caixa(models.Model):
    cd_Caixa = models.AutoField(primary_key=True, null=false)
    cd_ControleCaixa = models.ForeignKey(ControleCaixa, primary_key=True, null=false, on_delete=models.DO_NOTHING)
    vl_CaixaInicial = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    vl_Dinheiro = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    vl_CartaoCredito = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    vl_CartaoDebito = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    vl_Refeicao = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    vl_Online = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    vl_Sangrias = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    vl_Despesas = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    vl_Entradas= models.DecimalField(max_digits=12, decimal_places=2, default=0)

class ControleCaixa(models.Model):
    cd_ControleCaixa = models.AutoField(primary_key=True, null=false)
    dt_AberturaCaixa = models.DateTimeField(null=false, default=timezone.now)
    dt_FechamentoCaixa = models.DateTimeField(null=false, default=timezone.now)

class Despesas(models.Model):
    cd_Despesa = models.AutoField(primary_key=True, null=false)
    cd_Caixa = models.ForeignKey(Caixa, null=false, on_delete=models.DO_NOTHING)
    cd_DespesaTipo = models.ForeignKey(DespesaTipo, null=false, on_delete=models.DO_NOTHING)
    vl_Despesa = models.DecimalField(max_digits=12, decimal_places=2, default=0)

class DespesaTipo(models.Model):
    cd_DespesaTipo = models.AutoField(primary_key=True, null=false)
    ds_DespesaTipo = models.CharField(max_length=45, null=false)

class CaixaEntrada(models.Model):
    cd_Entrada = models.AutoField(primary_key=True, null=false)    
    cd_Caixa = models.ForeignKey(Caixa, null=false, on_delete=models.DO_NOTHING)    
    vl_Entrada = models.DecimalField(max_digits=12, decimal_places=2, default=0)

class CaixaSangria(models.Model):
    cd_Sangria = models.AutoField(primary_key=True, null=false)    
    cd_Caixa = models.ForeignKey(Caixa, null=false, on_delete=models.DO_NOTHING)    
    vl_Sangria = models.DecimalField(max_digits=12, decimal_places=2, default=0)