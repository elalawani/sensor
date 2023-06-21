import {defineStore} from "pinia";
import axios from "axios";

export const usePatientStore = defineStore({

    id: 'patients',

    state: () => ({
        patients: [],
    }),

    actions: {
        async getPatient() {
            await axios
                .get('/api/patients/')
                .then(response => {
                    console.log('data', response.data)
                    this.patients = response.data
                })
                .catch(error => {
                    console.log('error', error)
                })
        }
    },
    persist: true,
})
