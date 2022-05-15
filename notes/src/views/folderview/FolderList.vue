/* eslist-disable */
<template lang="pug">
<div>

    <div class="login-view" v-for="user in user">
    <h1> {{user.username}} </h1>

    <div>
        <b>[{{user.id}}] / </b>
        <b>{{user.username}} / </b>
        <b>{{user.email}}</b>
    </div>
    <div class="list" v-for="folder in user.folders">
    <pre>{{folder}}   </pre>
    <router-link :to = "{ name:'filesnote' }">
    <button style="background-color:white; color:black; font-size:10px" @click="getFolders(folder)">preview</button>
    </router-link>
    <router-link :to = "{ name:'note' }">
    <button style="background-color:#3fb984; color:black; font-size:10px" @click="getFolders(folder)">change</button>
    </router-link>
    <button style="background-color:#a72a64; color:white; font-size:10px" @click="deleteFolder(folder)">delete</button>
    <hr>
    </div>
    <form>
      <input v-model="name" type="text" id="name" placeholder="name">
          <button @click="submitFolder(user.id)">create folder</button>
    </form>
</div>
</div>
</template>
<script>
import { mapGetters } from 'vuex'
import axios from 'axios'
export default {
  name: 'folder-list',
  data () {
    return {
      folders: [],
      'name': '',
      'num_user': '',
      'message': ''
    }
  },
  computed: mapGetters(['user']),
  methods: {
    deleteFolder (folder) {
      this.message = 'Folder deleted. Update page and show'
      alert(this.message)
      axios.delete(folder)
    },
    getFolders (folder) {
      this.$store.dispatch('getFolders', folder)
    },
    submitFolder (id) {
      // eslint-disable-next-line
      this.message = 'Folder '+ this.name +' created. Update page and look for'
      alert(this.message)
      this.createFolder(id)
      this.num_user = this.id
      this.name = ''
      event.preventDefault()
    },
    createFolder (id) {
      this.$store.dispatch('createFolder', { num_user: id, name: this.name })
    }
  }
}
</script>
<style>
  header{
    margin-top: 50px;
  }
  .list {
    position: relative;
    padding: 15px 0;
    outline: none;
    letter-spacing: 1px;
    color: black;
    text-shadow: 0 0 1px rgb(255 255 255 / 30%);
  }
</style>
