<template>
    <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
        <h1 class="text-xl font-bold leading-tight tracking-tight md:text-2xl">
            add Temperature
        </h1>
        <form class="flex flex-col w-full" @submit.prevent="submitForm">
            <div class="flex flex-row items-center mb-8">
                <div class="flex flex-col w-4/5">
                    <label for="Temperature" class="block mb-2 text-sm font-medium ">Temperature</label>
                    <div class="flex flex-row items-center mr-12">
                        <input
                            type="number"
                            v-model="formData.Temperature"
                            name="Temperature"
                            id="Temperature"
                            class="border text-slate-50 border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block p-2.5
                            dark:bg-slate-700 dark:border-slate-600"
                            placeholder="Temperature">
                        <span class="text-slate-300 ml-2">
                            °C
                        </span>
                    </div>
                </div>

                <div class="ml-10 flex flex-col w-full">
                    <label for="status" class="block mb-2 text-sm font-medium pointer-events-none">status</label>
                    <input
                        type="text"
                        v-model="formData.status"
                        name="status"
                        id="status"
                        class="border pointer-events-none border-gray-300 sm:text-sm rounded-lg focus:border-sky-600
                        block p-2.5 dark:bg-slate-700 text-slate-500 dark:border-slate-600"
                        placeholder="Completed">
                </div>
            </div>
            <div class="flex flex-row w-full justify-around items-center">
                <div class="flex flex-col w-full">
                    <label for="code" class="block mb-2  text-sm font-medium pointer-events-none">code</label>
                    <input
                        type="text"
                        v-model="formData.code"
                        name="code"
                        id="code"
                        class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block
                            p-2.5 dark:bg-slate-700 text-slate-500 dark:border-slate-600 pointer-events-none"
                        placeholder="TMP001">

                </div>
                <div class="w-full flex-col flex">
                    <label for="category" class="block mb-2 text-sm font-medium pointer-events-none">category</label>
                    <input
                        type="text"
                        v-model="formData.category"
                        name="category"
                        id="category"
                        class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block
                        p-2.5 dark:bg-slate-700 text-slate-500 dark:border-slate-600 pointer-events-none"
                        placeholder="Temperature">
                </div>
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
import {useToastStore} from "@/stores/toast";
import router from "@/router";

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

        const currentPatient = computed(()=> store.patient)

        console.log(currentPatient.value)
        return {currentPatient, toastStore};
    },
    data() {
        return {
            formData: {
                "status": "Completed",
                "code": "TMP001",
                "category": "Temperature",
                "Temperature": '',
                "unit": "°C",
                "patient": this.currentPatient.id   // replace with the actual patient ID
            }
        }
    },
    methods: {
        submitForm() {
            axios.post('/api/sensor/temperature/', this.formData)
                .then(response => {
                    this.toastStore.showToast(
                                5000,
                                'measurement added',
                                'border border-green-500 bg-green-100 text-green-900'
                            )
                    console.log(response.data);
                    router.push({ path: `/patients/${this.currentPatient.id}/sensorData` })
                })
                .catch(error => {
                    console.error(error);
                });
        }
    }
}
</script>