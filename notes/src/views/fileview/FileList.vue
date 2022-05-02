/* eslist-disable */
<template lang="pug">
  <div>
    <form class="note-view" v-for="file in files">
        <i class="tag">{{file.tagging}}</i>
        <a class="tag" v-bind:href="file.filen">{{file.filen}}</a>
        <hr width="100%" size="1" color="#5A5256" />
        <input type="file" placeholder="filen...">
        <hr width="100%" size="1" color="#5A5256" />
        <button class="b" @click="updateNote(file)">update</button>
        <button class="b" @click="deleteNote(file)" float="left">delete</button>
        <i class="folder-subject">create:  {{file.created_at}}</i>
    </form>
  </div>
</template>
<script>
import { mapGetters } from 'vuex'
export default {
  name: 'file',
  computed: mapGetters(['files']),
  methods: {
    deleteFile (file) {
      this.$store.dispatch('deleteFile', file)
    }
  },
  beforeMount () {
    this.$store.dispatch('getFiles')
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
.note-view .che {width:5%;}
.tag {
    font-family: Helvetica, Arial, sans-serif;
    background: #a72a64;;
    display: inline-block;
    color: #fff;
    position: relative;
    padding: 10px;
    border-top-left-radius: 4px;
    border-bottom-left-radius: 4px;
    text-decoration: none;
}

a:hover {text-decoration: none; color: #a9788a;}

.tag:after {
    display: inline-block;
    border: 20px solid;
    border-color: transparent transparent transparent #a9788a;
    height: 0;
    width: 0;
    position: absolute;
    right: -40px;
    top: 0;
    content: "";
}
</style>
