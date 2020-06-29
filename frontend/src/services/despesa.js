import axios from "./config";

export function getDespesasByCaixa(caixaId) {
    return axios.get(`despesa/${caixaId}`);
}

export function storeDespesas(data) {
    return axios.post("despesa", {
        cd_Caixa: data.idCaixa,
        cd_DespesaTipo: data.idTipo,
        vl_Despesa: data.despesa,
    });
}

export function getTipoDespesas() {
    return axios.get("despesa/tipo");
}

export function storeTipoDespesas(data) {
    return axios.post("despesa/tipo", {
        ds_DespesaTipo: data.tipoDespesa
    });
}