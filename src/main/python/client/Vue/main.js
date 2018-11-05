// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from '../../../../../../../OneDrive - tgm - Die Schule der Technik/Schule/5BHIT/Sew/vuejs-crud-master/vuejs-crud-master/src/router/index'

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
