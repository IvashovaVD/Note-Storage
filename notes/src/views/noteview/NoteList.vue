/* eslist-disable */
<template lang="pug">
  <div>
  <a class="bu" href="#top" title="top"> top
  <router-link :to = "{ name:'createnote' }"  title="create note">create note</router-link>
  <router-link :to = "{ name:'createfile' }" title="add file">add file</router-link>
  </a>
    <form class="note-view" v-for="(note,index) in folderss.notes">
        <h3 id="note">{{note.name}}</h3>
         <button class="b" @click="deleteN(note.id)" style="float:right">delete</button>
        <br>
        <br>

        <hr width="100%" size="1" color="#5A5256" />
         <b>Text note</b>
        <code>{{note.textn}} </code>
        <hr width="100%" size="1" color="#5A5256" />
        <b>url</b>
        <i>{{note.urln}} </i>
        <hr width="100%" size="1" color="#5A5256" />
        <i class="folder-subject">create:  {{note.created_at}}</i>

    </form>
  </div>
</template>
<script>
import { mapGetters } from 'vuex'
import axios from 'axios'
export default {
  name: 'note',
  data () {
    return {
      'name': '',
      'textn': '',
      'urln': '',
      'message': ''
    }
  },
  computed: mapGetters(['folderss']),
  methods: {
    deleteNote (note) {
      this.$store.dispatch('deleteNote', this.message)
      this.$router.push({ name: 'note' })
    },
    deleteN (note) {
      // eslint-disable-next-line
      this.message = 'Note '+ this.name +' deleted'
      alert(this.message)
      // eslint-disable-next-line
      this.message='http://127.0.0.1:8000/main/notes/'+ note +'/'
      axios.delete(this.message)
    }
  },
  created () {
    let folder = this.$cookies.get('folder')
    this.$store.dispatch('getFolders', folder)
  }
}
</script>

<style>
.note-view {
   margin:0 30%;
   padding:3%
}
.note-view {clear:both;}
.note-view b, p, h3, .b {float:left; padding-right:20px;}
.note-view input {width:100%;}
.note-view .che {float:right}

.bu, .but {
    position: fixed; top:15%; right:3%; border-color: #6f7073; padding:3%;
    text-decoration: none;
    font-family: 'Quicksand', sans-serif;
    font-size: 22px;
    font-weight: bold;
    color: white;
    padding: 10px;
    border-radius: 7px;
    border: 5px solid;
    }
</style>
