<template>
  <div id="app">
    <Overview/>
    <div class="container">
      <router-view/>
    </div>
  </div>
</template>

<script>
import Overview from '@/components/Overview'
export default {
  name: 'App',
  components: {
    Overview
  }
}
</script>

<style>
</style>
