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
              <form @submit.prevent="abrirCaixa" id="caixa_inicial">
                <div class="form-group">
                  <label for="texto">Insira o valor:</label>
                  <input
                    v-model="caixaInicial"
                    required
                    class="form-control"
                    type="number"
                    id="texto"
                    name="texto"
                  />
                </div>
                <button class="btn btn-success btn-sm" type="submit">
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
import { storeCaixa, storeControleCaixa } from "@/services/caixa";

export default {
  name: "Caixa",
  data() {
    return {
      caixaInicial: "",
      errors: []
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
          //POST 'Criar um CaixaControle e consequentemente um Caixa, retorna o ID do caixa'
          storeControleCaixa()
            .then(res => {
              this.controleCaixa = res.data.cd_ControleCaixa;
              const data = {
                cd_ControleCaixa: res.data.cd_ControleCaixa,
                vl_CaixaInicial: this.caixaInicial
              };
              storeCaixa(data)
                .then(res => {
                  this.caixa = res.data;
                  this.$router.push({
                    name: "Caixa Aberto",
                    params: { caixaId: res.data.cd_Caixa }
                  });
                })
                .catch(err => this.errors.push(err.response));
            })
            .catch(err => this.errors.push(err.response));
        }
      });
    }
  }
};
</script>
