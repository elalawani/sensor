<template>
 hallo {{userStore.user.name}}
    <br>
 hallo {{userStore.user.email}}
    <br>
 hallo {{userStore.user.id}}
    <br>
  <div>
      reset my pass
  </div>
  <div>
      upload img
  </div>
  my todos:
  <div>
      123
  </div>
    <div>
      123
  </div>
my patients:

  <div v-for="patient in patientStore.patients">
      <div v-for="doctor in patient.doctors">
         <div v-if="doctor.id === userStore.user.id">
             {{ patient.first_name }}
         </div>
      </div>
  </div>

</template>
<script setup>
import {useUserStore} from "@/stores/user";
import {usePatientStore} from "@/stores/patient";

const userStore = useUserStore()
const patientStore = usePatientStore()

</script>