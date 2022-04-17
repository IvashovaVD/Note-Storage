/* eslist-disable */
<template lang="pug">
  #app
    .card(v-for="note in notes")
      .card-header
        button.btn.btn-clear.float-right(@click="deleteNote(note)")
        .card-title {{ note.name }}
        .card-subtitle {{ note.created_at }}
      .card-body {{ note.textn }}
</template>
<script>
import { mapGetters } from 'vuex'
export default {
  name: 'note-list',
  computed: mapGetters(['notes']),
  methods: {
    deleteNote (note) {
      this.$store.dispatch('deleteNote', note)
    }
  },
  beforeMount () {
    this.$store.dispatch('getNotes')
  }
}
</script>
<style>
  header{
    margin-top: 50px;
  }
</style>
