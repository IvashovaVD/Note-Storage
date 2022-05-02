/* eslint-disable */
<template lang="pug">
    <form class="login-view" @submit.prevent="submit">
        <input type="text" v-model="name" placeholder="Name note...">
        <br>
        <i>Close view
        <input type="checkbox" v-model="available"></i>
        textarea.form-input(v-model="textn" rows=8 placeholder="Text your note...")
        <input type="url" v-model="urln" placeholder="URL...">
        <hr width="100%" size="1" color="#5A5256" />
          <button @click="submitForm">create note</button>
    </form>
  </template>

<script>
export default {
  name: 'create-note',
  data () {
    return {
      'num_folder': '',
      'name': '',
      'textn': ''
    }
  },
  methods: {
    submitForm (event) {
      this.createNote()
      this.num_folder = ''
      this.name = ''
      this.textn = ''

      event.preventDefault()
    },
    createNote () {
      this.$store.dispatch('createNote', { num_folder: this.num_folder, name: this.name, textn: this.textn })
    }
  }
}
</script>
