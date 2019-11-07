<template>
  <div>
    <v-app>

      <v-app-bar
        color="#fafafa"
        app
        class="top-bar"
        elevation="2"
      >
        <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
        <v-toolbar-title>
          <img v-bind:class="{inactive: drawer}" class="nameplate" src="./assets/nameplate.png" >
        </v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn icon>
          <v-icon>mdi-magnify</v-icon>
        </v-btn>
      </v-app-bar>

      <v-navigation-drawer  v-model="drawer" app height="100%" dark color="#424242" class="z-index-0">
        <img class="logo" src="./assets/logo2.png">
        <hr>
        <v-container mt-10 class="catalog-title catalog-text-color">
          <p>Catalog</p>
        </v-container>
        <v-container ml-4 class="catalog-text-color">
          <p v-for="n in categoriesList">{{n.category}}</p>
        </v-container>
      </v-navigation-drawer>

      <v-container class="z-index-0">
        <router-view></router-view>
      </v-container>

      <v-footer app>
      </v-footer>

    </v-app>
  </div>
</template>


<script>
export default {
    name: 'app',
    data () {
        return {
            drawer: true
        }
   },
    mounted() {
            this.$store.dispatch('GET_GOODS');
            this.$store.dispatch('GET_CATEGORIES');
    },
    computed: {
        goodsList() {
            return this.$store.getters.GOODS;
        },
        categoriesList() {
            return this.$store.getters.CATEGORIES;
        },
    }
}
</script>

<style scoped>
  .catalog-title {
    font-size: 30px;
    font-weight: 100;
    font-family: "Microsoft Sans Serif", sans-serif;
  }
  .catalog-text-color {
    color: #FAFAFA;
  }
  .logo {
    height:200px;
    padding-left: 30px;
  }

   .nameplate {
     width: 180px;
     padding-top: 10px;
   }

  .top-bar {
    position: fixed;
  }

  .inactive {
    display: none;
  }

</style>
