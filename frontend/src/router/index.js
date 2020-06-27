import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Início",
    component: () => import(/* webpackChunkName: "about" */ "../views/Home.vue")
  },
  {
    path: "/caixa",
    name: "Caixa",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Caixa.vue")
  },
  {
    path: "/caixa-aberto",
    name: "Caixa Aberto",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/CaixaAberto.vue")
  },
  {
    path: "/caixa-fechar/:caixaId",
    name: "Fechar Caixa",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/CaixaFechar.vue")
  },
  
];

const router = new VueRouter({
  mode: "history",
  base: "",
  routes
});

export default router;
