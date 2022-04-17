import session from './session'

export default {
  login (username, password) {
    return session.post('/login/', { username, password })
  },
  logout () {
    return session.post('/logout/', {})
  },
  createAccount (username, password1, password2, email) {
    return session.post('/signup/', { username, password1, password2, email })
  },
  getAccountDetails () {
    return session.get('/users/')
  },
  updateAccountDetails (data) {
    return session.patch('/users/', data)
  }
}
