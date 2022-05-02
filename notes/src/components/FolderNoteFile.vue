/* eslist-disable */
<template lang="pug">
  #app
    <div class="form-signin" v-for="folder in folderv">
    <h1> {{folder.name}} </h1>
    <p>
        <b class="folder-index">[{{folder.id}}] / </b>
        <b class="folder-subject">{{folder.release_date}} / </b>
    </p>
        <p>{{folder.notes}}</p> <br>
        <p>{{folder.files}}</p>
    </div>
</template>
<script>
import { mapGetters } from 'vuex'
import '@/store'
export default {
  name: 'folder',
  computed: mapGetters(['folderv']),
  methods: {
    getFolderV () {
      this.$store.dispatch('getFolderV')
    }
  },
  beforeMount () {
    this.$store.dispatch('getFolderV')
  }
}
</script>
<style>
  header{
    margin-top: 50px;
  }
</style>
