<template lang="pug">
  <div class="filenote">
  <div class="naf">
    <ul>
       <li><a>NOTES</a>
         <ul>
            <li  v-for="note in folderss.notes">
            <a href="#note.name">{{note.name}}</a>
            </li>
         </ul>
       </li>
       <li><a>FILES</a>
         <ul>
              <li  v-for="file in folderss.files">
              <a href="#file.filen">{{file.filen}}</a>
              </li>
         </ul>
       </li>
    </ul>
    </div>
    <br><br>
    <hr>
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
  background:#819A32;
  height: 50px;
}
.filenote a {
  text-decoration: none;
  background:#819A32;
  color:#fff;
  padding:0px 15px;
  font-family: arial;
  line-height:50px;
  display: block;
  border-right: 1px solid #677B27;
  -moz-transition: all 0.3s 0.01s ease;
  -o-transition: all 0.3s 0.01s ease;
  -webkit-transition: all 0.3s 0.01s ease;
}
.filenote a:hover {background:#D43737;}
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
