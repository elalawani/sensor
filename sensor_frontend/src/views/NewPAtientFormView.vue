<template>
    <!--
   -->
    <section class="mt-14">
        <div class="flex flex-col items-center justify-center px-6 py-10 mx-auto h-screen lg:py-0">
            <div class="w-full rounded-lg md:mt-0 sm:max-w-screen-sm xl:p-0">
                <div class="p-6 space-y-4 md:space-y-6 sm:p-8 bg-slate-300 dark:bg-slate-500 rounded-xl">
                    <form method="post" class="space-y-4 md:space-y-6" @submit.prevent="submitform">
                        <div v-if="step === 1">
                            <h1 class="text-xl font-bold leading-tight tracking-tight md:text-2xl mb-6">
                                personal information
                            </h1>
                            <input type="radio" id="mr" value="M" v-model="patInfo.gender" />
                            <label for="mr">Mr</label>
                            <input type="radio" id="ms" value="F" v-model="patInfo.gender" />
                            <label for="ms">Ms</label>
                            <div>
                                <label for="firstname" class="block mb-2 text-sm font-medium ">first Name</label>
                                <input type="text" v-model="patInfo.first_name" name="firstname" id="firstname" class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block w-full p-2.5 dark:bg-slate-700 dark:border-slate-600" placeholder="first name" required="">
                            </div>
                            <div class="flex justify-between flex-row space-x-2 items-center">
                                <div class="w-full">
                                    <label for="lastname" class="block my-2 text-sm font-medium">last name</label>
                                    <input type="text" v-model="patInfo.last_name" name="lastname" id="lastname" class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block w-full p-2.5 dark:bg-slate-700 dark:border-slate-600" placeholder="last name" required="">
                                </div>
                                <div>
                                    <label for="birthdate" class=" block my-2 text-sm font-medium ">birthdate</label>
                                    <input type="date" v-model="patInfo.date_of_birth" name="birthdate" id="birthdate" class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block w-full p-2.5 dark:bg-slate-700 dark:border-slate-600" required="">
                                </div>
                            </div>
                            <div class="flex justify-between flex-row space-x-2 items-center">
                                <div class="w-full">
                                    <label for="street" class="block my-2 text-sm font-medium">Street</label>
                                    <input type="text" v-model="patInfo.address.street" name="street" id="street" class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block w-full p-2.5 dark:bg-slate-700 dark:border-slate-600" placeholder="last name" required="">
                                </div>
                                <div>
                                    <label for="nr" class=" block my-2 text-sm font-medium ">nr.</label>
                                    <input type="text" v-model="patInfo.address.nr" name="nr" id="nr" class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block w-full p-2.5 dark:bg-slate-700 dark:border-slate-600" placeholder="nr." required="">
                                </div>
                            </div>
                             <div class="flex justify-between flex-row space-x-2 items-center">
                                <div>
                                    <label for="plz" class="block my-2 text-sm font-medium">PLZ</label>
                                    <input type="text" v-model="patInfo.address.PLZ" name="plz" id="plz" class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block w-full p-2.5 dark:bg-slate-700 dark:border-slate-600" placeholder="PLZ" required="">
                                </div>
                                <div class="w-full">
                                    <label for="city" class=" block my-2 text-sm font-medium ">City</label>
                                    <input type="text" v-model="patInfo.address.city" name="city" id="city" class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block w-full p-2.5 dark:bg-slate-700 dark:border-slate-600" placeholder="City" required="">
                                </div>
                            </div>
                            <div>
                                <label for="email" class="block my-2 text-sm font-medium text-gray-900 dark:text-white">email</label>
                                <input type="email" v-model="patInfo.email" name="email"  placeholder="email" class="border border-gray-300 sm:text-sm rounded-lg block w-full p-2.5 dark:bg-slate-700 dark:border-slate-600" >
                                <label for="phone" class="block my-2 text-sm font-medium text-gray-900 dark:text-white">phone</label>
                                <input type="text" v-model="patInfo.phone" name="phone"  placeholder="phone" class="border border-gray-300 sm:text-sm rounded-lg block w-full p-2.5 dark:bg-slate-700 dark:border-slate-600" >
                            </div>
                        </div>
                        <div v-if="step === 2">
                            <h1 class="text-xl font-bold leading-tight tracking-tight md:text-2xl mb-6">
                                Medical history
                            </h1>
                            <div>
                                <label for="reason_of_visiting" class="block mb-2 text-sm font-medium ">reason of visiting</label>
                                <input type="text" v-model="patInfo.medicalHistory.reason_of_visiting" name="reason_of_visiting" id="reason_of_visiting" class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block w-full p-2.5 dark:bg-slate-700 dark:border-slate-600" placeholder="for example: Headache" >
                            </div>
                            <div>
                                <label for="chronic_conditions" class="block my-2 text-sm font-medium ">chronic conditions</label>
                                <input type="text" v-model="patInfo.medicalHistory.chronic_conditions" name="chronic_conditions" id="chronic_conditions" class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block w-full p-2.5 dark:bg-slate-700 dark:border-slate-600" placeholder="this must be a drop down list">
                            </div>
                            <div>
                                <label for="medications" class="block my-2 text-sm font-medium text-gray-900 dark:text-white">medications</label>
                                <input type="text" v-model="patInfo.medicalHistory.medications" name="medications" placeholder="drop down also" class="border border-gray-300 sm:text-sm rounded-lg block w-full p-2.5 dark:bg-slate-700 dark:border-slate-600">
                            </div>
                            <div>
                                <label for="measurements" class="block my-2 text-sm font-medium text-gray-900 dark:text-white">is there any measurements ? </label>
                                <div class="flex flex-row justify-start">
                                  yes  <input type="radio" value="y" v-model="patInfo.medicalHistory.measurements" name="measurements"  placeholder="repeat password" class="  w-[10%] p-1">
                             no   <input type="radio" value="n" v-model="patInfo.medicalHistory.measurements" name="measurements"  placeholder="repeat password" class=" w-[10%]   p-1 ">
                                </div>
                                <div>
                                </div>

                                   </div>
                        </div>
                        <div v-if="step === 3 && patInfo.medicalHistory.measurements === 'y'">
                            <h1 class="text-xl font-bold leading-tight tracking-tight md:text-2xl mb-6">
                                add Measurement +
                            </h1>

                        </div>
                        <div v-if="step === 4 || step === 3 && patInfo.medicalHistory.measurements === 'n'">
                            <h1 class="text-xl font-bold leading-tight tracking-tight md:text-2xl mb-6">
                                add Relations
                            </h1>
                            <div>
                                <label for="Doctors" class="block mb-2 text-sm font-medium ">Doctors</label>
                                <div>
                                    <div>
                                        {{doctors}}
                                    </div>
                                    <multi-select
                                        v-model="patInfo.relatedPerson.doctor"
                                        :options="doctors"
                                        mode="multiple"
                                        :close-on-select="false"
                                        :searchable="true"
                                        :create-option="true"
                                        class="text-sky-800"
                                    />
                                </div>
                                <input type="text" v-model="patInfo.relatedPerson.doctor" name="Doctors" id="Doctors" class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block w-full p-2.5 dark:bg-slate-700 dark:border-slate-600" placeholder="username" required="">
                            </div>
                            <div>
                                <label for="nurses" class="block my-2 text-sm font-medium ">nurses</label>
                                <input type="text" v-model="patInfo.relatedPerson.nurses" name="nurses" id="nurses" class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block w-full p-2.5 dark:bg-slate-700 dark:border-slate-600" placeholder="your Email" required="">
                            </div>
                             <div class="flex justify-around">

                            <button type="submit" class="text-gray-50 bg-sky-800 hover:bg-sky-600 rounded-lg text-sm mt-5 px-14 py-2.5">Add Patient</button>
                        </div>
                        </div>

                    </form>

                    <div class="flex justify-around">
                        <button @click="previous" v-if="step > 1">&lt; Previous</button>
                        <button @click="next" v-if="step < 4 ">next  &gt; </button>
                    </div>
                    <div v-if="errors.length">
                        <div class="bg-red-300 text-gray-50 rounded">
                        <p v-for="error in errors" :key="error">
                            {{ error }}
                        </p>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </section>

