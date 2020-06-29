import axios from 'axios';

axios.defaults.xsrfHeaderName = "X-CSRFToken"
axios.defaults.xsrfCookieName = 'csrftoken'

const Axios = axios.create({
    baseURL: "http://localhost:8000/api/"
});

export default Axios;