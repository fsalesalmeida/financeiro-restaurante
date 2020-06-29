import axios from "./config";

export function getDespesasByCaixa(caixaId) {
    return axios.get(`despesas/${caixaId}`);
}

export function storeDespesas(data) {
    return axios.post("despesas", {
        cd_Caixa: data.idCaixa,
        cd_DespesaTipo: data.idTipo,
        vl_Despesa: data.despesa,
    });
}

export function getTipoDespesas() {
    return axios.get("despesas/tipos");
}

export function storeTipoDespesas(data) {
    return axios.post("despesas/tipos", {
        ds_DespesaTipo: data.tipoDespesa
    });
}