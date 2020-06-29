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
              <input
                type="number"
                required
                v-model="dinheiro"
                id="dinheiro"
                class="form-control"
              />
            </div>
            <div class="form-group">
              <label for="credito">Cartão de crédito</label>
              <input
                type="number"
                required
                v-model="credito"
                id="credito"
                class="form-control"
              />
            </div>
            <div class="form-group">
              <label for="debito">Cartão de débito</label>
              <input
                type="number"
                required
                v-model="debito"
                id="debito"
                class="form-control"
              />
            </div>
            <div class="form-group">
              <label for="refeicao">Vale refeição</label>
              <input
                type="number"
                required
                v-model="refeicao"
                id="refeicao"
                class="form-control"
              />
            </div>
            <div class="form-group">
              <label for="online">Valor online</label>
              <input
                type="number"
                required
                v-model="online"
                id="online"
                class="form-control"
              />
            </div>
            <button class="btn btn-primary mt-3 float-right">
              Fechar Caixa
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
<style></style>
<script>
import { showCaixa, fecharCaixa } from "@/services/caixa";
import { getDespesasByCaixa } from "@/services/despesa";
import { getSangriasByCaixa } from "@/services/sangria";
import { getEntradasByCaixa } from "@/services/entrada";

export default {
  name: "fechamento",
  data() {
    return {
      caixa: {},
      dinheiro: 0,
      credito: 0,
      debito: 0,
      refeicao: 0,
      online: 0,
      sangrias: [],
      sangriaTotal: 0,
      entradas: [],
      entradaTotal: 0,
      despesas: [],
      despesaTotal: 0,
      errors: []
    };
  },
  computed: {
    faturamento() {
      this.entradas.reduce((acc, value) => this.entradaTotal += value.vl_Entrada);
      this.despesas.reduce((acc, value) => this.despesaTotal += value.vl_Despesa);
      this.sangrias.reduce((acc, value) => this.sangriaTotal += value.vl_Sangria);

      return parseFloat(this.dinheiro) + parseFloat(this.credito) + parseFloat(this.debito) + parseFloat(this.refeicao) + parseFloat(this.online) +
        parseFloat(this.sangriaTotal) + parseFloat(this.despesaTotal) - parseFloat(this.caixa.vl_CaixaInicial) - parseFloat(this.entradaTotal);
    }
  },
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
          console.log(this.faturamento);
          fecharCaixa(this.$route.params.caixaId, {
            dinheiro: this.dinheiro,
            credito: this.credito,
            debito: this.debito,
            refeicao: this.refeicao,
            online: this.online,
            sangrias: this.sangriaTotal,
            despesas: this.despesaTotal,
            entradas: this.entradaTotal,
            faturamento: this.faturamento
          })
          .then(res => console.log(res.data))
          .catch(err => this.errors.push(err.response))
        }
      });
    },
    fetchSangrias() {
      // GET 'Lista todas as sangrias pelo id do caixa'
      getSangriasByCaixa(this.$route.params.caixaId)
        .then(res => this.sangrias = res.data)
        .catch(err => this.errors.push(err.response));
    },
    fetchEntradas() {
      // GET 'Lista todas as entradas pelo id do caixa'
      getEntradasByCaixa(this.$route.params.caixaId)
        .then(res => this.entradas = res.data)
        .catch(err => this.errors.push(err.response));
    },
    fetchDespesas() {
      // GET 'Lista todas as despesas pelo id do caixa'
      getDespesasByCaixa(this.$route.params.caixaId)
        .then(res => this.despesas = res.data)
        .catch(err => this.errors.push(err.response));
    },
    fetchCaixa() {
      // GET 'Exibe o caixa pelo seu id'
      showCaixa(this.$route.params.caixaId)
        .then(res => (this.caixa = res.data))
        .catch(err => this.error.push(err.response));
    },
  },

  mounted() {
    this.fetchCaixa();
    this.fetchSangrias();
    this.fetchEntradas();
    this.fetchDespesas();
  }
};
</script>
