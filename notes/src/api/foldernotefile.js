import session from './session'
/* eslint-disable */
export const FolderV = {
  create (config) {
    return session.post('/folders/', config).then(response => {
      return response.data
    }
    )
  },
  delete (folders) {
    return session.delete('/folders/${folders}/')
  },
  list () {
    return session.get('/folders/').then(response => {
      return response.data
    })
  }
}
