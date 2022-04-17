/* eslint-disable */
import Vue from 'vue'
import Vuex from 'vuex'
import { Note } from '../api/notes'
import { Folder } from '../api/user'
import createLogger from 'vuex/dist/logger'

import auth from './reg/auth'
import signup from './reg/signup'

import {
  ADD_NOTE,
  REMOVE_NOTE,
  SET_NOTES,
  ADD_FOLDER,
  REMOVE_FOLDER,
  SET_FOLDERS
} from './notes/mutation-types.js'

const debug = process.env.NODE_ENV !== 'production';

Vue.use(Vuex)

const state = {
  notes: [],
  folders: []
}

const getters = {
  notes: state => state.notes,
  folders: state => state.folders,
}

const mutations = {

  [ADD_NOTE] (state, note) {
    state.notes = [note, ...state.notes]
  },

  [ADD_FOLDER] (state, folder) {
    state.folders = [folder, ...state.folders]
  },

  [REMOVE_NOTE] (state, { id }) {
    state.notes = state.notes.filter(note => {
      return note.id !== id
    })
  },

  [REMOVE_FOLDER] (state, { id }) {
    state.folders = state.folders.filter(folder => {
      return folder.id !== id
    })
  },

  [SET_NOTES] (state, { notes }) {
    state.notes = notes
  },

  [SET_FOLDERS] (state, { folders }) {
    state.folders = folders
  }
}

const actions = {
  createNote ({ commit }, noteData) {
    Note.create(noteData).then(note => {
      commit(ADD_NOTE, note)
    })
  },
  deleteNote ({ commit }, note) {
    Note.delete(note).then(response => {
      commit(REMOVE_NOTE, note)
    })
  },
  getNotes ({ commit }) {
    Note.list().then(notes => {
      commit(SET_NOTES, { notes })
    })
  },
  createFolder ({ commit }, folderData) {
    Folder.create(folderData).then(folder => {
      commit(ADD_FOLDER, folder)
    })
  },
  deleteFolder ({ commit }, folder) {
    Folder.delete(folder).then(response => {
      commit(REMOVE_FOLDER, folder)
    })
  },
  getFolders ({ commit }) {
    Folder.list().then(folders => {
      commit(SET_FOLDERS, { folders })
    })
  }
}

export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations,
  modules: {
  auth,
  signup
  },
  strict: debug,
  plugins: debug ? [createLogger()] : [],
});