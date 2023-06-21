<template>
  <div class="p-2">
      <div class="p-4 font-bold ">
          Medikation:
      </div>
      <div>
          {{patientInfo.medications}}
      </div>
      <div class="justify-between p-3 bg-gray-50 rounded shadow-lg">
          <table id="customers" class=" p-8  text-left">
              <thead class="text-gray-500">
              <tr>
                  <th>Firmenname</th>
                  <th>Name</th>
                  <th>strength</th>
                  <th>pack</th>
                  <th>form</th>
                  <th>hersteller</th>
              </tr>
              </thead>
              <tbody>
              <tr v-for="medications in patientInfo.medications" :key="medications.id">
                  <td>{{medications.name}}</td>
                  <td>Amoxicillin</td>
                  <td>150mg</td>
                  <td>20</td>
                  <td>tab</td>
                  <td>hersteller</td>
               </tr>
              </tbody>
          </table>
      </div>
  </div>
</template>
<script>
import {useRoute} from "vue-router";
import {usePatientStore} from "@/stores/patient";
import {computed, onMounted, ref, watch} from "vue";


export default {
  setup() {
    const route = useRoute();
    const store = usePatientStore();
    const id = ref(route.params.id);


    const fetchData = async () => {
      await store.getPatient(id.value);
    }

     watch(() => route.params.id, newId => {
      id.value = newId;
      fetchData();
    });

    onMounted(fetchData);

    const patientInfo = computed(()=> store.patient)

    return {patientInfo};
  },
};

</script>


<style>
#customers {
  width: 100%;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
}

#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #0489aa;
  color: white;
}
</style>