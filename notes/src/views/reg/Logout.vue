 /* eslint-disable */
<template>
  <div class="log">

  </div>
</template>

<script>
export default {
  created () {
    this.$store.dispatch('logout')
      .then(() => {
        this.$cookie.delete('username')
        this.$cookie.delete('folder')
        this.$router.push({ name: 'home' })
      })
  }
}
</script>
