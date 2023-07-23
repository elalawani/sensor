<template>
    <div class="p-5">
        <router-link :to="`/patients/${id}/documentations`"
                     class="font-extralight hover:text-sky-600"
        >
            &lt all documentations
        </router-link>
         <div
                class="flex justify-center p-6 items-center"
        >
            <h1 class="text-4xl">
                please select the type of the document
            </h1>
        </div>

        <div class="flex overflow-scroll space-x-3">
            <button
                v-for="(myOption, index) in options"
                :key="index"
                :class="option === myOption ? 'border-b border-b-sky-500 text-sky-500' : 'bg-slate-600'"
                class="p-4 rounded shadow-xl h-20"
                @click="option = myOption"
        >
                {{ myOption }}
            </button>
       </div>
    </div>
    <div v-if="option === 'Fallbesprechung'">
        <create-case-review />
    </div>
    <div v-else-if="option === 'Eingangsuntersuchung'">
        <create-initial-examination />
    </div>
    <div v-else-if="option === 'Wearable'">
        <create-instruction-wearable />
    </div>
    <div v-else-if="option === 'Eingangsgespräch'">
        <create-initial-interview-telephone />

    </div>
    <div v-else-if="option === 'Rückmeldung'">
        <create-feedback-care-team-telephone-consultation />
    </div>
    <div v-else-if="option === 'equipment'">
        <create-equipment />

    </div>
    <div v-else-if="option === 'hausebesuch'">
        <creat-visit />

    </div>
    <div v-else-if="option === 'processing'">
        <create-data-review-processing />

    </div>
    <div v-else-if="option === 'Fallbesprechung-konsil'">
        <creat-case-review-council />
    </div>
    <div v-else-if="option === 'Fallbesprechung-nurse-konsil'">
        <create-case-review-nurse-council />
    </div>
    <div v-else-if="option === 'Konsultation'">
        <create-consultation />
    </div>
    <div v-else-if="option === 'Telefonische-Konsultation'">
        <create-telephone-consultation />
    </div>
    <div v-else >
        <h1 class="container flex mt-10 justify-center m-auto text-7xl font-extrabold">
            nothing Selected
        </h1>
    </div>

</template>
<script>
import CreateCaseReview from "@/components/patientView/documentation/addDocumentation/createCaseReview.vue";
import CreateInitialExamination
    from "@/components/patientView/documentation/addDocumentation/createInitialExamination.vue";
import CreateInstructionWearable
    from "@/components/patientView/documentation/addDocumentation/createInstructionWearable.vue";
import CreateCaseReviewNurseCouncil
    from "@/components/patientView/documentation/addDocumentation/createCaseReviewNurseCouncil.vue";
import CreatCaseReviewCouncil from "@/components/patientView/documentation/addDocumentation/creatCaseReviewCouncil.vue";
import CreateEquipment from "@/components/patientView/documentation/addDocumentation/createEquipment.vue";
import CreatVisit from "@/components/patientView/documentation/addDocumentation/creatVisit.vue";
import CreateFeedbackCareTeamTelephoneConsultation
    from "@/components/patientView/documentation/addDocumentation/createFeedbackCareTeamTelephoneConsultation.vue";
import CreateDataReviewProcessing
    from "@/components/patientView/documentation/addDocumentation/createDataReviewProcessing.vue";
import CreateTelephoneConsultation
    from "@/components/patientView/documentation/addDocumentation/createTelephoneConsultation.vue";
import CreateConsultation from "@/components/patientView/documentation/addDocumentation/createConsultation.vue";
import CreateInitialInterviewTelephone
    from "@/components/patientView/documentation/addDocumentation/createInitialInterviewTelephone.vue";
import {useRoute} from "vue-router";
import InitialInterviewTelephones from "@/components/patientView/documentation/fetchAll/initialInterviewTelephones.vue";
export default {
    name: 'NewDataFormView',
    data() {
        return {
            option: '',
            id: useRoute().params.id,
            options: [
                'Eingangsuntersuchung',
                'Wearable',
                'Eingangsgespräch',
                'Rückmeldung',
                'equipment',
                'hausebesuch',
                'processing',
                'Fallbesprechung',
                'Fallbesprechung-konsil',
                'Fallbesprechung-nurse-konsil',
                'Konsultation',
                'Telefonische-Konsultation',
            ],
        }
    },

    components: {
        InitialInterviewTelephones,
        CreateCaseReview,
        CreateInitialExamination,
        CreateInstructionWearable,
        CreatVisit,
        CreateEquipment,
        CreateFeedbackCareTeamTelephoneConsultation,
        CreateConsultation,
        CreateCaseReviewNurseCouncil,
        CreateTelephoneConsultation,
        CreateDataReviewProcessing,
        CreatCaseReviewCouncil,
        CreateInitialInterviewTelephone

    }
}
</script>