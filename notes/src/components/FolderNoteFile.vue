/* eslist-disable */
<template lang="pug">
  #app
    createfolders
    files
</template>
<script>
import Files from '../views/fileview/Files'
import CreateFolder from '../views/folderview/CreateFolder'
export default {
  name: 'filesnote',
  components: {
    'files': Files,
    'createfolders': CreateFolder
  }
}
</script>
<style>
  header{
    margin-top: 50px;
  }
  .list-view {
  display:flex;
  justify-content: center;
  flex-wrap: wrap;
  align-items: center;
  width: 80%;
  margin: 0 10%
  }
  .list-li {
  text-decoration:none;
  color:white;
  background:#2f3033;
  display:block;
  height:auto;
  width:auto;
  max-width: 20em;
  word-wrap: break-word;
  padding:1em;
  -moz-box-shadow:5px 5px 7px rgba(33,33,33,1);
  -webkit-box-shadow: 5px 5px 7px rgba(33,33,33,.7);
  box-shadow: 5px 5px 7px rgba(33,33,33,.7);
  -moz-transition:-moz-transform .15s linear;
  -o-transition:-o-transform .15s linear;
  -webkit-transition:-webkit-transform .15s linear;
  }
  .list-a {
  text-decoration:none;
  color:white;
  }
  .list-a:active, .list-a:focus, .list-a:hover {
  color: rgb(63, 185, 132);
  text-decoration:none;
  }
</style>
