import session from './session'
/* eslint-disable */
export const FolderV = {
  create (config) {
    return session.post('/main/folders/', config).then(response => {
      return response.data
    }
    )
  },
  delete (folders) {
    return session.delete('/main/folders/${folders}/')
  },
  list () {
    return session.get('/main/folders/').then(response => {
      return response.data
    })
  }
}
