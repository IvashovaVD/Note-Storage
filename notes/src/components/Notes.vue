<template lang="pug">
  #app
    <h1 float="right" margin-right=10%>Notes</h1>
    <hr>
    note
    <h1 float="right" margin-right=10%>Files</h1>
    <hr>
    file
</template>
/* eslint-disable */
<script>
import FileList from '../views/fileview/FileList'
import NoteList from '../views/noteview/NoteList'
export default {
  name: 'app',
  components: {
    'file': FileList,
    'note': NoteList
  }
}
</script>
