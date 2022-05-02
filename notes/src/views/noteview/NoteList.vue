/* eslist-disable */
<template lang="pug">
  <div>
  <a class="bu">
  <router-link :to = "{ name:'createnote' }">CREATE NOTE</router-link> |||
  <router-link :to = "{ name:'createfile' }">ADD FILE</router-link>
  </a>
    <form class="note-view" v-for="note in notes">
        <h3>{{note.name}}</h3>
        <br>
        <input type="text" v-model="name" placeholder="Change Name note...">
        <br>
        <i>Close view</i>
        <input type="checkbox" class="che" v-model="available">
        <hr width="100%" size="1" color="#5A5256" />
         <b>Text note</b>
        <p>{{note.textn}} </p>
        textarea.form-input(v-model="textn" rows=8 placeholder="Change Text your note...")
        <hr width="100%" size="1" color="#5A5256" />
        <b>url</b>
        <i>{{note.urln}} </i>
        <input type="url" v-model="urln" placeholder="Change URL...">
        <hr width="100%" size="1" color="#5A5256" />
        <button class="b" @click="updateNote(note)">update</button>
        <button class="b" @click="deleteNote(note)" float="left">delete</button>
        <i class="folder-subject">create:  {{note.created_at}}</i>
        <br>
        <i class="folder-subject">update: {{note.updated_at}}</i>
    </form>
  </div>
</template>
<script>
import { mapGetters } from 'vuex'
export default {
  name: 'note',
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
.note-view {
   margin:0 30%;
   padding:3%
}
.note-view {clear:both; text-align:right;}
.note-view b, p, h3, .b {float:left; padding-right:20px;}
.note-view input {width:90%;}
.note-view .che {width:5%; float:right}

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
