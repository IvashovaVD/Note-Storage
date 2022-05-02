import session from './session'
/* eslint-disable */
export const File = {
  create (config) {
    return session.post('/files/', config).then(response => {
      return response.data
    }
  )
  },
  delete (note) {
    return session.delete('/files/${file}/')
  },
  list () {
    return session.get('/files/').then(response => {
      return response.data
    })
  }
}
