import axios from "./config";

export function getEntradasByCaixa(caixaId) {
  return axios.get(`entrada/caixa/${caixaId}`);
}

export function storeEntradas(data) {
  return axios.post("entrada/", {
    cd_Caixa: data.idCaixa,
    vl_Entrada: data.entrada
  });
}
