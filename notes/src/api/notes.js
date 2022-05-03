import session from './session'
/* eslint-disable */
export const Note = {
  create (config) {
    return session.post('/notes/', config).then(response => {
      return response.data
    }
  )
  },
  delete (note) {
    return session.delete(note)
  },
  list () {
    return session.get('/notes/').then(response => {
      return response.data
    })
  }
}
