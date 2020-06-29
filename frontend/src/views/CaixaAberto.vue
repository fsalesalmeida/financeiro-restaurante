<template>
  <div class="content">
    <div class="container-fluid">
      <div class="card card-default">
        <div class="card-header">
          <h3 class="card-title">
            <i class="fas fa-wallet"></i>
            Caixa Aberto
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
                  <form @submit.prevent="criarEntrada">
                    <div class="form-group margin-form">
                      <input
                        ref="entrada"
                        v-model="entrada"
                        class="form-control"
                        type="number"
                        id="entrada"
                        name="entrada"
                        required
                      />
                      <span class="error invalid-feedback">{{ msg.error1 }}</span>
                    </div>
                    <button class="btn btn-primary margin-btn">criar entrada</button>
                  </form>
                </div>
              </div>
            </div>
            <div class="col-4">
              <div class="card">
                <div class="card-header">
                  <h3 class="card-title">Despesa</h3>
                </div>
                <div class="card-body">
                  <form @submit.prevent="criarDespesa">
                    <div class="input-group mb-3">
                      <div class="input-group-prepend">
                        <label class="input-group-text" for="tipoDespesa">Tipo</label>
                      </div>
                      <select
                        ref="tipo"
                        v-model="tipoDespesa"
                        class="custom-select"
                        id="tipoDespesa"
                        required
                      >
                        <option
                          v-for="tipo in tipoDespesas"
                          :key="tipo.cd_DespesaTipo"
                          :value="tipo.cd_DespesaTipo"
                        >{{ tipo.ds_DespesaTipo }}</option>
                      </select>
                      <span class="error invalid-feedback">{{ msg.error2 }}</span>
                    </div>
                    <div class="form-group">
                      <input
                        ref="despesa"
                        v-model="despesa"
                        class="form-control"
                        type="number"
                        id="despesa"
                        name="despesa"
                        required
                      />
                      <span class="error invalid-feedback">{{ msg.error3 }}</span>
                    </div>
                    <button class="btn btn-primary">criar despesa</button>
                  </form>
                </div>
              </div>
            </div>
            <div class="col-4">
              <div class="card">
                <div class="card-header">
                  <h3 class="card-title">Sangria</h3>
                </div>
                <div class="card-body">
                  <form @submit.prevent="criarSangria">
                    <div class="form-group margin-form">
                      <input
                        ref="sangria"
                        v-model="sangria"
                        class="form-control"
                        type="number"
                        id="sangria"
                        name="sangria"
                        required
                      />
                      <span class="error invalid-feedback">{{ msg.error4 }}</span>
                    </div>
                    <button class="btn btn-primary margin-btn">criar sangria</button>
                  </form>
                </div>
              </div>
            </div>
          </div>
          <button
            class="btn btn-success btn-block mt-3"
            type="button"
            @click="fecharCaixa"
          >Preparar Fechamento</button>
        </div>
      </div>
    </div>
    <div v-if="toast" id="toastsContainerTopRight" class="toasts-top-right fixed">
      <div class="toast bg-success fade show" role="alert" aria-live="assertive" aria-atomic="true">
        <div class="toast-header">
          <strong class="mr-auto">Sucesso</strong>
          <button data-dismiss="toast" type="button" class="ml-2 mb-1 close" aria-label="Close">
            <span aria-hidden="true" @click="toast = false">×</span>
          </button>
        </div>
        <div class="toast-body">{{ msgToast }}</div>
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
import { showCaixa } from "@/services/caixa";
import { getTipoDespesas, storeDespesas } from "@/services/despesa";
import { storeSangrias } from "@/services/sangria";
import { storeEntradas } from "@/services/entrada";

export default {
  name: "caixa-aberto",
  data() {
    return {
      caixa: {},
      toast: false,
      msgToast: "",
      msg: {
        error1: "",
        error2: "",
        error3: "",
        error4: ""
      },
      entrada: 0,
      despesa: 0,
      sangria: 0,
      tipoDespesas: [],
      tipoDespesa: 0,
      error: []
    };
  },
  methods: {
    afterSend(tipo, valor) {
      this.msgToast = `A ${tipo} de R$${valor} foi criada com sucesso.`;
      this.toast = true;
      this.entrada = 0;
      this.despesa = 0;
      this.sangria = 0;
      this.tipoDespesa = 0;
    },
    criarEntrada() {
      // POST "Criar uma entrada associando ao ID do Caixa"
      if (this.entrada === 0 || this.entrada === "") {
        this.$refs.entrada.classList.add("is-invalid");
        this.msg.error1 =
          "O campo entrada precisa ser um número positivo maior que 0";
        return;
      }
      this.$refs.entrada.classList.remove("is-invalid");
      storeEntradas({
        idCaixa: this.$route.params.caixaId,
        entrada: this.entrada
      })
        .then(res => {
          console.log(res.data);
          this.afterSend("entrada", res.data.vl_Entrada);
        })
        .catch(err => this.error.push(err.response));
    },
    criarDespesa() {
      // POST "Criar uma despesa associando ao ID do Caixa"
      if (this.despesa === 0 || this.despesa === "" || this.tipoDespesa === 0) {
        if (this.despesa === 0 || this.despesa === "") {
          this.$refs.despesa.classList.add("is-invalid");
          this.msg.error3 =
            "O campo despesa precisa ser um número positivo maior que 0";
        }
        if (this.tipoDespesa === 0) {
          this.$refs.tipo.classList.add("is-invalid");
          this.msg.error2 = "O campo tipo precisa ser selecionado";
        }
        return;
      }
      this.$refs.despesa.classList.remove("is-invalid");
      this.$refs.tipo.classList.remove("is-invalid");
      storeDespesas({
        idCaixa: this.$route.params.caixaId,
        idTipo: this.tipoDespesa,
        despesa: this.despesa
      })
        .then(res => {
          console.log(res.data);
          this.afterSend("despesa", res.data.vl_Despesa);
        })
        .catch(err => this.error.push(err.response));
    },
    criarSangria() {
      // POST "Criar uma sangria associando ao ID do Caixa"
      if (this.sangria === 0 || this.sangria === "") {
        this.$refs.sangria.classList.add("is-invalid");
        this.msg.error4 =
          "O campo sangria precisa ser um número positivo maior que 0";
        return;
      }
      this.$refs.sangria.classList.remove("is-invalid");
      storeSangrias({
        idCaixa: this.$route.params.caixaId,
        sangria: this.sangria
      })
        .then(res => {
          console.log(res.data);
          this.afterSend("sangria", res.data.vl_Sangria);
        })
        .catch(err => this.error.push(err.response));
    },
    fetchDespesaTipo() {
      // GET "Lista todos os tipos de despesa"
      getTipoDespesas()
        .then(res => (this.tipoDespesas = res.data))
        .catch(err => this.error.push(err.response));
    },
    fetchCaixa() {
      // GET 'Exibe o caixa pelo seu id'
      showCaixa(this.$route.params.caixaId)
        .then(res => (this.caixa = res.data))
        .catch(err => this.error.push(err.response));
    },
    fecharCaixa() {
      this.$swal({
        title: "Fechar caixa",
        text: "Você tem certeza que quer ir para o fechamento?",
        icon: "warning",
        showCancelButton: true,
        confirmButtonText: "Sim",
        cancelButtonText: "Não"
      }).then(result => {
        if (result.value) {
          this.$router.push({
            name: "Fechamento",
            params: { caixaId: this.$route.params.caixaId }
          });
        }
      });
    }
  },

  mounted() {
    this.fetchCaixa();
    this.fetchDespesaTipo();
  }
};
</script>
