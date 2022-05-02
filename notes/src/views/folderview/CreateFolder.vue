/* eslist-disable */
<template lang="pug">
  <div class="login-view">
    #app
    <div class="list" v-for="not in notes">
    <h1> {{not.name}} </h1>
    <div>
        <b>[{{not.release_date}}] / </b>
    </div>

    <p>{{not.name}}</p>
    <p>{{not.textn}}</p>
    <p>{{not.urln}}</p>
    </div>

  </div>
</template>
<script>
import { mapGetters } from 'vuex'
export default {
  name: 'folder-list',
  data () {
    return {
      note: []
    }
  },
  computed: mapGetters(['notes'])
}
</script>
<style>
  header{
    margin-top: 50px;
  }
  .list {
    position: relative;
    padding: 15px 0;
    outline: none;
    letter-spacing: 1px;
    color: black;
    text-shadow: 0 0 1px rgb(255 255 255 / 30%);
  }
</style>
