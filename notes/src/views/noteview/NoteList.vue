/* eslist-disable */
<template lang="pug">
  <div>
  <a class="bu">
  <router-link :to = "{ name:'createnote' }">CREATE NOTE</router-link>
  <router-link :to = "{ name:'createfile' }">ADD FILE</router-link>
  </a>
    <form class="note-view" v-for="note in folderss.notes">
        <h3 id="note.name">{{note.name}}</h3>
        <br>
        <input type="text" v-model="name" placeholder="Change Name note...">
        <br>

        <hr width="100%" size="1" color="#5A5256" />
         <b>Text note</b>
        <code>{{note.textn}} </code>
        textarea.form-input(v-model="textn" rows=8 placeholder="Change Text your note...")
        <hr width="100%" size="1" color="#5A5256" />
        <b>url</b>
        <i>{{note.urln}} </i>
        <input type="url" v-model="urln" placeholder="Change URL...">
        <hr width="100%" size="1" color="#5A5256" />
        <i class="folder-subject">create:  {{note.created_at}}</i>
        <br>
        <i class="folder-subject">update: {{note.updated_at}}</i>
        <br>
        <button class="b" @click="submitNote(note.id)">update</button>
        <button class="b" @click="deleteN(note.id)" float="left">delete</button>
        <br>
    </form>
  </div>
</template>
<script>
import { mapGetters } from 'vuex'
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
    },
    deleteN (note) {
      // eslint-disable-next-line
      this.message = 'Note '+ this.name +' deleted'
      alert(this.message)
      // eslint-disable-next-line
      this.message='http://127.0.0.1:8000/main/notes/'+ note +'/'
      this.deleteNote(this.message)
    },
    submitNote (id) {
      // eslint-disable-next-line
      this.message = 'Note '+ this.name +' created'
      alert(this.message)
      this.putNote(id)
      this.num_folder = this.id
      this.name = ''
      event.preventDefault()
    },
    createFolder (id) {
      this.$store.dispatch('putFolder', { num_user: id, name: this.name }) // TODO
    }
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
