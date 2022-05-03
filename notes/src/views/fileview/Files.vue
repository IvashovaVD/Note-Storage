/* eslist-disable */
<template lang="pug">
  <div class="list-view">
    #app
    <div v-for="fil in folderss.files">
    <ul>
    <li class="list-li">
    <h4 style="color:#3fb984">
       <strong v-if="fil.tagging=='i'">Image (File)</strong>
       <strong v-else-if="fil.tagging=='d'">Document (File)</strong>
       <strong v-else-if="fil.tagging=='v'">Video (File)</strong>
       <strong v-else="fil.tagging=='o'">Other (File)</strong>
    </h4>
    <sup>date add: {{fil.created_at}}</sup>
    <a class="list-a" v-bind:href="fil.filen">{{fil.filen}}</a>
    </li>
    </ul>
    </div>
  </div>
</template>
<script>
import { mapGetters } from 'vuex'
export default {
  name: 'createfolder',
  data () {
    return {
      note: []
    }
  },
  computed: mapGetters(['folderss'])
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
</style>
