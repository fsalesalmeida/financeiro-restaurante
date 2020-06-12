import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Inicio",
    component: Home
  },
  {
    path: "/caixa",
    name: "Caixa",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Caixa.vue")
  }
];

const router = new VueRouter({
  mode: "history",
  base: '',
  routes
});

export default router;
