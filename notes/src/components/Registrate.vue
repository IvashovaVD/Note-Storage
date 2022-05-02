<template>
  <div class="navbar">
    <ul>
      <li align="left"><router-link :to = "{ name:'logout' }">LOGOUT</router-link></li>
      <li align="left"><router-link :to = "{ name:'register' }">REGISTER</router-link></li>
      <li align="left"><router-link :to = "{ name:'login' }">LOGIN</router-link></li>
      <li><router-link :to = "{ name:'downloads' }">FOLDERS</router-link></li>
      <li> <router-link :to = "{ name:'note' }">NOTES</router-link></li>
      <li>
      <router-link :to = "{ name:'home' }" exact>
      <img src="../assets/logo.png" alt="image" width=10%>
      home
      </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'NavBar',
  computed:
   mapState(['accessToken'])
}
</script>

<style scoped>
  @import url(https://fonts.googleapis.com/css?family=Quicksand);
  .navbar {
    background-color: #2f3033;
    width: 100%;
    top: 0;
    left: 0;
    overflow: hidden;
    justify-content: center;
  }
  h1 { font-family: 'Quicksand', sans-serif; }
  .navbar ul {
    list-style: none;
    margin:0;
    padding: 0;
    color: white;
  }
  .navbar ul li {
    display: inline-block;
    margin: 0 5px;
    padding: 25px;
    float: right;
  }
  .navbar:after {
    content: '';
    display: block;
    clear: both;
  }
  .navbar ul li a {
    text-decoration: none;
    font-family: 'Quicksand', sans-serif;
    font-size: 22px;
    font-weight: bold;
    color: white;
    padding: 10px;
    border-radius: 7px;
  }
  .navbar ul li a:hover {
    background-color: #a72a64;
  }
  .router-link-active {
    border-color: #a72a64
  }
@import url(https://fonts.googleapis.com/css?family=Eczar);
@import url(https://fonts.googleapis.com/css?family=Work+Sans);
body {
  font-family: "Work Sans", "Segoe UI", "Helvetica Neue", sans-serif;
}
h1, h2, h3, h4, h5, h6 {
  font-family: "Eczar", sans-serif;
}
</style>
