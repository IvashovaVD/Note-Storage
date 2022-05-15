import session from './session'
/* eslint-disable */
export const FolderV = {
  create (config) {
    return session.post('/users/', config).then(response => {
      return response.data
    }
    )
  },
  delete (folders) {
    return session.delete('/main/folders/${folders}/')
  },
  list (username) {
    return session.get('/users/', {
    params: {
        username: username
        }})
        .then(response => {
           return response.data
    })
  }
}
