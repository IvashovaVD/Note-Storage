/* eslist-disable */
<template lang="pug">
<div>
  <code>Create date folder {{folderss.release_date}} </code>
  <div class="list-view" >
       <h2>{{folderss.name}}</h2>
  </div>
  <div class="list-view" >
    <div v-for="(not,index) in folderss.notes">
    <ul>
    <li class="list-li">
    <h4 style="color:#3fb984">{{not.name}} (Note)</h4>
        <sup>date create: {{not.created_at}}</sup> <br>
        <sup>date update: {{not.updated_at}}</sup>
        <hr>
    <kbd width="100%">{{not.textn}}</kbd>
    <a v-bind:href="not.urln" class="list-a">{{not.urln}}</a>
    </li>
    </ul>
    </div>
  </div>
    </div>
</template>
<script>
import Files from '../fileview/Files'
import { mapGetters } from 'vuex'
export default {
  name: 'createfolder',
  components: {
    'files': Files
  },
  data () {
    return {
      note: []
    }
  },
  computed: mapGetters(['folderss'])
}
</script>
