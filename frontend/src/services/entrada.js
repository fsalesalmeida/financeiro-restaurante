import axios from "./config";

export function getEntradasByCaixa(caixaId) {
    return axios.get(`entradas/${caixaId}`);
}

export function storeEntradas(data) {
    return axios.post("entradas", {
        cd_Caixa: data.idCaixa,
        vl_Entrada: data.entrada,
    });
}