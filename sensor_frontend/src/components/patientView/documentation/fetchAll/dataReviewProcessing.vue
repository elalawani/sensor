<template>
    <div class="left flex flex-col h-full border-r border-r-slate-500 w-full p-2">
        <div class="w-full bg-sky-700">
            <h1 class="flex justify-around text-[min(10vw,30px)] p-4">
                Datensichtung, Beurteilung & Aufbereitung
            </h1>
        </div>
        <select class="flex justify-end items-end py-2 my-1 rounded bg-sky-900 px-1 w-fit">
            <option value="">export</option>
            <option value="pdf">pdf</option>
            <option value="csv">csv</option>
            <option value="fhir">fhir</option>
        </select>
        <div
            v-for="data in dataProcessing"
            class="flex justify-start items-start">
            <table class="rounded text-sm text-left text-slate-500 dark:text-slate-100 w-full">
                <tbody>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        patient
                    </th>
                    <td class="pl-2 py-4">
                        {{data.patient.last_name}},  {{data.patient.first_name}}
                    </td>
                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-1/4">
                        added by
                    </th>
                    <td class="pl-2 py-4">
                        {{data.created_by.name}}
                    </td>
                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-1/4">
                       Role
                    </th>
                    <td class="pl-2 py-4">
                        {{data.documentation_role}}
                    </td>
                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        duration
                    </th>
                    <td class="pl-2 py-4">
                        {{data.duration }}
                    </td>
                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        created at
                    </th>
                    <td class="pl-2 py-4">
                        {{data.created_at}}
                    </td>
                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        code
                    </th>
                    <td class="pl-2 py-4">
                        {{ data.code }}
                    </td>
                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        duration month
                    </th>
                    <td class="pl-2 py-4">
                        {{ data.duration_month }}
                    </td>
                </tr>

                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        note
                    </th>
                    <td class="pl-2 py-4">
                        {{ data.patient.doctors }}
                        {{ data.patient.nurses }}
                    </td>
                </tr>
                </tbody>
            </table>
        </div>
    </div>

</template>
<script setup>
import {useDocumentationsStore} from "@/stores/documentation";
import {computed, onMounted} from "vue";

const dataReviewProcessing = useDocumentationsStore()

const fetchData = async () => {
    await dataReviewProcessing.get_data_review_processing()
}
onMounted(fetchData)

const dataProcessing = computed(()=> dataReviewProcessing.data_review_processing)

</script>