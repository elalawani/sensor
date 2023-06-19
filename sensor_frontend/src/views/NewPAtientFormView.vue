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
                                    <input type="text" v-model="patInfo.street" name="street" id="street" class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block w-full p-2.5 dark:bg-slate-700 dark:border-slate-600" placeholder="last name" required="">
                                </div>
                                <div>
                                    <label for="nr" class=" block my-2 text-sm font-medium ">nr.</label>
                                    <input type="text" v-model="patInfo.nr" name="nr" id="nr" class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block w-full p-2.5 dark:bg-slate-700 dark:border-slate-600" placeholder="nr." required="">
                                </div>
                            </div>
                             <div class="flex justify-between flex-row space-x-2 items-center">
                                <div>
                                    <label for="plz" class="block my-2 text-sm font-medium">PLZ</label>
                                    <input type="text" v-model="patInfo.PLZ" name="plz" id="plz" class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block w-full p-2.5 dark:bg-slate-700 dark:border-slate-600" placeholder="PLZ" required="">
                                </div>
                                <div class="w-full">
                                    <label for="city" class=" block my-2 text-sm font-medium ">City</label>
                                    <input type="text" v-model="patInfo.city" name="city" id="city" class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block w-full p-2.5 dark:bg-slate-700 dark:border-slate-600" placeholder="City" required="">
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
                                <input type="text" v-model="patInfo.reason_of_visiting" name="reason_of_visiting" id="reason_of_visiting" class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block w-full p-2.5 dark:bg-slate-700 dark:border-slate-600" placeholder="for example: Headache" >
                            </div>
                            <div>
                                <label for="chronic_conditions" class="block my-2 text-sm font-medium ">chronic conditions</label>
                                <input type="text" v-model="patInfo.chronic_conditions.name" name="chronic_conditions" id="chronic_conditions" class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block w-full p-2.5 dark:bg-slate-700 dark:border-slate-600" placeholder="this must be a drop down list">
                            </div>
                            <div>
                                <label for="medications" class="block my-2 text-sm font-medium text-gray-900 dark:text-white">medications</label>
                                <input type="text" v-model="patInfo.medications.name" name="medications" placeholder="drop down also" class="border border-gray-300 sm:text-sm rounded-lg block w-full p-2.5 dark:bg-slate-700 dark:border-slate-600">
                            </div>
                        </div>
                        <div v-if="step === 3">
                            <h1 class="text-xl font-bold leading-tight tracking-tight md:text-2xl mb-6">
                                add Relations
                            </h1>
                            <div>
                                <label for="Doctors" class="block mb-2 text-sm font-medium ">Doctors</label>
                                <div>
                                    <div class="flex flex-row space-x-2">
                                        <div class="p-1 pl-2 rounded bg-slate-700 mb-1" v-for="(doctor, index_doctor) in patInfo.doctor" :key="index_doctor">
                                            {{doctors[doctor].label}}
                                            <span class="hover:cursor-pointer py-1 px-2 rounded-full bg-slate-900 text-xs" @click="removeDoctor(index_doctor)">x</span>
                                        </div>
                                    </div>
                                    <multi-select
                                        v-model="patInfo.doctor"
                                        :options="doctors"
                                        mode="multiple"
                                        :close-on-select="false"
                                        :searchable="true"
                                        :create-option="true"
                                        class="text-sky-800"
                                        placeholder="Select Doctors"
                                    />
                                </div>
                            </div>
                            <div>
                                <label for="nurses" class="block mt-12 mb-2 text-sm font-medium ">nurses</label>
                                <div>
                                    <div class="flex flex-row space-x-2">
                                        <div class="p-1 pl-2 rounded bg-slate-700 mb-1" v-for="(nurse, index_nurse) in patInfo.nurse" :key="index_nurse">
                                            {{nurses[nurse].label}}
                                            <span class="hover:cursor-pointer py-1 px-2 rounded-full bg-slate-900 text-xs" @click="removeNurse(index_nurse)">x</span>
                                        </div>
                                    </div>
                                    <multi-select
                                        v-model="patInfo.nurse"
                                        :options="nurses"
                                        mode="multiple"
                                        :close-on-select="false"
                                        :search="true"
                                        class="text-sky-800"
                                        placeholder="Select Nurses"
                                    />
                                </div>
                            </div>
                             <div class="flex justify-around">

                            <button type="submit" class="text-gray-50 bg-sky-800 hover:bg-sky-600 rounded-lg text-sm mt-5 px-14 py-2.5">Add Patient</button>
                        </div>
                        </div>

                    </form>

                    <div class="flex justify-around">
                        <button @click="previous" v-if="step > 1">&lt; Previous</button>
                        <button @click="next" v-if="step < 3 ">next  &gt; </button>
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
            nurses: [],
            patInfo: {
                first_name: '',
                last_name: '',
                gender: '',
                street: '',
                nr: '',
                PLZ: '',
                city: '',
                date_of_birth: '',
                email: '',
                phone: '',
                reason_of_visiting: '',
                medications: [],
                chronic_conditions: [],
                doctor: [],
                nurse: [],
            },
            errors: [],
        }
    },
    methods: {
        next() {
            if (this.step < 3) {
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

            console.log(this.patInfo)
                axios
                    .post(
                        '/api/patients/create/',
                        this.patInfo,
                    )
                    .then(response => {
                        console.log( 'response', response.data)
                        if (response.data.message === 'success') {


                            this.toastStore.showToast(
                                5000,
                                'registered, please login',
                                'bg-emerald-400'
                            )

                            this.patInfo.first_name = ''
                            this.patInfo.last_name = ''
                            this.patInfo.gender = ''
                            this.patInfo.street = ''
                            this.patInfo.nr = ''
                            this.patInfo.city = ''
                            this.patInfo.PLZ = ''
                            this.patInfo.date_of_birth = ''
                            this.patInfo.email = ''
                            this.patInfo.phone = ''
                            this.patInfo.reason_of_visiting = ''
                            this.patInfo.medications = []
                            this.patInfo.chronic_conditions = []
                            this.patInfo.doctor = []
                            this.patInfo.nurses = []

                        }
                        else {
                            console.log(response.data)
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
         removeDoctor(index) {
        this.patInfo.doctor.splice(index, 1);
    },
        removeNurse(index) {
        this.patInfo.nurse.splice(index, 1);
    },
    },

    async mounted() {
    const response_doctors = await axios.get('/api/doctors/');
    this.doctors = response_doctors.data.map((doctor, index) => ({
        value: index,
        label: doctor.name
    }));

    const response_nurses = await axios.get('/api/nurses/');
    this.nurses = response_nurses.data.map((nurse, index) => ({
        value: index,
        label: nurse.name
    }));
  },
}
/*
<template>
  <Multiselect
    v-model="value"
    mode="tags"
    placeholder="Select employees"
    track-by="name"
    label="name"
    :close-on-select="false"
    :search="true"
    :options="[
      { value: 'judy', name: 'Judy', image: 'https://randomuser.me/api/portraits/med/women/1.jpg' },
      { value: 'jane', name: 'Jane', image: 'https://randomuser.me/api/portraits/med/women/2.jpg' },
      { value: 'john', name: 'John', image: 'https://randomuser.me/api/portraits/med/men/1.jpg' },
      { value: 'joe', name: 'Joe', image: 'https://randomuser.me/api/portraits/med/men/2.jpg' }
    ]"
  >
    <template v-slot:tag="{ option, handleTagRemove, disabled }">
      <div
        class="multiselect-tag is-user"
        :class="{
          'is-disabled': disabled
        }"
       >
        <img :src="option.image">
        {{ option.name }}
        <span
           v-if="!disabled"
           class="multiselect-tag-remove"
           @mousedown.prevent="handleTagRemove(option, $event)"
        >
          <span class="multiselect-tag-remove-icon"></span>
        </span>
      </div>
    </template>
 </Multiselect>
</template>

<style>
  .multiselect-tag.is-user {
    padding: 5px 8px;
    border-radius: 22px;
    background: #35495e;
    margin: 3px 3px 8px;
  }

  .multiselect-tag.is-user img {
    width: 18px;
    border-radius: 50%;
    height: 18px;
    margin-right: 8px;
    border: 2px solid #ffffffbf;
  }

  .multiselect-tag.is-user i:before {
    color: #ffffff;
    border-radius: 50%;;
  }

  .user-image {
    margin: 0 6px 0 0;
    border-radius: 50%;
    height: 22px;
  }
</style>
*/
</script>
