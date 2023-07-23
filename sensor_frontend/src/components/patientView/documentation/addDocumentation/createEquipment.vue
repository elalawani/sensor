<template>
         <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
        <h1 class="text-xl font-bold leading-tight tracking-tight md:text-2xl">
            Equipment
        </h1>
        <form class="flex flex-col w-full" @submit.prevent="submitForm">

            <div class="mb-5">
                add Equipment for patient
                <span class="font-bold">
                    {{ currentPatient.last_name }},  {{ currentPatient.first_name }}
                </span>
            </div>
            <div class="flex flex-row items-center mb-8">
                <div class="flex flex-col w-4/5">
                    <label for="blood_cholesterol" class="block mb-2 text-sm font-medium ">equipment</label>
                    <div class="flex flex-row items-center mr-12">
                        <input
                            type="text"
                            v-model="form.equipment"
                            name="blood_cholesterol"
                            id="blood_cholesterol"
                            class="border text-slate-50 border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block p-2.5
                            dark:bg-slate-700 dark:border-slate-600"
                            placeholder="minuten">
                    </div>
                </div>

                <div class="ml-10 flex flex-col w-full">
                    <label for="created_at" class="block mb-2 text-sm font-medium">created_at</label>
                    <input
                        type="date"
                        v-model="form.created_at"
                        name="created_at"
                        id="created_at"
                        class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600
                        block p-2.5 dark:bg-slate-700 text-slate-500 dark:border-slate-600"
                        placeholder="code">
                </div>
                <div class="ml-10 flex flex-col w-full">
                    <label for="removed_at" class="block mb-2 text-sm font-medium">removed_at</label>
                    <input
                        type="date"
                        v-model="form.removed_at"
                        name="removed_at"
                        id="removed_at"
                        class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600
                        block p-2.5 dark:bg-slate-700 text-slate-500 dark:border-slate-600"
                        placeholder="code">
                </div>
            </div>
                    <div class="flex flex-col w-full">
                        <label for="status" class="block mb-2 text-sm font-medium">note</label>
                        <textarea
                                type="text"
                                v-model="form.note"
                                name="status"
                                id="status"
                                class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600
                        block p-2.5 dark:bg-slate-700 text-slate-500 dark:border-slate-600"
                                placeholder="code">
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
import {computed, onMounted, ref} from "vue";
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
            form: {
                patient: this.currentPatient.id,
                equipment: '',
                created_at: '',
                removed_at: '',
                note: '',

            }
        }
    },
    methods: {
        submitForm() {
            console.log(this.form)
            axios.post('/api/documentation/equipment/create/', this.form)
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
}
</script>