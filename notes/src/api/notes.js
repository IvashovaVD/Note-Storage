import session from './session'
/* eslint-disable */
export const Note = {
  create (config) {
    return session.post('/notes/', config).then(response => {
      return response.data
    }
  )
  },

  list () {
    return session.get('/notes/').then(response => {
      return response.data
    })
  }
}
