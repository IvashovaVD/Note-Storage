/* eslint-disable */
<template lang="pug">
<div>
    <form class="login-view">
        <input type="text" v-model="name" placeholder="Name note...">
        <br>
        textarea.form-input(v-model="textn" rows=8 placeholder="Text your note...")
        <input type="url" v-model="urln" placeholder="URL...">
        <hr width="100%" size="1" color="#5A5256" />
<div v-for="f in folderss.notes" class="login-view" id="noteid">
<button @click="submitForm(f.num_folder)">create note</button>
</div>
</form>

</div>
  </template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'create-note',
  computed: mapGetters(['folderss']),
  data () {
    return {
      'num_folder': '',
      'name': '',
      'textn': '',
      'urln': ''
    }
  },
  methods: {
    submitForm (f) {
      this.num_folder = f
      this.createNote()
      this.name = ''
      this.textn = ''
      this.urln = ''

      event.preventDefault()
    },
    createNote () {
      this.$store.dispatch('createNote', { num_folder: this.num_folder, name: this.name, textn: this.textn, urln: this.urln, available: false })
    }
  }
}
</script>
<style>
#noteid {
height: 0px;
padding:0
}
#noteid button{
margin: 0px;
}
</style>
