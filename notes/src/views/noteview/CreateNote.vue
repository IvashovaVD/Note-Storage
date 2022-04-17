/* eslint-disable */
<template lang="pug">
  form.form-horizontal(@submit="submitForm" id="formNote")
    .form-group
      .col-3
        label.form-label Folder
      .col-9
        input.form-input(type="text" v-model="num_folder" placeholder="Name folder...")
    .form-group
      .col-3
        label.form-label Title
      .col-9
        input.form-input(type="text" v-model="name" placeholder="Type note title...")
    .form-group
      .col-3
        label.form-label Body
      .col-9
        textarea.form-input(v-model="textn" rows=8 placeholder="Type your note...")
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
  name: 'create-note',
  data () {
    return {
      'num_folder': '',
      'name': '',
      'textn': ''
    }
  },
  methods: {
    submitForm (event) {
      this.createNote()
      this.num_folder = ''
      this.name = ''
      this.textn = ''

      event.preventDefault()
    },
    createNote () {
      this.$store.dispatch('createNote', { num_folder: this.num_folder, name: this.name, textn: this.textn })
    }
  }
}
</script>
