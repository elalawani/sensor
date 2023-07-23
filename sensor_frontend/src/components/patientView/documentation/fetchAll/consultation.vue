<template>
    <div class="left flex flex-col h-full border-r border-r-slate-500 w-full p-2">
        <div class="w-full bg-sky-700">
            <h1 class="flex justify-around text-[min(10vw,30px)] p-4">
                Konsultation der/ des Patient
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
            <option v-for="(_, index) in consultations"
                    :value="index"
                    :key="index"
            >
                go to page: {{index}}</option>
        </select>
       </div>
        <div
            v-for="(consultation, index) in consultations"
            class="flex justify-start items-start">
            <table
                v-if="index === selected"
                class="rounded text-sm text-left text-slate-500 dark:text-slate-100 w-full">
                <tbody>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        patient
                    </th>
                    <td
                        class="pl-2 py-4">
                        {{ consultation.patient.last_name}},  {{ consultation.patient.first_name}}
                    </td>
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        code
                    </th>
                    <td colspan="3"
                        class="pl-2 py-4">
                        {{ consultation.code}}
                    </td>

                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-1/4">
                        added by
                    </th>
                    <td class="pl-2 py-4 flex flex-row">
                        {{consultation.created_by.name}}
                    </td>
                    <th class="pl-2 py-4 dark:bg-sky-700 w-1/4">
                        role
                    </th>
                    <td class="pl-2 py-4">
                        {{consultation.documentation_role}}
                    </td>
                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        duration
                    </th>
                    <td
                        colspan="3"
                        class="pl-2 py-4">
                        {{consultation.duration}}
                    </td>
                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        created at
                    </th>
                    <td
                        colspan="3"
                        class="pl-2 py-4">
                        {{consultation.created_at}}
                    </td>
                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        doctor initials
                    </th>
                    <td
                        colspan="3"
                        class="pl-2 py-4">
                        {{consultation.doctor_initials}}
                    </td>
                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        decisions
                    </th>
                    <td
                        colspan="3"
                        class="pl-2 py-4">
                        {{consultation.decisions}}
                    </td>
                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        reason for admission
                    </th>
                    <td
                        colspan="3"
                        class="pl-2 py-4">
                        {{consultation.reason_for_admission}}
                    </td>
                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        hospital admission required
                    </th>
                    <td
                        v-if="consultation.hospital_admission_required === true"
                        class="pl-2 py-4">
                        Yes
                    </td>
                    <td v-else
                        class="pl-2 py-4"
                    >
                        No
                    </td>
                     <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        clinic appointment required
                    </th>
                    <td
                        v-if="consultation.clinic_appointment_required === true"
                        class="pl-2 py-4">
                        Yes
                    </td>
                    <td
                        v-else
                        class="pl-2 py-4">
                        No
                    </td>
                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        reason for clinic appointment
                    </th>
                    <td
                        colspan="3"
                        class="pl-2 py-4">
                        {{consultation.reason_for_clinic_appointment}}
                    </td>
                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        measures after appointment
                    </th>
                    <td
                        colspan="3"
                        class="pl-2 py-4">
                        {{consultation.measures_after_appointment}}
                    </td>
                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        measures taken
                    </th>
                    <td
                        colspan="3"
                        class="pl-2 py-4">
                        {{consultation.measures_taken}}
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
import {computed, onMounted, ref} from "vue";
import {useRoute} from "vue-router";

const consultation = useDocumentationsStore()
const patient_id = useRoute().params.id

const fetchData = async () => {
    await consultation.get_consultation(patient_id)
}
onMounted(fetchData)

const consultations = computed(()=> consultation.consultation)
let selected = ref(consultations.value.length-1)

</script>