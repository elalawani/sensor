<template>
    <div class="left flex flex-col h-full border-r border-r-slate-500 w-full p-2">
        <div class="w-full bg-sky-700">
            <h1 class="flex justify-around text-[min(10vw,30px)] p-4">
                Fallbesprechung konsil
            </h1>
        </div>

        <select class="flex justify-end items-end py-2 my-1 rounded bg-sky-900 px-1 w-fit">
            <option value="">export</option>
            <option value="pdf">pdf</option>
            <option value="csv">csv</option>
            <option value="fhir">fhir</option>
        </select>
        <div
            v-for="caseReview in caseReviews"
            class="flex justify-start items-start">
            <table class="rounded text-sm text-left text-slate-500 dark:text-slate-100 w-full">
                <tbody>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        patient
                    </th>
                    <td class="pl-2 py-4">
                        {{caseReview.patient.last_name}},  {{caseReview.patient.first_name}}
                    </td>
                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-1/4">
                        added by
                    </th>
                    <td class="pl-2 py-4">
                        {{caseReview.created_by.name}}
                    </td>
                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-1/4">
                       Role
                    </th>
                    <td class="pl-2 py-4">
                        {{caseReview.documentation_role}}
                    </td>
                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        duration
                    </th>
                    <td class="pl-2 py-4">
                        {{caseReview.duration }}
                    </td>
                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        created at
                    </th>
                    <td class="pl-2 py-4">
                        {{caseReview.created_at}}
                    </td>
                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        code
                    </th>
                    <td class="pl-2 py-4">
                        {{ caseReview.code }}
                    </td>
                </tr>
                <tr
                    class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        participants
                    </th>
                    <td
                        v-for="name in caseReview.participants"
                        class="pl-2 py-4">
                        {{ name.name }}
                    </td>
                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        second visit required
                    </th>
                    <td class="pl-2 py-4">
                        {{ caseReview.second_visit_required }}
                    </td>
                </tr>

                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        discussed issues
                    </th>
                    <td class="pl-2 py-4">
                        {{ caseReview.discussed_issues }}
                    </td>
                </tr>

                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        specialist consultation required
                    </th>
                    <td class="pl-2 py-4">
                        {{ caseReview.specialist_consultation_required }}
                    </td>
                </tr>

                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        recommendations
                    </th>
                    <td class="pl-2 py-4">
                        {{ caseReview.recommendations }}
                    </td>
                </tr>

                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        recommendation issued
                    </th>
                    <td class="pl-2 py-4">
                        {{ caseReview.recommendation_issued }}
                    </td>
                </tr>
                <tr class="border dark:bg-slate-800 dark:border-slate-700">
                    <th class="pl-2 py-4 dark:bg-sky-700 w-fit">
                        note
                    </th>
                    <td class="pl-2 py-4">
                        {{ caseReview.patient.doctors }}
                        {{ caseReview.patient.nurses }}
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

const caseReviewNurseCouncil = useDocumentationsStore()

const fetchData = async () => {
    await caseReviewNurseCouncil.get_case_review_nurse_council()
}
onMounted(fetchData)

const caseReviews = computed(()=> caseReviewNurseCouncil.case_review_nurse_council)

</script>