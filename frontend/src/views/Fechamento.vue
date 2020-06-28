<template>
  <div class="content">
    <div class="container-fluid">
      <div class="card card-default">
        <div class="card-header">
          <h3 class="card-title">
            <i class="fas fa-wallet"></i>
            Fechar Caixa
          </h3>
        </div>
        <form>
            <div class="card-body">
                <div class="form-group">
                    <label for="dinheiro">Dinheiro em caixa</label>
                    <input type="number" id="dinheiro" class="form-control">
                </div>
                <div class="form-group">
                    <label for="credito">Cartão de crédito</label>
                    <input type="number" id="credito" class="form-control">
                </div>
                <div class="form-group">
                    <label for="debito">Cartão de débito</label>
                    <input type="number" id="debito" class="form-control">
                </div>
                <div class="form-group">
                    <label for="refeicao">Vale refeição</label>
                    <input type="number" id="refeicao" class="form-control">
                </div>
                <div class="form-group">
                    <label for="online">Valor online</label>
                    <input type="number" id="online" class="form-control">
                </div>
                <button class="btn btn-primary mt-3 float-right">Fechar Caixa</button>
            </div>
        </form>
      </div>
    </div>
  </div>
</template>
<style>
</style>
<script>
export default {
  name: "fechamento",
  data() {
    return {
      
    };
  },
  methods: {
    
  }
};
</script>
