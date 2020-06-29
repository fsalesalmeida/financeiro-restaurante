import axios from "./config";

export function getSangriasByCaixa(caixaId) {
  return axios.get(`sangria/caixa/${caixaId}`);
}

export function storeSangrias(data) {
  return axios.post("sangria/", {
    cd_Caixa: data.idCaixa,
    vl_Sangria: data.sangria
  });
}
