/* eslint-disable */
import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import Axios from 'axios'
import VueCookies from 'vue-cookies'

Vue.use(VueCookies)
Vue.config.productionTip = false

const eventsHub = new Vue()

Vue.prototype.$http = Axios;
const token = localStorage.getItem('token')
if (token) {
  Vue.prototype.$http.defaults.headers.common['Authorization'] = token
}

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!store.getters.loggedIn) {
      next({ name: 'login' })
    } else {
      next()
    }
  } else if (to.matched.some(record => record.meta.requiresLogged)) {
     if (store.getters.loggedIn) {
      next({ name: 'downloads' })
    } else {
      next()
    }
  } else {
    next()
  }
})

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
