<template lang="pug">
  <div class="filenote">
  <div class="naf">
    <ul>
       <li><a>NOTES</a>
         <ul>
            <li v-for="note in folderss.notes">
            <a href="#note">{{note.name}}</a>
            </li>
         </ul>
       </li>
       <li><a>FILES</a>
         <ul>
              <li  v-for="file in folderss.files"  style="margin:0; padding:0;">
              <a href="#file">id file: {{file.id}}</a>
              </li>
         </ul>
       </li>
    </ul>
    </div>
    note
    <hr>
    file
    </div>
</template>
/* eslint-disable */
<script>
import FileList from '../views/fileview/FileList'
import NoteList from '../views/noteview/NoteList'
import { mapGetters } from 'vuex'
export default {
  name: 'app',
  computed: mapGetters(['folderss']),
  components: {
    'file': FileList,
    'note': NoteList
  }
}
</script>
<style>
.naf {position: fixed;}
.filenote ul {
   list-style: none;
  margin: 0;
  padding: 0;
  margin-top:25px;
  background:#2f3033;
  height: 50px;
}
.filenote a {
    text-decoration: none;
    background: #2f3033;
    color: #fbfbfe;
    padding: 0px 15px;
    font-family: arial;
    line-height: 50px;
    display: block;
  border-bottom: 2px solid #ffffff;
}
.filenote a:hover {background:#3fa67d;}
.filenote li {
  float:left;
  position:relative;
  margin-top: 0;
}
li > ul {
        position:absolute;
        top:25px;
        display:none;
}
li:hover >ul {
        display:block;
        width:250px;
}
li:hover > ul > li {
        float:none;
    }
</style>
