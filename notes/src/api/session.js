import axios from 'axios'

const session = axios.create({
  baseURL: 'http://127.0.0.1:8000/main/',
  xsrfCookieName: 'csrftoken',
  xsrfHeaderName: 'X-CSRFTOKEN'
})

export default session
