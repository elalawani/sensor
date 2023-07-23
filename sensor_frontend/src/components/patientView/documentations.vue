<template>
    <div class="container">
        <div
            class="container flex flex-row h-full"
        >
            <div v-if="dataView === 'examination' || dataView === ''">
                 <initial-examinations/>
            </div>
            <div v-if="dataView === 'wearables'">
                 <instruction-wearables/>
            </div>
            <div v-if="dataView === 'interview-telephones'">
                 <initial-interview-telephones/>
            </div>
            <div v-if="dataView === 'feedback'">
                 <feedback-care-team-telephone-consultation/>
            </div>
            <div v-if="dataView === 'equipment'">
                 <equipment/>
            </div>
            <div v-if="dataView === 'visit'">
                 <visit/>
            </div>
            <div v-if="dataView === 'processing'">
                 <data-review-processing/>
            </div>
            <div v-if="dataView === 'case-review'">
                 <case-review/>
            </div>
            <div v-if="dataView === 'case-review-council'">
                 <case-review-council/>
            </div>
            <div v-if="dataView === 'case-review-nurse-council'">
                 <case-review-nurse-council/>
            </div>
            <div v-if="dataView === 'telephone-consultation'">
                 <telephone-consultations/>
            </div>
            <div v-if="dataView === 'consultation'">
                 <consultation/>
            </div>

            <div class="right flex flex-col w-1/2 p-2">
                <div class="mb-16 space-y-2 flex flex-col items-center">
                    <router-link :to="`/patients/${id}/add_docu`" class="p-2 bg-sky-700 rounded">
                        add +
                    </router-link>
                </div>
                <div class="flex flex-col w-full h-96 overflow-auto">
                    <button
                        :class="dataView === 'examination'  || dataView === '' ? ' font-extrabold text-lg' : ''"
                        class="px-3 py-2 rounded bg-slate-600 m-1"
                        @click="dataView = 'examination'">
                        Initial Examinations
                    </button>
                    <button
                        :class="dataView === 'wearables' ? ' font-extrabold text-lg' : ''"
                        class="px-3 py-2 rounded bg-slate-600 m-1"
                        @click="dataView = 'wearables'">
                        Instruction wearables
                    </button>
                    <button
                        :class="dataView === 'interview-telephones' ? ' font-extrabold text-lg' : ''"
                        class="px-3 py-2 rounded bg-slate-600 m-1"
                        @click="dataView = 'interview-telephones'">
                        interview telephones
                    </button>
                    <button
                        :class="dataView === 'feedback' ? ' font-extrabold text-lg' : ''"
                        class="px-3 py-2 rounded bg-slate-600 m-1"
                        @click="dataView = 'feedback'">
                        feedback consultation
                    </button>
                    <button
                        :class="dataView === 'equipment' ? ' font-extrabold text-lg' : ''"
                        class="px-3 py-2 rounded bg-slate-600 m-1"
                        @click="dataView = 'equipment'">
                        equipment
                    </button>
                    <button
                        :class="dataView === 'visit' ? ' font-extrabold text-lg' : ''"
                        class="px-3 py-2 rounded bg-slate-600 m-1"
                        @click="dataView = 'visit'">
                        visit
                    </button>
                    <button
                        :class="dataView === 'processing' ? ' font-extrabold text-lg' : ''"
                        class="px-3 py-2 rounded bg-slate-600 m-1"
                        @click="dataView = 'processing'">
                        processing
                    </button>
                    <button
                        :class="dataView === 'case-review' ? ' font-extrabold text-lg' : ''"
                        class="px-3 py-2 rounded bg-slate-600 m-1"
                        @click="dataView = 'case-review'">
                        case review
                    </button>
                    <button
                        :class="dataView === 'case-review-council' ? ' font-extrabold text-lg' : ''"
                        class="px-3 py-2 rounded bg-slate-600 m-1"
                        @click="dataView = 'case-review-council'">
                        case review council
                    </button>
                    <button
                        :class="dataView === 'case-review-nurse-council' ? ' font-extrabold text-lg' : ''"
                        class="px-3 py-2 rounded bg-slate-600 m-1"
                        @click="dataView = 'case-review-nurse-council'">
                        case review nurse-council
                    </button>
                    <button
                        :class="dataView === 'telephone-consultation' ? ' font-extrabold text-lg' : ''"
                        class="px-3 py-2 rounded bg-slate-600 m-1"
                        @click="dataView = 'telephone-consultation'">
                        telephone consultation
                    </button>
                    <button
                        :class="dataView === 'consultation' ? ' font-extrabold text-lg' : ''"
                        class="px-3 py-2 rounded bg-slate-600 m-1"
                        @click="dataView = 'consultation'">
                        consultation
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import InitialExaminations from "@/components/patientView/documentation/fetchAll/initialExaminations.vue";
import InstructionWearables from "@/components/patientView/documentation/fetchAll/instructionWearables.vue";
import InitialInterviewTelephones from "@/components/patientView/documentation/fetchAll/initialInterviewTelephones.vue";
import FeedbackCareTeamTelephoneConsultation
    from "@/components/patientView/documentation/fetchAll/feedbackCareTeamTelephoneConsultation.vue";
import Equipment from "@/components/patientView/documentation/fetchAll/equipment.vue";
import Visit from "@/components/patientView/documentation/fetchAll/visit.vue";
import DataReviewProcessing from "@/components/patientView/documentation/fetchAll/dataReviewProcessing.vue";
import CaseReview from "@/components/patientView/documentation/fetchAll/caseReview.vue";
import CaseReviewCouncil from "@/components/patientView/documentation/fetchAll/caseReviewCouncil.vue";
import CaseReviewNurseCouncil from "@/components/patientView/documentation/fetchAll/caseReviewNurseCouncil.vue";
import TelephoneConsultations from "@/components/patientView/documentation/fetchAll/telephoneConsultations.vue";
import Consultation from "@/components/patientView/documentation/fetchAll/consultation.vue";
import {useRoute} from "vue-router";

export default {
    name: 'documentation',
    components: {
        Consultation,
        TelephoneConsultations,
        CaseReviewNurseCouncil,
        CaseReviewCouncil,
        CaseReview,
        DataReviewProcessing,
        Visit,
        Equipment,
        FeedbackCareTeamTelephoneConsultation,
        InitialInterviewTelephones,
        InstructionWearables,
        InitialExaminations
    },
    data() {
        return {
            dataView: '',
            id: useRoute().params.id,
        }
    },
}

</script>