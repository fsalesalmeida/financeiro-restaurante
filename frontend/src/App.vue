<template>
  <div class="wrapper">
    <nav-bar></nav-bar>
    <side-bar></side-bar>
    <div class="content-wrapper">
      <content-header
        v-if="$route.name != 'Início'"
        :pagina-atual="$route.name"
      ></content-header>
      <router-view />
    </div>
    <footer class="main-footer">
      <strong
        >Copyright &copy; 2020 - Controle Financeiro para Restaurante.</strong
      >
    </footer>
  </div>
</template>

<script>
import ContentHeader from "@/components/ContentHeader.vue";
import SideBar from "@/components/SideBar.vue";
import NavBar from "@/components/NavBar.vue";

export default {
  components: {
    ContentHeader,
    SideBar,
    NavBar
  }
};
</script>
