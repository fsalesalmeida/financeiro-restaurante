<template>
  <div class="content">
    <div class="container-fluid">
      <div class="card card-default">
        <div class="card-header">
          <h3 class="card-title">
            <i class="fas fa-wallet"></i> Caixa Aberto - {{ caixaInicial }}
          </h3>
        </div>
        <div class="card-body">
          <form id="caixa_aberto">
            <div class="form-group">
              <label for="entrada">Entrada:</label>
              <input v-model="entrada" class="form-control" type="number" id="entrada" name="entrada" />
            </div>
            <div class="form-group">
              <label for="despesa">Despesas:</label>
              <input v-model="despesa" class="form-control" type="number" id="despesa" name="despesa" />
            </div>
            <div class="form-group">
              <label for="sangria">Sangria:</label>
              <input v-model="sangria" class="form-control" type="number" id="sangria" name="sangria" />
            </div>
            <button class="btn btn-success btn-sm float-right" type="button">Fechar caixa</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "caixa-aberto",
  data() {
    return {
      caixaInicial: "200,00", 
      entrada: 0,
      despesa: 0,
      sangria: 0,
    };
  }
};
</script>
