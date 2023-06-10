<template>
  <div id="app">
      <navbar/>
  </div>
  <router-view/>
</template>
<script>
import navbar from "../src/components/navbar.vue";
export default {
    name: 'app',
    components: {
        navbar
    }
}
</script>