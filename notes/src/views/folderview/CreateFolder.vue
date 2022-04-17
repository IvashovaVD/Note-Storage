<template lang="pug">
  form.form-horizontal(@submit="submitForm" id="formFolder")
    .form-group
      .col-3
        label.form-label Folder
      .col-9
        input.form-input(type="num_user" v-model="num_user" placeholder="User...")
    .form-group
      .col-3
        label.form-label Title
      .col-9
        input.form-input(type="name" v-model="name" placeholder="Type note title...")

    .form-group
      .col-3
      .col-9
        button.btn.btn-primary(type="submit") Create
      .col-3
      .col-9
        button.btn.btn-primary(type="reset") Clear
 </template>

<script>
export default {
  name: 'create-folder',
  data () {
    return {
      'num_user': '',
      'name': ''
    }
  },
  methods: {
    submitForm (event) {
      this.createFolder()
      this.num_user = ''
      this.name = ''

      event.preventDefault()
    },
    createFolder () {
      this.$store.dispatch('createNote', { num_user: this.num_user, name: this.name })
    }
  }
}
</script>
