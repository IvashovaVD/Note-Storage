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
  list (folder) {
    return session.get(folder).then(response => {
      return response.data
    })
  }
}
