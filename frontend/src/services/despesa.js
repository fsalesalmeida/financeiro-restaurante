import axios from "./config";

export function getDespesas() {
    return axios.get("despesas");
}

export function criarDespesas(data) {
    return axios.post("despesas", {
        cd_Caixa: data.idCaixa,
        cd_DespesaTipo: data.idTipo,
        vl_Despesa: data.vlDespesa,
    });
}

export function getTipoDespesas() {
    return axios.get("despesas/tipos");
}

export function criarTipoDespesas(data) {
    return axios.post("despesas/tipos", {
        ds_DespesaTipo: data.tipoDespesa
    });
}