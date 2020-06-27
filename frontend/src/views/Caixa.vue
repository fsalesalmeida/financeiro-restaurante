<template>
  <div class="content">
    <div class="container-fluid">
      <div class="container">
        <div class="row justify-content-center align-items-center">
          <div class="col-xs-3 card">
            <div class="card-header">
              <h3 class="card-title">
                <i class="fas fa-wallet"></i> Caixa Inicial
              </h3>
            </div>
            <div class="card-body p-4">
              <form id="caixa_inicial">
                <div class="form-group">
                  <label for="texto">Insira o valor:</label>
                  <input
                    v-model="inputText"
                    class="form-control"
                    type="number"
                    id="texto"
                    name="texto"
                  />
                </div>
                <button
                  class="btn btn-success btn-sm"
                  @click="abrirCaixa"
                  type="button"
                >
                  Abrir caixa
                </button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "Caixa",
  data() {
    return {
      inputText: ""
    };
  },
  methods: {
    abrirCaixa() {
      this.$swal({
        title: "Abertura do caixa",
        text: "Você tem certeza da abertura do caixa?",
        icon: "warning",
        showCancelButton: true,
        confirmButtonText: "Sim",
        cancelButtonText: "Não"
      }).then(result => {
        if (result.value) {
          this.$router.push({ name: "Caixa Aberto" });
        }
      });
    }
  }
};
</script>
