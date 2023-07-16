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
        async get_initial_examinations(){
            this.initial_examinations = []
            await axios.get('/api/documentation/initial_examinations/')
                .then(response => {
                    this.initial_examinations = response.data
                })
                .catch(error => {
                    console.log('error', error.response.status)
                    if (error.response && error.response.status === 403) {
                        router.push({name: 'all_patients'})
                    }
                })
        },
        async get_instruction_wearables(){
            this.instruction_wearables = []
            await axios.get('/api/documentation/instruction_wearables/')
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
         async get_initial_interview_telephones(){
            this.initial_interview_telephones = []
            await axios.get('/api/documentation/initial_interview_telephones/')
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
         async get_data_review_processing(){
            this.data_review_processing = []
            await axios.get('/api/documentation/data_review_processing/')
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
         async get_telephone_consultations(){
            this.telephone_consultations = []
            await axios.get('/api/documentation/telephone_consultations/')
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
         async get_feedback_careTeam_telephone_consultation(){
            this.feedback_careTeam_telephone_consultation = []
            await axios.get('/api/documentation/feedback_careTeam_telephone_consultation/')
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
         async get_case_review_nurse_council(){
            this.case_review_nurse_council = []
            await axios.get('/api/documentation/case_review_nurse_council/')
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
         async get_case_review_council(){
            this.case_review_council = []
            await axios.get('/api/documentation/case_review_council/')
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
         async get_equipment(){
            this.equipment = []
            await axios.get('/api/documentation/equipment/')
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
         async get_visit(){
            this.visit = []
            await axios.get('/api/documentation/visit/')
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
         async get_consultation(){
            this.consultation = []
            await axios.get('/api/documentation/consultation/')
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
         async get_case_review(){
            this.case_review = []
            await axios.get('/api/documentation/case_review/')
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