import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import IniciarSesion from '../views/IniciarSesion.vue'
import ZonasInundables from '../components/zonas-inundables/ZonasInundablesIndex.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/iniciar-sesion',
    name: 'iniciar-sesion',
    component: IniciarSesion
  },
  {
    path: '/zonas-inundables',
    name: 'zonas-inundables',
    component: ZonasInundables
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
