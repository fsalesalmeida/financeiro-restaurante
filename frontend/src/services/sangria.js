import axios from "./config";

export function getSangriasByCaixa(caixaId) {
    return axios.get(`sangrias/${caixaId}`);
}

export function storeSangrias(data) {
    return axios.post("sangrias", {
        cd_Caixa: data.idCaixa,
        vl_Sangria: data.sangria,
    });
}