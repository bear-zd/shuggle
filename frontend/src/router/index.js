import {createRouter, createWebHashHistory} from 'vue-router'
import login from "../view/login";



const routes = [
  { path: '/', component: login },
  { path: '/login', component: login },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes,
})

export default router;