import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex);

const backend_url = axios.create({
  baseURL: 'http://127.0.0.1:8000/',
  timeout: 1000,
});

export default new Vuex.Store ({
  state: {
    goods: null,
  },
  getters: {
    GOODS: state => {
      return state.goods;
    },
  },
  mutations:{
    SET_GOODS: (state, payload) => {
      state.goods = payload;
    },
  },
  actions: {
    GET_GOODS: async (context, payload) => {
      await backend_url.get('/goods/')
                              .then((response) => {
                                context.commit('SET_GOODS', response.data);
                              });
    },
  },
})
