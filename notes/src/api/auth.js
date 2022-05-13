import session from './session'

export default {
  login (username, password) {
    return session.get('/login/', {
      params: {
        username: username,
        password: password
      }})
  },
  logout () {
    return session.get('/logout/', {})
  },
  createAccount (username, password, email) {
    return session.post('/signup/', { username, password, email })
  },
  getAccountDetails () {
    return session.get('/users/')
  },
  updateAccountDetails (data) {
    return session.patch('/users/', data)
  }
}
