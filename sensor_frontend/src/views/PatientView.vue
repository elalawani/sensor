<template>
  <div class="sm:mt-36 mt-16 flex flex-col-reverse sm:flex-row">
       <div class=" inset-x-0 bottom-0 backdrop-blur">
          <side-bar/>
      </div>
      <div class="sm:ml-36 bg-slate-200 text-slate-900 rounded sm:mr-5
      w-4/5 sm:fixed h-4/6 overflow-auto mb-16 sm:mb-0

">
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