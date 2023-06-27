<template>
    <div class="p-3">
        <div class="dark:text-slate-100 text-slate-900 tracking-tight whitespace-nowrap font-extrabold py-4 sm:text-4xl text-2xl my-8">
            Search or add Patient
        </div>
        <div class="flex justify-center items-center w-full mb-2 rounded-full p-2 bg-sky-700 dark:bg-sky-900 sm:hidden ">
                <router-link to="/add_patient">
                    <i>+</i>
                    add new patient
                </router-link>
        </div>
        <form @keyup.enter.prevent="applyFilter" class="dark:bg-slate-700 rounded-lg bg-gray-50 border  shadow-inner dark:border-0 dark:shadow-none">
            <div class="p-4">
                <input v-model="filters.byName" type="search" class="p-2 pl-3 w-full outline-none dark:bg-slate-500 rounded-lg dark:text-slate-100 mb-2 dark:placeholder-slate-100 border-2 dark:border-0 dark:shadow-none shadow-lg" placeholder="search name"/>
                <div class="flex flex-row justify-around mb-4">
                    <input v-model="filters.byBirthdate" type="date" class="p-2 pl-3 w-full outline-none dark:bg-slate-500 rounded-lg dark:text-slate-100 mb-2 mr-1 border-2 dark:border-0 dark:shadow-none shadow-lg"/>
                    <select v-model="filters.byType" class="p-2 pl-3 w-full outline-none dark:bg-slate-500 rounded-lg dark:text-slate-100 mb-2 mr-1 dark:placeholder-slate-100 border-2 dark:border-0 dark:shadow-none shadow-lg">
                        <option disabled selected value="">Select Type</option>
                        <option value="M">male</option>
                        <option value="F">Female</option>
                    </select>
                    <input v-model="filters.byCreator" type="search" class="p-2 pl-3 w-full outline-none dark:bg-slate-500 rounded-lg dark:text-slate-100 mb-2 mr-1 dark:placeholder-slate-100 border-2 dark:border-0 dark:shadow-none shadow-lg" placeholder="type"/>
                </div>
                <label class="dark:text-slate-100 text-xl">
                    filter by disease or chronic Conditions
                </label>

                <div class="flex flex-row justify-around my-3">
                     <multiselect
                                        v-model="filters.byMedications"
                                        :options="medications"
                                        :close-on-select="true"
                                        :searchable="true"
                                        class="p-2 pl-3 w-full outline-none dark:bg-slate-500 rounded-lg dark:text-slate-100 mb-2 mr-1 dark:placeholder-slate-100 border-2 dark:border-0 dark:shadow-none shadow-lg"
                                        placeholder="Select medication"
                                    />
                     <multiselect
                                        v-model="filters.byCondition"
                                        :options="chronic_conditions"
                                        :close-on-select="true"
                                        :searchable="true"
                                        class="p-2 pl-3 w-full outline-none dark:bg-slate-500 rounded-lg dark:text-slate-100 mb-2 mr-1 dark:placeholder-slate-100 border-2 dark:border-0 dark:shadow-none shadow-lg"
                                        placeholder="Select Condition"
                                    />
                </div>
                <label class="dark:text-slate-100 text-xl">
                    filter by doctor or nurse
                </label>

                <div class="flex flex-row justify-around mt-3">
                    <multiselect
                                        v-model="filters.byDoctor"
                                        :options="doctors"
                                        :close-on-select="true"
                                        :searchable="true"
                                        class="p-2 pl-3 w-full outline-none dark:bg-slate-500 rounded-lg dark:text-slate-100 mb-2 mr-1 dark:placeholder-slate-100 border-2 dark:border-0 dark:shadow-none shadow-lg"
                                        placeholder="Select doctor"
                                    />
                     <multiselect
                                        v-model="filters.byNurse"
                                        :options="nurses"
                                        :close-on-select="true"
                                        :searchable="true"
                                        class="p-2 pl-3 w-full outline-none dark:bg-slate-500 rounded-lg dark:text-slate-100 mb-2 mr-1 dark:placeholder-slate-100 border-2 dark:border-0 dark:shadow-none shadow-lg"
                                        placeholder="Select nurse"
                                    />
                </div>
            </div>
        </form>
        <div class="flex justify-between items-center text-slate-50 mx-2 my-4">
            <div class="w-fit font-bold sm:rounded-2xl rounded-full p-2 bg-sky-700 dark:bg-sky-900 justify-items-end hidden sm:inline">
                <router-link to="/add_patient">
                    <i>+</i>
                        add new patient
                </router-link>
            </div>
            <div class="flex space-x-4 justify-end">
                <button @click="applyFilter" class="flex dark:bg-slate-700 bg-slate-500 p-2 rounded-2xl px-4">
                    <span class="mr-1">filter</span> <search/>
                </button>
                <button @click="removeFilter" class="flex dark:bg-slate-700 bg-slate-500 p-2 rounded-2xl px-2">
                    <span class="mr-1">refresh</span> <search/>
                </button>
            </div>
        </div>

    </div>

    <div
        class="flex w-full flex-row items-center mt-10"
        v-for="(patient, index) in patients"
        :key="index"
    >
        <div class="flex w-full flex-row sm:space-x-10 pr-4">
            <div class="p-10 items-center border-r border-r-slate-500 hidden sm:inline">
                <i class="py-4 ml-auto px-5 text-gray-300 border border-slate-300 rounded-full text-4xl">
                    <font-awesome-icon icon="fa-solid fa-user" />
                </i>
            </div>
            <div class="flex px-10 py-2 rounded-lg flex-row justify-between sm:dark:hover:bg-slate-800 dark:bg-slate-800 ml-4 sm:ml-0 sm:dark:bg-slate-900
            dark:hover:shadow-none dark:border-0 hover:border-t hover:shadow-xl ease-in transition-all duration-100 items-center w-full">
                <div class="">
                    <div class="dark:text-slate-100 font-bold text-2xl">
                        {{patient.last_name}}, {{patient.first_name}}
                    </div>
                    <div class="my-2">
                        <span class="text-slate-100">born on:</span> {{patient.date_of_birth}}
                    </div>
                    <div
                        v-if="patient.gender === 'M'"
                         class="font-extrabold">
                        MALE
                    </div>
                    <div v-else class="font-extrabold">
                        FEMALE
                    </div>
                    <div>
                        date of creation
                    </div>
                    <div class="text-sky-500 hover:text-sky-300 hover:dark:text-sky-500 dark:text-sky-700 flex flex-row m-4 mb-0">
                        <router-link :to="`patients/${patient.id}/info`">
                        more information
                        <font-awesome-icon icon="fa-solid fa-arrow-right" />
                    </router-link>
                    </div>
                </div>
                <div class="mr-10">
                  <div class="mb-2 pb-1 border-b border-b-slate-500">
                        <div class="font-bold">
                        Doctors:
                    </div>
                    <div
                        v-for="(doctors, index) in patient.doctors"
                        :key="index"
                    >
                        <router-link to="/" class="dark:hover:text-sky-500 dark:text-sky-700 text-sky-500 hover:text-sky-300 ml-10">
                            {{doctors.name}}
                        </router-link>

                    </div>
                  </div>
                    <div class="mt-1">
                       <div class="font-bold">
                            nurses:
                       </div>
                    <div
                        v-for="(nurses, index) in patient.nurses"
                        :key="index"
                    >
                        <router-link to="/" class="dark:hover:text-sky-500 dark:text-sky-700 text-sky-500 hover:text-sky-300  ml-10">
                            {{nurses.name}}
                        </router-link>

                    </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>

