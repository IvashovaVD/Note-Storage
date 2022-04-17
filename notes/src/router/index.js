import Vue from 'vue'
import Router from 'vue-router'
import Home from '../components/HelloWorld'
import Folder from '../views/folderview/FolderList'
import login from '../views/reg/Login'
import register from '../views/reg/Register'
import downloads from '../views/reg/Downloads'
import logout from '../views/reg/Logout'
import store from '@/store'

const requireAuthenticated = (to, from, next) => {
  store.dispatch('auth/initialize')
    .then(() => {
      if (!store.getters['auth/isAuthenticated']) {
        next('/users/')
      } else {
        next()
      }
    })
}

const requireUnauthenticated = (to, from, next) => {
  store.dispatch('auth/initialize')
    .then(() => {
      if (store.getters['auth/isAuthenticated']) {
        next('/home')
      } else {
        next()
      }
    })
}

const redirectLogout = (to, from, next) => {
  store.dispatch('auth/logout')
    .then(() => next('/login/'))
}

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
      beforeEnter: requireAuthenticated
    },
    {
      path: '/users/',
      name: 'user',
      component: Folder
    },
    {
      path: '/login/',
      name: 'login',
      component: login,
      beforeEnter: requireUnauthenticated
    },
    {
      path: '/signup/',
      name: 'register',
      component: register
    },
    {
      path: '/users/',
      name: 'downloads',
      component: downloads
    },
    {
      path: '/logout',
      name: 'logout',
      component: logout,
      beforeEnter: redirectLogout
    }
  ]
})
