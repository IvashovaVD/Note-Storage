import axios from 'axios'
/* eslint-disable */
export const HTTP = axios.create({
baseURL: 'http://localhost:8000/main',
headers: { contentType: 'application/json' },
xsrfCookieName: 'csrftoken',
xsrfHeaderName: "X-CSRFTOKEN"
})