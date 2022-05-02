import Vue from 'vue'
import Router from 'vue-router'
import Home from '../components/HelloWorld'
import note from '../components/Notes'
import folder from '../components/FolderNoteFile'

import login from '../views/reg/Login'
import register from '../views/reg/Register'
import downloads from '../views/reg/Downloads'
import logout from '../views/reg/Logout'
import createfile from '../views/fileview/CreaeteFile'
import createfolder from '../views/folderview/CreateFolder'
import createnote from '../views/noteview/CreateNote'
import store from '@/store'

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

const requireAuthenticated = (to, from, next) => {
  store.dispatch('auth/initialize')
    .then(() => {
      if (!store.getters['auth/isAuthenticated']) {
        next('/login')
      } else {
        next()
      }
    })
}

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/login/',
      name: 'login',
      component: login
    },
    {
      path: '/signup/',
      name: 'register',
      component: register,
      beforeEnter: requireUnauthenticated
    },
    {
      path: '/users/',
      name: 'downloads',
      component: downloads,
      beforeEnter: requireAuthenticated
    },
    {
      path: '/folders/',
      name: 'folders',
      component: folder,
      beforeEnter: requireAuthenticated
    },
    {
      path: '/notes/',
      name: 'note',
      component: note,
      beforeEnter: requireAuthenticated
    },
    {
      path: '/add/notes/',
      name: 'createnote',
      component: createnote
    },
    {
      path: '/files/',
      name: 'createfile',
      component: createfile
    },
    {
      path: '/folder/:id',
      name: 'createfolder',
      component: createfolder
    },
    {
      path: '/logout',
      name: 'logout',
      component: logout,
      beforeEnter: redirectLogout
    }
  ]
})
