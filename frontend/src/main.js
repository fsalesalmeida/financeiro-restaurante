import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import VueSweetalert2 from "vue-sweetalert2";

import "sweetalert2/dist/sweetalert2.min.css";

const options = {
  confirmButtonColor: "#003257",
  cancelButtonColor: "#008230"
};

Vue.use(VueSweetalert2, options);

Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App)
}).$mount("#app");
