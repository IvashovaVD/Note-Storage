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
        this.$router.push({ name: 'home' })
      })
  }
}
</script>
