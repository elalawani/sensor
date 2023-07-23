<template>
    <div class="left flex flex-col h-full border-r border-r-slate-500 w-full p-2">
        <div class="w-full bg-sky-700">
            <h1 class="flex justify-around text-[min(10vw,30px)] p-4">
                Telefonische Konsultation des Patient
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
            <option v-for="(_, index) in telephoneConsultations"
                    :value="index"
                    :key="index"
            >
                go to page: {{index}}</option>
        </select>
       </div>
        <div
            v-for="(telephoneConsultation, index) in telephoneConsultations"
            class="flex justify-start items-start">
            <table
                v-if="index === selected"
                class="rounded text-sm text-left text-slate-500 dark:text-slate-100 w-full">
                <tbody>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        patient
                    </th>
                    <td class="pl-2 py-4">
                        {{telephoneConsultation.patient.last_name}},  {{telephoneConsultation.patient.first_name}}
                    </td>
                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-1/4">
                        added by
                    </th>
                    <td class="pl-2 py-4">
                        {{telephoneConsultation.created_by.name}}
                    </td>
                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-1/4">
                       Role
                    </th>
                    <td class="pl-2 py-4">
                        {{telephoneConsultation.documentation_role}}
                    </td>
                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        duration
                    </th>
                    <td class="pl-2 py-4">
                        {{telephoneConsultation.duration }}
                    </td>
                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        created at
                    </th>
                    <td class="pl-2 py-4">
                        {{telephoneConsultation.created_at}}
                    </td>
                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        code
                    </th>
                    <td class="pl-2 py-4">
                        {{ telephoneConsultation.code }}
                    </td>
                </tr>
                <tr
                    class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        consultation by
                    </th>
                    <td>
                        <div
                            v-for="name in telephoneConsultation.consultation_by"
                        class="pl-2 py-4">
                        {{ name.name }}
                        </div>
                    </td>
                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        consultation reason
                    </th>
                    <td class="pl-2 py-4">
                        {{ telephoneConsultation.consultation_reason }}
                    </td>
                </tr>

                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        conversation topics
                    </th>
                    <td class="pl-2 py-4">
                        {{ telephoneConsultation.conversation_topics }}
                    </td>
                </tr>

                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        recommendations
                    </th>
                    <td class="pl-2 py-4">
                        {{ telephoneConsultation.recommendations }}
                    </td>
                </tr>

                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        recommendations
                    </th>
                    <td class="pl-2 py-4">
                        {{ telephoneConsultation.recommendations }}
                    </td>
                </tr>

                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        recommendation issued
                    </th>
                    <td class="pl-2 py-4">
                        {{ telephoneConsultation.recommendation_issued }}
                    </td>
                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        others
                    </th>
                    <td class="pl-2 py-4">
                        {{ telephoneConsultation.others }}
                    </td>
                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        note
                    </th>
                    <td class="pl-2 py-4">
                        {{ telephoneConsultation.patient.doctors }}
                        {{ telephoneConsultation.patient.nurses }}
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

const telephoneConsultation = useDocumentationsStore()
const patient_id = useRoute().params.id

const fetchData = async () => {
    await telephoneConsultation.get_telephone_consultations(patient_id)
}
onMounted(fetchData)

const telephoneConsultations = computed(()=> telephoneConsultation.telephone_consultations)
const selected = ref(telephoneConsultations.value.length-1)

</script>