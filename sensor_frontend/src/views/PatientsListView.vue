<template>
  <div class="p-3 mt-24">
      <div class="bg-gray-50 border dark:border-sky-500 rounded-lg">
              <div class="p-4 flex items-center">
                  <input v-model="searchTerm" type="search" class="p-2 w-full border rounded-lg text-slate-900" placeholder="search"/>
                  <a href="#" class="py-3 px-4 hover:bg-sky-800 bg-slate-200 text-sky-800 hover:text-slate-200 rounded-full mx-3">
                      <font-awesome-icon icon="fa-solid fa-search" />
                  </a>
              </div>
          <div class="text-slate-900 p-2 pt-1 ml-4 hover:text-sky-800">
              <router-link to="add_patient">
                  <i>+</i> add new patient
              </router-link>
          </div>
       </div>
  </div>

  <div v-for="patient in filteredPatients" :key="patient.id">
      <router-link to="/">
         <div class="items-center m-10 hover:cursor-pointer relative">
             <div class="flex items-center px-2 bg-gray-50 rounded-lg mb-2 relative
                        shadow shadow-slate-400 hover:shadow-lg hover:shadow-gray-200">
                 <i class="py-4 px-5 text-gray-900 bg-slate-200 rounded-full text-4xl">
                     <font-awesome-icon icon="fa-solid fa-user" />
                 </i>
                 <div class="text-slate-900 p-8">
                     <strong>{{patient.first_name}} {{patient.last_name}}</strong><br>
                     <span class="text-gray-400">{{patient.date_of_birth}}</span>
                 </div>
                 <i v-if="patient.gender === 'M'" class="py-4 px-6 text-gray-900 bg-slate-200 rounded-full text-4xl absolute right-10 -top-10">
                     <font-awesome-icon icon="fa-solid fa-male" />
                 </i>
                  <i v-else class="py-4 px-6 text-gray-900 bg-slate-200 rounded-full text-4xl absolute right-10 -top-10">
                     <font-awesome-icon icon="fa-solid fa-female" />
                 </i>
                 <div class="bg-sky-800 absolute px-3 py-1 bottom-[-1px] right-[-1px] text-gray-50 rounded-br-lg rounded-tl-lg">
                     <font-awesome-icon icon="fa-solid fa-arrow-right" />
                 </div>
             </div>
         </div>
     </router-link>
  </div>

</template>
<script>

import axios from "axios";

export default {
    name: 'PatientListView',
    data() {
        return {
            searchTerm: '',
            patients: []
        }
    },
    mounted() {
        this.getPatient()
    },
    methods: {
        getPatient() {
            axios
                .get('/api/patients/')
                .then(response => {
                    console.log('data', response.data)
                    this.patients = response.data
                })
                .catch(error => {
                    console.log('error', error)
                })
        }
    },
    computed: {
        filteredPatients() {
            const searchTerm = this.searchTerm.toLowerCase();
            return this.patients.filter(patient => {
                const fullName = `${patient.first_name} ${patient.last_name}`.toLowerCase();
                return fullName.includes(searchTerm);
            });
        }
    },

}
</script>