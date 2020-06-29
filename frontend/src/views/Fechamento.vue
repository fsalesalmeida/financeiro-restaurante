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
        <form @submit.prevent="fechamento">
            <div class="card-body">
                <div class="form-group">
                    <label for="dinheiro">Dinheiro em caixa</label>
                    <input type="number" required v-model="dinheiro" id="dinheiro" class="form-control">
                </div>
                <div class="form-group">
                    <label for="credito">Cartão de crédito</label>
                    <input type="number" required v-model="credito" id="credito" class="form-control">
                </div>
                <div class="form-group">
                    <label for="debito">Cartão de débito</label>
                    <input type="number" required v-model="debito" id="debito" class="form-control">
                </div>
                <div class="form-group">
                    <label for="refeicao">Vale refeição</label>
                    <input type="number" required v-model="refeicao" id="refeicao" class="form-control">
                </div>
                <div class="form-group">
                    <label for="online">Valor online</label>
                    <input type="number" required v-model="online" id="online" class="form-control">
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
      dinheiro: 0,
      credito: 0,
      debito: 0,
      refeicao: 0,
      online: 0,
      sangrias: [],
      entradas: [],
      despesas: [],
    };
  },
  /* props: {
    caixaId: {
      type: Number,
      required: true
    }
  }, */
  methods: {
    fechamento() {
      this.$swal({
        title: "Fechamento",
        text: "Você tem certeza do fechamento do caixa?",
        icon: "warning",
        showCancelButton: true,
        confirmButtonText: "Sim",
        cancelButtonText: "Não"
      }).then(result => {
        if (result.value) {
          //POST 'Fecha o caixa e faz as contas gerando o faturamento, retorna o faturamento'
        }
      });
    },
    fetchSangrias() {
      // GET 'Lista todas as sangrias pelo id do caixa'
    },
    fetchEntradas() {
      // GET 'Lista todas as entradas pelo id do caixa'
    },
    fetchDespesas() {
      // GET 'Lista todas as despesas pelo id do caixa'
    }
  }
};
</script>
