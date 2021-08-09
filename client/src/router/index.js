import Vue from 'vue';
import Router from 'vue-router';
import Ip from '../components/Ip.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Ip',
      component: Ip,
    },
  ],
});
