/* eslist-disable */
<template lang="pug">
  <div class="login-view">
    #app
    <h1> {{users.username}} </h1>

    <div>
        <b>[{{users.id}}] / </b>
        <b>{{users.username}} / </b>
        <b>{{users.email}}</b>
    </div>
    <div class="list" v-for="folder in users.folders">
    <pre>{{folder}}   </pre>
    <router-link :to = "{ name:'createfolder' }">
    <button style="background-color:white; color:black; font-size:10px">preview</button>
    </router-link>
    <button style="background-color:#3fb984; color:black; font-size:10px" @click="changeFolder(folder)">change</button>
    <button style="background-color:#a72a64; color:white; font-size:10px" @click="deleteFolder(folder)">delete</button>
    <hr>
    </div>
    <form>
      <input v-model="name" type="text" id="name" placeholder="name">
          <button @click="submitFolder(users.id)">create folder</button>
    </form>

  </div>
</template>
<script>
import { mapGetters } from 'vuex'
import axios from 'axios'
export default {
  name: 'folder-list',
  data () {
    return {
      users: [],
      'name': '',
      'num_user': '',
      'message': ''
    }
  },
  computed: mapGetters(['folderss']),
  methods: {
    deleteFolder (folder) {
      this.message = 'Folder deleted. Update page and show'
      alert(this.message)
      axios.delete(folder)
      this.getFolders()
    },
    getFolders () {
      axios.get('http://127.0.0.1:8000/main/users/49/')
        .then(response => {
          this.users = response.data
        })
    },
    submitFolder (id) {
      // eslint-disable-next-line
      this.message = 'Folder '+ this.name +' created'
      alert(this.message)
      this.createFolder(id)
      this.num_user = this.id
      this.name = ''
      this.getFolders()
      event.preventDefault()
    },
    createFolder (id) {
      this.$store.dispatch('createFolder', { num_user: id, name: this.name })
    }
  },
  created () {
    axios.get('http://127.0.0.1:8000/main/users/49/')
      .then(response => {
        this.users = response.data
      })
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
