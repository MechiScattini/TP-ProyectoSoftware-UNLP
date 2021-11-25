import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import IniciarSesion from '../views/IniciarSesion.vue'
import ZonasInundablesIndex from '../components/zonas-inundables/ZonasInundablesIndex.vue'
import ZonasInundablesShow from '../components/zonas-inundables/ZonasInundablesShow.vue'

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
    component: ZonasInundablesIndex
  },
  {
    path: '/zonas-inundables/ver/:id',
    name: 'zonas-inundables-ver',
    component: ZonasInundablesShow
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
