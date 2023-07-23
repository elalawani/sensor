<template>
    <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
        <h1 class="text-xl font-bold leading-tight tracking-tight md:text-2xl">
            review
        </h1>
             <form class="flex flex-col w-full" @submit.prevent="submitForm">
                 <div class="mb-5">
                     add review for patient
                     <span class="font-bold">
                         {{ currentPatient.last_name }},  {{ currentPatient.first_name }}
                     </span>
                 </div>
                 <div class="flex items-center mb-8">
                     <div class="flex flex-col w-4/5">
                         <label for="duration" class="block mb-2 text-sm font-medium ">Dauer in min</label>
                         <div class="flex flex-row items-center mr-12">
                             <input
                                 type="number"
                                 v-model="form.duration"
                                 name="duration"
                                 id="duration"
                                 class="border text-slate-50 border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block p-2.5
                            dark:bg-slate-700 dark:border-slate-600"
                                 placeholder="minuten">
                             <span class="text-slate-300 ml-2">
                                 min
                             </span>
                         </div>
                     </div>
                     <div class="ml-10 flex flex-col w-full">
                         <label for="code" class="block mb-2 text-sm font-medium">code</label>
                         <input
                             type="text"
                             v-model="form.code"
                             name="code"
                             id="code"
                             class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600
                        block p-2.5 dark:bg-slate-700 text-slate-500 dark:border-slate-600"
                             placeholder="code">
                     </div>
                 </div>
                 <div class="flex flex-row justify-around items-center space-x-3">
                     <div class="w-full flex-col flex">
                         <label for="anamnese_discussed" class="block mb-2 text-sm font-medium">anamnese discussed</label>
                         <input
                             type="text"
                             v-model="form.anamnese_discussed"
                             name="anamnese_discussed"
                             id="anamnese_discussed"
                             class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block
                        p-2.5 dark:bg-slate-700 text-slate-500 dark:border-slate-600"
                             placeholder="anamnese_discussed">
                     </div>
                 </div>
                 <div class="flex flex-row justify-around items-center space-x-3">
                     <div class="w-full flex-col flex">
                         <label for="discussed_issues" class="block mb-2 text-sm font-medium">discussed issues</label>
                         <input
                             type="text"
                             v-model="form.discussed_issues"
                             name="discussed_issues"
                             id="discussed_issues"
                             class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block
                        p-2.5 dark:bg-slate-700 text-slate-500 dark:border-slate-600"
                             placeholder="issues">
                     </div>
                 </div>
                 <div class="mt-10 flex flex-row justify-around items-center space-x-3">
                     <div class="flex flex-col w-full">
                         <label class="block mb-2 text-sm font-medium ">second visit required</label>
                         <div class="flex flex-row items-center mr-12">
                             <input
                                     type="radio"
                                     value="false"
                                     id="no"
                                     v-model="form.second_visit_required">
                             <label
                                     class="mx-3"
                                     for="no"
                             >No</label>
                             <input
                                     type="radio"
                                     value="true"
                                     id="yes"
                                     v-model="form.second_visit_required">
                             <label
                                     class="mx-3"
                                     for="Yes">Yes</label>
                         </div>
                     </div>
                 </div>
                 <div class="mt-10 flex flex-row justify-around items-center space-x-3">
                     <div class="flex flex-col w-full">
                         <label class="block mb-2 text-sm font-medium ">specialist consultation required</label>
                         <div class="flex flex-row items-center mr-12">
                             <input
                                     type="radio"
                                     value="false"
                                     id="no"
                                     v-model="form.specialist_consultation_required">
                             <label
                                     class="mx-3"
                                     for="no"
                             >No</label>
                             <input
                                     type="radio"
                                     value="true"
                                     id="yes"
                                     v-model="form.specialist_consultation_required">
                             <label
                                     class="mx-3"
                                     for="Yes">Yes</label>
                         </div>
                     </div>
                 </div>
                 <div class="mt-10">
                     <div class="flex flex-row justify-between space-x-3">
                         <div class="w-full flex-col flex">
                         <label for="participants" class="block mb-2 text-sm font-medium ">participants</label>
                         <div>
                             <multi-select
                                 v-model="form.participants"
                                 :options="allParticipants"
                                 mode="tags"
                                 :close-on-select="false"
                                 :searchable="true"
                                 class="text-sky-800"
                                 placeholder="Select participants"
                             />
                         </div>
                     </div>
                     </div>
                 </div>
                 <div class="w-full flex-col flex">
                     <label for="category" class="block mb-2 text-sm font-medium">recommendations</label>
                     <input
                         type="text"
                         v-model="form.recommendations"
                         name="category"
                         id="category"
                         class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block
                        p-2.5 dark:bg-slate-700 text-slate-500 dark:border-slate-600"
                         placeholder="recommendations">
                 </div>
                 <div class="mt-10 flex flex-row justify-between space-x-3">
                     <div class="w-full flex-col flex">
                         <label for="category" class="block mb-2 text-sm font-medium">recommendation issued</label>
                         <input
                             type="text"
                             v-model="form.recommendation_issued"
                             name="category"
                             id="category"
                             class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block
                        p-2.5 dark:bg-slate-700 text-slate-500 dark:border-slate-600"
                             placeholder="recommendation_issued">
                     </div>
                 </div>
                 <div class="w-full flex-col flex mt-10">
                     <label for="note" class="block mb-2 text-sm font-medium">note</label>
                     <textarea
                         type="text"
                         v-model="form.note"
                         name="note"
                         id="note"
                         class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block
                        p-2.5 dark:bg-slate-700 text-slate-500 dark:border-slate-600"
                         placeholder="note">
                     </textarea>
                 </div>
             </form>
        <button
            @click="submitForm"
            class="px-5 py-3 dark:bg-sky-900 bg-sky-700 hover:bg-sky-500 dark:hover:bg-sky-700
                text-slate-50 w-fit rounded-xl">
            send
        </button>
    </div>
