import {defineStore} from "pinia";
import axios from "axios";

export const usePatientStore = defineStore({

    id: 'patients',

    state: () => ({
        patients: [],
        patient: [],
    }),

    actions: {
        async getPatients() {
            await axios
                .get('/api/patients/')
                .then(response => {
                    this.patients = response.data
                })
                .catch(error => {
                    console.log('error', error)
                })
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
