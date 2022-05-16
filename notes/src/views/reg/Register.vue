<template>
  <div id="register-view"  class="login-view">
    <h1>Create Account</h1>
    <template v-if="registrationLoading">
      loading...
    </template>
    <template v-else-if="!registrationCompleted">
      <form @submit.prevent="submit">
        <input v-model="inputs.username" type="text" id="username" placeholder="username">
        <input v-model="inputs.password" type="password" id="password" placeholder="password">
        <input v-model="inputs.email" type="email" id="email" placeholder="email">
      </form>
      <button @click="createAccount(inputs)">
        create account
      </button>
      <br>
      <span class="error" v-show="registrationError">
        An error occured while processing your request.
      </span>
     </template>
    <template v-else>
      <div>
        Registration complete. You should receive an email shortly with instructions on how to
        activate your account.
      </div>
      <div>
        <router-link to="/login">return to login page</router-link>
      </div>
    </template>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
export default {
  data () {
    return {
      inputs: {
        username: '',
        password: '',
        password2: '',
        email: ''
      }
    }
  },
  computed: mapState('signup', [
    'registrationCompleted',
    'registrationError',
    'registrationLoading'
  ]),
  methods: mapActions('signup', [
    'createAccount',
    'clearRegistrationStatus'
  ]),
  createAccount ({username, password, email}) {
    this.$store.dispatch('auth/signup', { username, password, email })
    this.$store.dispatch('auth/login', { username, password })
  },
  beforeRouteLeave (to, from, next) {
    this.clearRegistrationStatus()
    next()
  }
}
</script>

<style>
form input {
  display: block
}
.error {
  color: crimson;
  font-size: 12px;
}
</style>
