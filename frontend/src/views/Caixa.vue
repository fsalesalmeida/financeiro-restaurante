<template>
  <div class="content">
    <div class="container-fluid">
      <div class="container">
        <div class="row">
          <div class="col-xs-3 card w-100">
            <div class="card-header tex-center">
              <h3 class="card-title">
                <i class="fas fa-wallet"></i> Caixa Inicial
              </h3>
            </div>
            <div
              class="card-body p-4 text-center d-flex justify-content-center align-items-center"
            >
              <form @submit.prevent="abrirCaixa" id="caixa_inicial">
                <div class="form-group">
                  <label for="texto">Insira o valor</label>
                  <input
                    v-model="caixaInicial"
                    required
                    class="form-control tamanho-input"
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
        <div class="row">
          <div class="w-100 card">
            <div class="card-header">
              <h3 class="card-title">
                <i class="fas fa-wallet"></i> Caixas Cadastrados
              </h3>
            </div>
            <div class="card-body p-4 row">
              <div v-for="caixa in caixas" :key="caixa.cd_Caixa" class="col-4">
                <div class="card m-3">
                  <div class="card-header bg-light">
                    <h3 class="card-title">Caixa #{{ caixa.cd_Caixa }}</h3>
                  </div>
                  <div class="card-body text-center">
                    <p class="card-text">
                      Faturamento: R$ {{ caixa.vl_Faturamento }}
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped>
.tamanho-input {
  width: 250px;
}
</style>
<script>
import { getCaixas, storeCaixa, storeControleCaixa } from "@/services/caixa";

export default {
  name: "Caixa",
  data() {
    return {
      caixaInicial: "",
      errors: [],
      caixas: []
    };
  },
  methods: {
    fetchCaixaData() {
      getCaixas()
        .then(res => {
          console.log(res.data);
          this.caixas = res.data;
        })
        .catch(err => this.errors.push(err.response));
    },
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
  },
  mounted() {
    this.fetchCaixaData();
  }
};
</script>
