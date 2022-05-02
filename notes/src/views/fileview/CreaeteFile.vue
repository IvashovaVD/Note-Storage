<template lang="pug">
  <div class="login-view">
    <router-link :to = "{ name:'note' }">NOTES</router-link>
    <h1>Create File</h1>

    <form @submit.prevent="submit">
      <strong>tagging</strong>
      <select v-model="tagging" id="tagging" placeholder="i">
        <option>i</option>
        <option>d</option>
        <option>v</option>
        <option>m</option>
        <option>o</option>
      </select>
       <strong v-model="tag" id="tag" v-if="tagging=='i'">image</strong>
       <strong v-model="tag" id="tag" v-else-if="tagging=='d'">document</strong>
       <strong v-model="tag" id="tag" v-else="tagging=='o'">other</strong>
    </form>
    <button @click="submitForm">create file</button>
  </div>
</template>

<script>
export default {
  name: 'createfile',
  data () {
    return {
      'tagging': ''
    }
  },
  methods: {
    submitForm (event) {
      this.createFile()
      this.tagging = ''
      event.preventDefault()
    },
    createFile () {
      this.$store.dispatch('createFile', {tagging: this.tagging})
    }
  }
}
</script>
