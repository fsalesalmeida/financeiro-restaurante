import axios from "./config";

export function getCaixas() {
    return axios.get("caixas");
}

export function showCaixa(id) {
    return axios.get(`caixas/${id}`);
}

export function storeCaixa(data) {
    return axios.post("caixas", {
        vl_CaixaInicial: data.caixaInicial
    });
}

export function fecharCaixa(id, data) {
    return axios.patch(`caixas/${id}`, {
        vl_Dinheiro: data.dinheiro,
        vl_CartaoCredito: data.credito,
        vl_CartaoDebito: data.debito,
        vl_Refeicao: data.refeicao,
        vl_Online: data.online,
        vl_Sangrias: data.sangrias,
        vl_Despesas: data.despesas,
        vl_Entradas: data.entradas,
    });
}