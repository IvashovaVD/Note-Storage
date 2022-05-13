<template lang="pug">
  <div>
    <button style="float:left; background:white"><router-link :to = "{ name:'note' }">BACK</router-link></button>

    <div @submit.prevent="submit" class="login-view">
        <h3>Create note for Folder: {{folderss.id}} - {{folderss.name}}</h3>
    <div style="float:left">
      <strong>tagging</strong>
      <select v-model="tagging" id="tagging" value="i">
        <option selected>i</option>
        <option>d</option>
        <option>v</option>
        <option>m</option>
        <option>o</option>
      </select>
       <strong v-model="tagging" id="tag" v-if="tagging=='i'">image</strong>
       <strong v-model="tagging" id="tag" v-else-if="tagging=='d'">document</strong>
       <strong v-model="tagging" id="tag" v-else-if="tagging=='v'">vidio</strong>
       <strong v-model="tagging" id="tag" v-else-if="tagging=='m'">music</strong>
       <strong v-model="tagging" id="tag" v-else="tagging=='o'">other</strong>
       <input type="file" id="file" ref="file" v-on:change="handleFileUpload()"/>
       </div>
       <button@click="submitForm(folderss.id)">add file</button>
    </div>

  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'createfile',
  computed: mapGetters(['folderss']),
  data () {
    return {
      'tagging': 'i',
      'filen': ''
    }
  },
  methods: {
    handleFileUpload () {
      this.file = this.$refs.file.files[0]
    },
    submitForm (id) {
      this.createFile(id)
      this.tagging = ''
      this.filen = ''
      event.preventDefault()
    },
    createFile (id) {
      let formData = new FormData()
      formData.append('num_folder', id)
      formData.append('tagging', this.tagging)
      formData.append('filen', this.file)
      this.$store.dispatch('createFile', formData)
      alert('SUCCESS')
    }
  }
}
</script>
