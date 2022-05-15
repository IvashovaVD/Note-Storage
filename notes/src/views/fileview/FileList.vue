/* eslist-disable */
<template lang="pug">
  <div>
    <form class="note-view" v-for="file in folderss.files">
        <i class="tag">{{file.tagging}}</i>
        <a class="tag" v-bind:href="file.filen">{{file.filen}}</a>
        <button @click="deleteFile(file.id)"  style="float:right">delete</button>
        <hr width="100%" size="1" color="#5A5256" />
        <i id="file">id file: {{file.id}}, </i>
        <i class="folder-subject">create:  {{file.created_at}}</i>
    </form>
  </div>
</template>
<script>
import { mapGetters } from 'vuex'
import axios from 'axios'
export default {
  name: 'file',
  computed: mapGetters(['folderss']),
  methods: {
    deleteFile (file) {
      // eslint-disable-next-line
      this.message = 'File deleted'
      alert(this.message)
      // eslint-disable-next-line
      this.message='http://127.0.0.1:8000/main/files/'+ file +'/'
      axios.delete(this.message)
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
.note-view .che {width:5%;}
.note-view .tag {
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

.note-view .tag:hover {text-decoration: none;}
</style>