</template>
<script>
import axios from "axios";
import {useToastStore} from "@/stores/toast";

export default {
    name: 'signupForm',

    setup() {
        const toastStore = useToastStore()

        return {
            toastStore
        }
    },
    data() {
        return {
            step: 1,
            doctors: [],
            patInfo: {
                first_name: '',
                last_name: '',
                gender: '',
                address: {
                    street: '',
                    nr: '',
                    PLZ: '',
                    city: '',
                },
                date_of_birth: '',
                email: '',
                phone: '',
                medicalHistory: {
                    reason_of_visiting: '',
                    medications: '',
                    chronic_conditions: '',
                    measurements: false,
                },
                measurements: {
                    type: '',
                    eval: '',
                    comment: '',
                    date_of_measure: '',
                },
                relatedPerson: {
                    doctor: null,
                    nurses: '',
                },
            },

            errors: [],
        }
    },
    methods: {
        next() {
            if (this.step < 4) {
                this.step += 1;
            }
        },
        previous() {
            if (this.step > 1) {
                this.step -= 1;
            }
        },
        submitform() {
         /*   this.errors = []

            if (this.form.email === ''){
                this.errors.push('please enter email')
            }

            if (this.form.name === ''){
                this.errors.push('please enter name')
            }
            if (this.form.password1 === ''){
                this.errors.push('please enter password')
            }

            if (this.form.password1 !== this.form.password2){
                this.errors.push('no match found')
            }
*/
                axios
                    .post('/api/patients/create/', this.patInfo)
                    .then(response => {
                        console.log(this.patInfo)
                        if (response.data.message === 'success') {

                            this.toastStore.showToast(
                                5000,
                                'registered, please login',
                                'bg-emerald-400'
                            )

                            this.patInfo.first_name = ''
                            this.patInfo.last_name = ''
                            this.patInfo.gender = ''
                            this.patInfo.address.street = ''
                            this.patInfo.address.nr = ''
                            this.patInfo.address.city = ''
                            this.patInfo.address.PLZ = ''
                            this.patInfo.date_of_birth = ''
                            this.patInfo.email = ''
                            this.patInfo.phone = ''
                            this.patInfo.medicalHistory.reason_of_visiting = ''
                            this.patInfo.medicalHistory.medications = ''
                            this.patInfo.medicalHistory.measurements = false
                            this.patInfo.medicalHistory.chronic_conditions = ''
                            this.patInfo.measurements.type = ''
                            this.patInfo.measurements.eval = ''
                            this.patInfo.measurements.comment = ''
                            this.patInfo.measurements.date_of_measure = ''
                            this.patInfo.relatedPerson.doctor = ''
                            this.patInfo.relatedPerson.nurses = ''

                        }
                        else {
                            this.toastStore.showToast(
                                5000,
                                'please try again',
                                'bg-red-400'
                            )
                        }
                    })
                    .catch(error => {
                        console.log('error',error)
                    })
        },
    },

    async mounted() {
    const response = await axios.get('/api/doctors/');
    this.doctors = response.data.map((doctor, index) => ({
        value: index,
        label: doctor.name
    }));
  },
}
</script>
