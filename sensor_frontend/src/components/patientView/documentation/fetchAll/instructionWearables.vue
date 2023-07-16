<template>
    <div class="left flex flex-col h-full border-r border-r-slate-500 w-full p-2">
        <div class="w-full bg-sky-700">
            <h1 class="flex justify-around text-[min(10vw,30px)] p-4">
                Instruktion in Wearable und App (57203A02)
            </h1>
        </div>
        <select class="flex justify-end items-end py-2 my-1 rounded bg-sky-900 px-1 w-fit">
            <option value="">export</option>
            <option value="pdf">pdf</option>
            <option value="csv">csv</option>
            <option value="fhir">fhir</option>
        </select>
        <div
            v-for="instructionWearable in instructionWearables"
            class="flex justify-start items-start">
            <table class="rounded text-sm text-left text-slate-500 dark:text-slate-100 w-full">
                <tbody>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        patient
                    </th>
                    <td
                        class="pl-2 py-4">
                        {{ instructionWearable.patient.last_name}},  {{ instructionWearable.patient.first_name}}
                    </td>
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        code
                    </th>
                    <td colspan="3"
                        class="pl-2 py-4">
                        {{ instructionWearable.code}}
                    </td>

                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-1/4">
                        added by
                    </th>
                    <td class="pl-2 py-4 flex flex-row">
                        {{instructionWearable.created_by.name}}
                    </td>
                    <th class="pl-2 py-4 dark:bg-sky-700 w-1/4">
                        role
                    </th>
                    <td class="pl-2 py-4">
                        {{instructionWearable.documentation_role}}
                    </td>
                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        duration
                    </th>
                    <td
                        colspan="3"
                        class="pl-2 py-4">
                        {{instructionWearable.duration}}
                    </td>
                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        created at
                    </th>
                    <td
                        colspan="3"
                        class="pl-2 py-4">
                        {{instructionWearable.created_at}}
                    </td>
                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        center
                    </th>
                    <td
                        colspan="3"
                        class="pl-2 py-4">
                        {{instructionWearable.centrePick}}
                    </td>
                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        note
                    </th>
                    <td colspan="3"
                        class="pl-2 py-4">
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

const instructionWearable = useDocumentationsStore()

const fetchData = async () => {
    await instructionWearable.get_instruction_wearables()
}
onMounted(fetchData)

const instructionWearables = computed(()=> instructionWearable.instruction_wearables)

</script>