<template lang="pug">
  <div class="login-view">
    <h1>Create Folder</h1>
    <form @submit.prevent="submit">
      <input v-model="name" type="text" id="name" placeholder="name">
    </form>
    <button @click="submitForm">
      login create folder
    </button>
  </div>
</template>

<script>
export default {
  name: 'create-folder',
  data () {
    return {
      'name': ''
    }
  },
  methods: {
    submitForm (event) {
      this.createFolder()
      this.name = ''
      event.preventDefault()
    },
    createFolder () {
      this.$store.dispatch('createFolder', { num_user: this.num_user, name: this.name })
    }
  }
}
</script>
