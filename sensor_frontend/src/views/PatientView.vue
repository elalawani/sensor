<template>
  <div class="mt-36 flex flex-row">
      {{ patient }}
      <div>
      </div>
  </div>
</template>
<script setup>
import { usePatientStore } from '@/stores/patient'
import {useRoute} from "vue-router";

const patientStore = usePatientStore()

patientStore.getPatient()

const patient = patientStore.patients.find(x => x.id === (useRoute().params.id))


</script>