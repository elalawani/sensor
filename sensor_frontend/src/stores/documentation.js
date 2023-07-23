import {defineStore} from "pinia";
import axios from "axios";
import router from '../router'

export const useDocumentationsStore = defineStore({

    id: 'documentation',

    state: ()=> ({
        initial_examinations: [],
        instruction_wearables: [],
        initial_interview_telephones: [],
        data_review_processing: [],
        telephone_consultations: [],
        feedback_careTeam_telephone_consultation: [],
        case_review_nurse_council: [],
        case_review_council: [],
        case_review: [],
        consultation: [],
        visit: [],
        equipment: [],
    }),

    actions: {
        async get_initial_examinations(patient_id){
            this.initial_examinations = []
            await axios.get(`/api/documentation/initial_examinations/${patient_id}`)
                .then(response => {
                    this.initial_examinations = response.data
                    console.log(this.initial_examinations);
                })
                .catch(error => {
                    console.log('error', error.response.status)
                    if (error.response && error.response.status === 403) {
                        router.push({name: 'all_patients'})
                    }
                })
        },
        async get_instruction_wearables(patient_id){
            this.instruction_wearables = []
            await axios.get(`/api/documentation/instruction_wearables/${patient_id}`)
                .then(response => {
                    console.log(response.data[0].created_at)
                    this.instruction_wearables = response.data
                })
                .catch(error => {
                    console.log('error', error.response.status)
                    if (error.response && error.response.status === 403) {
                        router.push({name: 'all_patients'})
                    }
                })
        },
         async get_initial_interview_telephones(patient_id){
            this.initial_interview_telephones = []
            await axios.get(`/api/documentation/initial_interview_telephones/${patient_id}`)
                .then(response => {
                    this.initial_interview_telephones = response.data
                })
                .catch(error => {
                    console.log('error', error.response.status)
                    if (error.response && error.response.status === 403) {
                        router.push({name: 'all_patients'})
                    }
                })
        },
         async get_data_review_processing(patient_id){
            this.data_review_processing = []
            await axios.get(`/api/documentation/data_review_processing/${patient_id}`)
                .then(response => {
                    this.data_review_processing = response.data
                    console.log(response.data)
                })
                .catch(error => {
                    console.log('error', error.response.status)
                    if (error.response && error.response.status === 403) {
                        router.push({name: 'all_patients'})
                    }
                })
        },
         async get_telephone_consultations(patient_id){
            this.telephone_consultations = []
            await axios.get(`/api/documentation/telephone_consultations/${patient_id}`)
                .then(response => {
                    this.telephone_consultations = response.data
                })
                .catch(error => {
                    console.log('error', error.response.status)
                    if (error.response && error.response.status === 403) {
                        router.push({name: 'all_patients'})
                    }
                })
        },
         async get_feedback_careTeam_telephone_consultation(patient_id){
            this.feedback_careTeam_telephone_consultation = []
            await axios.get(`/api/documentation/feedback_care_team_telephone_consultation/${patient_id}`)
                .then(response => {
                    this.feedback_careTeam_telephone_consultation = response.data
                                        console.log(response.data[0])

                })
                .catch(error => {
                    console.log('error', error.response.status)
                    if (error.response && error.response.status === 403) {
                        router.push({name: 'all_patients'})
                    }
                })
        },
         async get_case_review_nurse_council(patient_id){
            this.case_review_nurse_council = []
            await axios.get(`/api/documentation/case_review_nurse_council/${patient_id}`)
                .then(response => {
                    this.case_review_nurse_council = response.data
                })
                .catch(error => {
                    console.log('error', error.response.status)
                    if (error.response && error.response.status === 403) {
                        router.push({name: 'all_patients'})
                    }
                })
        },
         async get_case_review_council(patient_id){
            this.case_review_council = []
            await axios.get(`/api/documentation/case_review_council/${patient_id}`)
                .then(response => {
                    this.case_review_council = response.data
                })
                .catch(error => {
                    console.log('error', error.response.status)
                    if (error.response && error.response.status === 403) {
                        router.push({name: 'all_patients'})
                    }
                })
        },
         async get_equipment(patient_id){
            this.equipment = []
            await axios.get(`/api/documentation/equipment/${patient_id}`)
                .then(response => {
                    this.equipment = response.data
                })
                .catch(error => {
                    console.log('error', error.response.status)
                    if (error.response && error.response.status === 403) {
                        router.push({name: 'all_patients'})
                    }
                })
        },
         async get_visit(patient_id){
            this.visit = []
            await axios.get(`/api/documentation/visit/${patient_id}`)
                .then(response => {
                    this.visit = response.data
                })
                .catch(error => {
                    console.log('error', error.response.status)
                    if (error.response && error.response.status === 403) {
                        router.push({name: 'all_patients'})
                    }
                })
        },
         async get_consultation(patient_id){
            this.consultation = []
            await axios.get(`/api/documentation/consultation/${patient_id}`)
                .then(response => {
                    this.consultation = response.data
                })
                .catch(error => {
                    console.log('error', error.response.status)
                    if (error.response && error.response.status === 403) {
                        router.push({name: 'all_patients'})
                    }
                })
        },
         async get_case_review(patient_id){
            this.case_review = []
            await axios.get(`/api/documentation/case_review/${patient_id}`)
                .then(response => {
                    this.case_review = response.data
                })
                .catch(error => {
                    console.log('error', error.response.status)
                    if (error.response && error.response.status === 403) {
                        router.push({name: 'all_patients'})
                    }
                })
        },
    }
})