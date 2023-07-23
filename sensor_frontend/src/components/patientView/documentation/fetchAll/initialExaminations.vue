<template>
    <div class="left flex flex-col h-full border-r border-r-slate-500 w-full p-2">
        <div class="w-full bg-sky-700">
            <h1 class="flex justify-around text-[min(10vw,30px)] p-4">
                Eingangsuntersuchung in der Praxis/ Klinik
            </h1>
        </div>
       <div class="flex flex-row justify-between container px-4">
            <select class="flex justify-end items-end py-2 my-1 rounded bg-sky-900 px-1 w-fit">
            <option value="">export</option>
            <option value="pdf">pdf</option>
            <option value="csv">csv</option>
            <option value="fhir">fhir</option>
        </select>
        <select v-model="selected" class="flex justify-end items-end py-2 my-1 rounded bg-sky-900 px-1 w-fit">
            <option v-for="(_, index) in examinations"
                    :value="index"
                    :key="index"
            >
                go to page: {{index}}</option>
        </select>
       </div>
        <div
            v-for="(examination, index) in examinations"
            :key="index"
            class="flex justify-start items-start">
            <table
                v-if="index === selected"
                class="rounded text-sm text-left text-slate-500 dark:text-slate-100 w-full">
                <tbody>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-1/4">
                        added by
                    </th>
                    <td class="pl-2 py-4">
                        {{ examination.created_by.name }}
                    </td>
                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        duration
                    </th>
                    <td class="pl-2 py-4">
                        {{examination.duration}} {{ examination.duration }}
                    </td>
                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        created at
                    </th>
                    <td class="pl-2 py-4">
                        {{ examination.created_at }}
                    </td>
                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        praxis
                    </th>
                    <td class="pl-2 py-4">
                        {{ examination.centrePick }}
                    </td>
                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        note
                    </th>
                    <td class="pl-2 py-4">
                        {{ examination.note }}
                    </td>
                </tr>
                </tbody>
            </table>
        </div>
    </div>

</template>
<script setup>
import {useDocumentationsStore} from "@/stores/documentation";
import {computed, onMounted, ref} from "vue";
import {useRoute} from "vue-router";

const initialExamination = useDocumentationsStore()
const patient_id = useRoute().params.id

const fetchData = async () => {
    await initialExamination.get_initial_examinations(patient_id)
}
onMounted(fetchData)

const examinations = computed(()=> initialExamination.initial_examinations)
const selected = ref( examinations.value.length-1);


</script>