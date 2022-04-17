/* eslist-disable */
<template lang="pug">
  #app
    <div class="form-signin" v-for="folder in folders">
    <h1> {{folder.username}} </h1>
    button.btn.btn-clear.float-right(@click="deleteFolder(folder)")
    <p>
        <b class="folder-index">[{{folder.id}}] / </b>
        <b class="folder-subject">{{folder.username}} / </b>
        <b class="folder-subject">{{folder.email}}</b>
    </p>
        <i class="folder-subject">{{folder.folders}}</i>
    </div>
</template>
<script>
import { mapGetters } from 'vuex'
import '@/store'
export default {
  name: 'folder-list',
  computed: mapGetters(['folders']),
  methods: {
    deleteFolder (folder) {
      this.$store.dispatch('deleteFolder', folder)
    },
    getFolders () {
      this.$store.dispatch('getFolders')
    }
  },
  beforeMount () {
    this.$store.dispatch('getFolders')
  }
}
</script>
<style>
  header{
    margin-top: 50px;
  }
</style>
