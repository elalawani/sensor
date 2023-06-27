import {defineStore} from "pinia";
import axios from "axios";
import router from '../router'
import {useToastStore} from "@/stores/toast";
export const usePatientStore = defineStore({

    id: 'patients',

    state: () => ({
        patients: [],
        patient: [],
        filters: {
            byName: null,
            byType: null,
            byBirthdate: null,
            byDoctor: null,
            byNurse: null,
            byCondition: null,
            byMedications: null,
            byCreator: null,
    }
    }),

    actions: {
        async getPatients() {
            this.patients = []
            await axios
                .get('/api/patients/', {params: this.filters})
                .then(response => {
                    this.patients = response.data
                })
                .catch(error => {
                    console.log('error', error)
                })
        },
        updateFilters(newFilters) {
            this.filters = newFilters
        },
        removeFilter() {
            this.filters = ''
        },
        async getPatient(id) {
            await axios
                .get(`/api/patients/${id}`)
                .then(response => {
                    this.patient = response.data
                })
                .catch(error => {
                    console.log('error', error.response.status)
                    if (error.response && error.response.status === 403) {
                        router.push({name: 'all_patients'})
                    }
                })
        },

    },
    persist: true,
})
