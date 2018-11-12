import Vue from 'vue'
import Router from 'vue-router'
Vue.use(Router)
const routerOptions = [
  { path: '/', component: 'Navbar' },

]
const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => import(`@/components/${route.component}.vue`)
  }
})
export default new Router({
  routes,
  mode: 'history'
})
