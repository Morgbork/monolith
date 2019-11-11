import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '../router'

Vue.use(Vuex);

const backend_url = axios.create({
  baseURL: 'http://127.0.0.1:8000/',
  timeout: 1000,
});

export default new Vuex.Store ({
  state: {
    goods: null,
    categories: null,

  },
  getters: {
    GOODS: state => {
      return state.goods;
    },
    CATEGORIES: state => {
      return state.categories;
    },
  },
  mutations:{
    SET_GOODS: (state, payload) => {
      state.goods = payload;
    },
    SET_CATEGORIES: (state, payload) => {
      state.categories = payload;
    }
  },
  actions: {
    GET_GOODS: async (context, payload) => {
      await backend_url.get('/goods/', {params: payload})
                              .then((response) => {
                                context.commit('SET_GOODS', response.data);
                              });
    },
    GET_CATEGORIES: async (context, payload) => {
      await backend_url.get('/categories/')
        .then((response) => {
          context.commit('SET_CATEGORIES', response.data);
        });
    },
    ADMIN_AUTH: async (context, payload) => {
      await  backend_url.post('/rest-auth/login/', {username: payload.login, email: '', password: payload.password})
        .then((response) => {
            if (response.status===200)
              {sessionStorage.adminToken = response.data.key; router.push("admin")}},
          (reject) => {alert("Incorrect username or password")}

        );
    },
    ADD_PRODUCT: async (context, payload) => {
      await backend_url.post('/goods/', payload)
        .then((response) => {alert(response.status)})
    },
    UPDATE_PRODUCT: async (context, payload) => {
      await backend_url.patch('/goods/'+payload.id+'/', payload.payload)
        .then((response) => {alert(response.status)})
    }
  },
})
