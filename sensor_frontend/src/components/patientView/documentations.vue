<template>
  <div class="bg-gray-200 text-slate-900 rounded-xl mr-5 min-w-max min-h-screen">

      {{initial_examinations}}
      <br>

      {{instruction_wearables}}
      <br>
      {{visit }}
      <br>
      {{ initial_interview_telephones}}
      <br>
      {{case_review_nurse_council }}
      <br>
      {{case_review_council }}<br>
      {{consultation }}<br>
      {{telephone_consultations }}<br>
      {{ data_review_processing}}
      <br>{{equipment }}
      <br>
      {{case_review }}
      <br>
      {{feedback_careTeam_telephone_consultation }}
  </div>
</template>
<script setup>
import {useDocumentationsStore} from "@/stores/documentation";
import {computed, onMounted} from "vue";
const documentation = useDocumentationsStore()

const fetchData = async () => {
    await documentation.get_feedback_careTeam_telephone_consultation()

}

onMounted(fetchData)

const feedback_careTeam_telephone_consultation = computed(()=>documentation.feedback_careTeam_telephone_consultation)


/*
export default {
    data() {
        return {
            initial_examinations: '',
            instruction_wearables: '',
            initial_interview_telephones: '',
            data_review_processings: '',
            telephone_consultations: '',
            feedback_careTeam_telephone_consultation: '',
            case_review_nurse_council: '',
            case_review_council: '',
            case_review: '',
            consultation: '',
            visit: '',
            equipment: '',
        }
    },
    methods: {
        async documentsList() {
            await axios
                .get('/api/documentation/initial_interview_telephones')
                .then(
                    response => {
                        this.initial_interview_telephones = response.data
            }
                )
        }
    },
    mounted() {
        this.documentsList()
    }
}
*/
</script>