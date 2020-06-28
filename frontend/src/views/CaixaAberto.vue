<template>
  <div class="content">
    <div class="container-fluid">
      <div class="card card-default">
        <div class="card-header">
          <h3 class="card-title">
            <i class="fas fa-wallet"></i>
            Caixa Aberto - {{ caixaInicial }}
          </h3>
        </div>
        <div class="card-body">
          <div class="row">
            <div class="col-4">
              <div class="card">
                <div class="card-header">
                  <h3 class="card-title">Entrada</h3>
                </div>
                <div class="card-body">
                  <div class="form-group margin-form">
                    <input
                      v-model="entrada"
                      class="form-control"
                      type="number"
                      id="entrada"
                      name="entrada"
                      required
                    />
                  </div>
                  <button
                    @click="criarEntrada"
                    class="btn btn-primary margin-btn"
                  >
                    criar entrada
                  </button>
                </div>
              </div>
            </div>
            <div class="col-4">
              <div class="card">
                <div class="card-header">
                  <h3 class="card-title">Despesa</h3>
                </div>
                <div class="card-body">
                  <div class="input-group mb-3">
                    <div class="input-group-prepend">
                      <label class="input-group-text" for="tipoDespesa"
                        >Tipo</label
                      >
                    </div>
                    <select
                      v-model="tipoDespesa"
                      class="custom-select"
                      id="tipoDespesa"
                      required
                    >
                      <option
                        v-for="tipo in selectTipo"
                        :key="tipo.value"
                        :value="tipo.value"
                      >
                        {{ tipo.text }}
                      </option>
                    </select>
                  </div>
                  <div class="form-group">
                    <input
                      v-model="despesa"
                      class="form-control"
                      type="number"
                      id="despesa"
                      name="despesa"
                      required
                    />
                  </div>
                  <button @click="criarDespesa" class="btn btn-primary">
                    criar despesa
                  </button>
                </div>
              </div>
            </div>
            <div class="col-4">
              <div class="card">
                <div class="card-header">
                  <h3 class="card-title">Sangria</h3>
                </div>
                <div class="card-body">
                  <div class="form-group margin-form">
                    <input
                      v-model="sangria"
                      class="form-control"
                      type="number"
                      id="sangria"
                      name="sangria"
                      required
                    />
                  </div>
                  <button
                    @click="criarSangria"
                    class="btn btn-primary margin-btn"
                  >
                    criar sangria
                  </button>
                </div>
              </div>
            </div>
          </div>
          <button class="btn btn-success btn-block mt-3" type="button" @click="fecharCaixa">
            Preparar Fechamento
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
<style>
.margin-form {
  margin-top: 30px;
}

.margin-btn {
  margin-top: 23px;
}
</style>
<script>
export default {
  name: "caixa-aberto",
  data() {
    return {
      caixaInicial: "200,00",
      entrada: 0,
      despesa: 0,
      sangria: 0,
      tipoDespesa: null,
      caixa_id: '',
      selectTipo: [
        { text: "Escolha...", value: null },
        { text: "Fornecedor", value: 1 },
        { text: "Petit Cash", value: 2 },
        { text: "Pagamento c/ Pessoal", value: 3 }
      ]
    };
  },
  methods: {
    criarEntrada() {
      // POST "Criar uma entrada associando ao ID do Caixa"
    },
    criarDespesa() {
      // POST "Criar uma despesa associando ao ID do Caixa"
    },
    criarSangria() {
      // POST "Criar uma sangria associando ao ID do Caixa"
    },
    fetchDespesaTipo() {
      // GET "Lista todos os tipos de despesa"
    },
    fecharCaixa() {
      this.$swal({
        title: "Fechar caixa",
        text: "Você tem certeza do fechamento do caixa?",
        icon: "warning",
        showCancelButton: true,
        confirmButtonText: "Sim",
        cancelButtonText: "Não",
      }).then(result => {
        if (result.value) {
          this.$router.push({ name: "Fechamento", params: { caixaId: this.caixa_id } });
        }
      });
    }
  }
};
</script>
