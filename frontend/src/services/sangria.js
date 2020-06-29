import axios from "./config";

export function getSangriasByCaixa(caixaId) {
    return axios.get(`sangria/${caixaId}`);
}

export function storeSangrias(data) {
    return axios.post("sangria", {
        cd_Caixa: data.idCaixa,
        vl_Sangria: data.sangria,
    });
}