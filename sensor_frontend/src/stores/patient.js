import {defineStore} from "pinia";
import axios from "axios";

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
                    console.log('error', error)
                })
        },

    },
    persist: true,
})
