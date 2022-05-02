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
    {{user_id}}
  </div>
</template>

<script>
export default {
  data () {
    return {
      inputs: {
        username: '',
        password: ''
      },
      user_id: ''
    }
  },
  methods: {
    login ({ username, password }) {
      this.$store.dispatch('auth/login', { username, password })
        .then(() => this.$router.push('downloads/{user_id}'))
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
