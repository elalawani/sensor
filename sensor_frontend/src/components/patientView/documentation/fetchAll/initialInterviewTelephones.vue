<template>
    <div class="left flex flex-col h-full border-r border-r-slate-500 w-full p-2">
        <div class="w-full bg-sky-700">
            <h1 class="flex justify-around text-[min(10vw,30px)] p-4">
                Eingangsgespräch mit Patient via Telefon
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
            <option v-for="(_, index) in initialInterviewTelephones"
                    :value="index"
                    :key="index"
            >
                go to page: {{index}}</option>
        </select>
       </div>
        <div
            v-for="(initialInterviewTelephone, index) in initialInterviewTelephones"
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
                        {{initialInterviewTelephone.created_by.name}}
                    </td>
                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-1/4">
                       Role
                    </th>
                    <td class="pl-2 py-4">
                        {{initialInterviewTelephone.documentation_role}}
                    </td>
                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        duration
                    </th>
                    <td class="pl-2 py-4">
                        {{initialInterviewTelephone.duration }}
                    </td>
                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        created at
                    </th>
                    <td class="pl-2 py-4">
                        {{initialInterviewTelephone.created_at}}
                    </td>
                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        code
                    </th>
                    <td class="pl-2 py-4">
                        {{ initialInterviewTelephone.code }}
                    </td>
                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        conversation reason
                    </th>
                    <td class="pl-2 py-4">
                        {{ initialInterviewTelephone.conversation_reason }}
                    </td>
                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        note
                    </th>
                    <td class="pl-2 py-4">
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

const initialInterviewTelephone = useDocumentationsStore()
const patient_id = useRoute().params.id

const fetchData = async () => {
    await initialInterviewTelephone.get_initial_interview_telephones(patient_id)
}
onMounted(fetchData)

const initialInterviewTelephones = computed(()=> initialInterviewTelephone.initial_interview_telephones)
const selected = ref(initialInterviewTelephones.value.length-1)

</script>