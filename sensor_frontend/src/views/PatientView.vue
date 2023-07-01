<template>
  <div class="mt-8 mx-2 flex flex-col-reverse sm:flex-row">
      <div>
          <side-bar/>
      </div>
      <div class="sm:ml-36 border shadow-xl dark:border-none dark:bg-slate-700 text-slate-100 rounded sm:mr-5
      sm:w-4/5 w-full sm:fixed h-4/5 overflow-auto mb-16 sm:mb-0">
          <router-view></router-view>
      </div>

  </div>
</template>
<script>
import { usePatientStore } from '@/stores/patient'
import {useRoute} from "vue-router";
import sideBar from '@/components/sideBar.vue'
import {computed} from "vue";


export default {
    components:{
        sideBar
    },
    setup() {
        const route = useRoute();
        const id = computed(() => route.params.id);

        const patientStore = usePatientStore()
        patientStore.getPatient(id.value)

  }
}
</script>