<template lang="pug">
  #app
     create-folder
     folder-list
</template>
/* eslint-disable */
<script>
import CreateFolder from '../views/folderview/CreateFolder'
import FolderList from '../views/folderview/FolderList'
export default {
  name: 'app',
  components: {
    'create-folder': CreateFolder,
    'folder-list': FolderList
  }
}
</script>
