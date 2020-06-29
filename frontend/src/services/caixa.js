import axios from "./config";

export function getCaixas() {
    return axios.get("caixa");
}

export function showCaixa(id) {
    return axios.get(`caixa/${id}`);
}

export function getControleCaixas() {
    return axios.get("controle/");
}

export function showControleCaixa(id) {
    return axios.get(`controle/${id}`);
}

export function storeControleCaixa() {
    return axios.post("controle/");
}

export function storeCaixa(data) {
    return axios.post("caixa/", {
        cd_ControleCaixa: data.cd_ControleCaixa,
        vl_CaixaInicial: data.vl_CaixaInicial,
    });
}

export function fecharCaixa(id, data) {
    return axios.patch(`caixa/${id}/`, {
        vl_Dinheiro: data.dinheiro,
        vl_CartaoCredito: data.credito,
        vl_CartaoDebito: data.debito,
        vl_Refeicao: data.refeicao,
        vl_Online: data.online,
        vl_Sangrias: data.sangrias,
        vl_Despesas: data.despesas,
        vl_Entradas: data.entradas,
        vl_Faturamento: data.faturamento,
    });
}