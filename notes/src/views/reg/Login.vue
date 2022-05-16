<template>
  <div class="login-view">
    <h1>Login</h1>
    <form @submit.prevent="submit">
      <input v-model="inputs.username" type="text" id="username" placeholder="username">
      <input v-model="inputs.password" type="password" id="password" placeholder="password">
    </form>
    <button @click="login(inputs)" id="login-button">
      login
    </button>
  </div>
</template>

<script>
import VueCookies from 'vue-cookies'
export default {
  data () {
    return {
      inputs: {
        username: '',
        password: ''
      }
    }
  },
  methods: {
    /* eslint-disable */
    login ({ username, password }) {
      this.$store.dispatch('auth/login', { username, password })
        .then(response => {
        VueCookies.set('username', username, 'expiring time')
        this.$router.push({ name: 'downloads' })
        }
        )
      .catch(e => {
        alert('error in login or password')
        this.$router.push({ name: 'logout' })
      })
    }
  }
}
</script>
<style>
form input {
  display: block;
  width:100%;
  padding:3%
}
.login-view{
margin:0 30%;
padding:3%
}
</style>
