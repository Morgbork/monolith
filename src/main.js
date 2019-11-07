import Vue from 'vue'
import App from './App'
import router from './router'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import store from './store'
import Vuelidate from 'vuelidate'


Vue.use(Vuelidate);
Vue.use(Vuetify);
const vuetifyOptions = { };

Vue.config.productionTip = false;

new Vue({
  el: '#app',
  store,
  router,
  vuetify: new Vuetify(vuetifyOptions),
  components: { App },
  template: '<App/>'
});
