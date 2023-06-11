<template>
  <div id="app">
      <navbar/>
  </div>
  <router-view/>

    1234
  <toast/>
</template>
<script>
import navbar from "../src/components/navbar.vue";
import toast from '../src/components/toast.vue'
export default {
    name: 'app',
    components: {
        navbar,
        toast,
    }
}
</script>