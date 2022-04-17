import session from './session'
/* eslint-disable */
export const Folder = {
  create (config) {
    return session.post('/add/folders/', config).then(response => {
      return response.data
    }
  )
  },
  delete (id) {
    return session.delete('/change/folders/' + id)
  },
  list () {
    return session.get('/users/').then(response => {
      return response.data
    })
  }
}