import Search from "@/components/svgs/search.vue";
import {usePatientStore} from "@/stores/patient";
import {computed, onMounted, ref} from "vue";
import axios from "axios";
import Multiselect from "@vueform/multiselect";

export default {
    name: 'PatientListView',
    setup() {
        const patientStore = usePatientStore()

        const filters = ref({
            byName: '',
            byBirthdate: '',
            byType: '',
            byCreator: '',
            byMedications: '',
            byCondition: '',
            byDoctor: '',
            byNurse: '',
        })

        const applyFilter = async () => {
            patientStore.updateFilters(filters.value);
            await patientStore.getPatients();
        };

        const removeFilter = async () => {
            filters.value = {
                byName: '',
                byBirthdate: '',
                byType: '',
                byCreator: '',
                byMedications: '',
                byCondition: '',
                byDoctor: '',
                byNurse: '',
            }
            patientStore.updateFilters(filters.value);
            await patientStore.getPatients();
            window.location.reload()
        };

        onMounted(() => {
            patientStore.getPatients()
        })

        const patients = computed(() => patientStore.patients)

        return {
            patients,
            filters,
            applyFilter,
            removeFilter
        }
    },
    components: {Multiselect, Search},
    data() {
        return {
            doctors: [],
            selectedDoctor: null,
            nurses: [],
            selectedNurse: null,
            medications: [],
            selectedMedication: null,
            chronic_conditions: [],
            selectedCondition: null,
        }
    },

     async mounted() {
    const response_doctors = await axios.get('/api/doctors/');
    this.doctors = response_doctors.data.map(doctors => ({
        value: doctors.name,
        label: doctors.name
    }));

    const response_nurses = await axios.get('/api/nurses/');
    this.nurses = response_nurses.data.map(nurses => ({
        value: nurses.name,
        label: nurses.name
    }));


    const response_conditions = await axios.get('/api/patients/chronic_conditions/');
    this.chronic_conditions = response_conditions.data.map(chronicConditions => ({
        value: chronicConditions.name,
        label: chronicConditions.name
    }));

    console.log(response_conditions)


    const response_medications = await axios.get('/api/patients/medications/');
    this.medications = response_medications.data.map(medications => ({
        value: medications.name,
        label: medications.name
    }));

         console.log(response_medications)
         await this.$nextTick(() => {
             const elements1 = document.querySelectorAll('.multiselect-search');
             const elements2 = document.querySelectorAll('.multiselect-dropdown');
             const elements3 = document.querySelectorAll('.multiselect-option.is-selected');
             elements1.forEach((element) => {
                 element.style.backgroundColor = "#333";
                 element.style.color = "#f5f5f5";
             });
             elements2.forEach((element) => {
                 element.style.backgroundColor = "#333";
                 element.style.color = "#f5f5f5";
             });
             elements3.forEach((element) => {
                 element.style.backgroundColor = "#333";
                 element.style.color = "#f5f5f5";
             });
         });

  },
}


</script>
<style>
.parent >>> .child {

.multiselect-search {
    background: red !important;
}
    .multiselect__dropdown {
  background-color: red;
}

/* Changing the font color and size of the selected item */
.multiselect__single {
  color: #333;
  font-size: 16px;
}

/* Changing the color of the tags */
.multiselect__tag {
  background-color: #333;
  color: #f5f5f5;
}



}
</style>