</template>
<script>
import axios from "axios";
import {usePatientStore} from "@/stores/patient";
import {useRoute} from "vue-router";
import {computed, onMounted, ref, watch} from "vue";
import router from "@/router";
import {useToastStore} from "@/stores/toast";

export default {
    setup() {
        const route = useRoute();
        const store = usePatientStore();
        const id = ref(route.params.id);
        const toastStore = useToastStore();


        const fetchData = async () => {
            await store.getPatient(id.value);
        }


        onMounted(fetchData);

        const currentPatient = computed(() => store.patient)

        console.log(currentPatient.value)
        return {currentPatient, toastStore};
    },
    data() {
        return {
            allParticipants: [],
            form: {
                patient: this.currentPatient.id,
                duration: '',
                code: '',
                participants: [],
                anamnese_discussed: '',
                recommendations: '',
                recommendation_issued: '',
                specialist_consultation_required: false,
                second_visit_required: false,
                discussed_issues: '',
                note: '',

            }
        }
    },
    methods: {
        submitForm() {
            console.log(this.form)
            axios.post('/api/documentation/case_review_nurse_council/create/', this.form)
                .then(response => {
                    this.toastStore.showToast(
                        5000,
                        'measurement added',
                        'border border-green-500 bg-green-100 text-green-900'
                    )
                    console.log(response.data)
                    router.push({path: `/patients/${this.currentPatient.id}/documentations`})
                })
                .catch(error => {
                    if (error.response) {
                        // The request was made and the server responded with a status code
                        // that falls out of the range of 2xx
                        console.error('Data:', error.response.data);
                        console.error('Status:', error.response.status);
                        console.error('Headers:', error.response.headers);
                    } else if (error.request) {
                        // The request was made but no response was received
                        // `error.request` is an instance of XMLHttpRequest in the browser
                        console.error('No response received:', error.request);
                    } else {
                        // Something happened in setting up the request that triggered an Error
                        console.error('Error', error.message);
                    }
                });
        }
    },
    async mounted() {
        const response_doctors = await axios.get('/api/doctors/');
        this.allParticipants = response_doctors.data.map(doctors => ({
            value: doctors.id,
            label: doctors.name
        }));

    },
}
</script>