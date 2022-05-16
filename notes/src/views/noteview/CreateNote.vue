/* eslint-disable */
<template lang="pug">
<div>
 <button style="float:left; background:white"><router-link :to = "{ name:'note' }">BACK</router-link></button>

    <div @submit.prevent="submit" class="login-view">
        <h2>Folder: {{folderss.name}}</h2>
        <input type="text" v-model="name" placeholder="Name note...">
        textarea.form-input(v-model="textn" rows=8 placeholder="Text your note...")
        <input type="url" v-model="urln" placeholder="URL...">
        <hr width="100%" size="1" color="#5A5256" />

<button @click="submitForm(folderss.id)">create note</button>

</form>
</div>
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
      alert('SUCCESS')
      event.preventDefault()
    },
    createNote () {
      this.$store.dispatch('createNote', { num_folder: this.num_folder, name: this.name, textn: this.textn, urln: this.urln, available: false })
    }
  },
  created () {
    let folder = this.$cookies.get('folder')
    this.$store.dispatch('getFolders', folder)
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
