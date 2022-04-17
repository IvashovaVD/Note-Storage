/* eslint-disable */
<template>
  Logout
</template>
<script>
  import { LogoutOptions } from '../types'
  export default {
    data (){
      return {
      }
    },
    created:function(){
      Auth.logout();
      console.log(Auth.getLogin());
      this.$router.go('/home');
    }
  }
</script>
