import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import Admin from '@/components/Admin'
import Home from '@/components/Home'
import Cart from '@/components/Cart'

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '',
      name: 'home',
      component: Home
    },
    {
     path: '/admin',
     name: 'admin',
     component: Admin,
      beforeEnter: (to, from, next) => {
        if (!sessionStorage.adminToken) {
          next('/login');
          alert("You must authorize to enter this page.");
        }
        else next()
      }
    },
    {
      path: '/login',
      name: 'login',
      component:  Login
    },
    {
      path: '/cart',
      name: 'cart',
      component:  Cart
    },
  ],
  mode: 'history'
})
