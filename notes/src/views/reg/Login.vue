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
    login ({ username, password }) {
      this.$store.dispatch('auth/login', { username, password })
        .then(() => this.$router.push('users'))
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
