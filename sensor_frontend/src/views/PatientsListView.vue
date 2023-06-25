<template>
    <div class="p-3">
        <div class="dark:text-slate-100 text-slate-900 tracking-tight whitespace-nowrap font-extrabold py-4 sm:text-4xl text-2xl my-8">
            Search or add Patient
        </div>
        <div class="flex justify-center items-center w-full mb-2 rounded-full p-2 bg-sky-700 dark:bg-sky-900 sm:hidden ">
                <router-link to="/add_patient">
                    <i>+</i>
                    add new patient
                </router-link>
        </div>
        <div class="dark:bg-slate-700 rounded-lg bg-gray-50 border  shadow-inner dark:border-0 dark:shadow-none">
            <div class="p-4">
                <input type="search" class="p-2 pl-3 w-full outline-none dark:bg-slate-500 rounded-lg dark:text-slate-100 mb-2 dark:placeholder-slate-100 border-2 dark:border-0 dark:shadow-none shadow-lg" placeholder="search name"/>
                <div class="flex flex-row justify-around mb-4">
                    <input type="date" class="p-2 pl-3 w-full outline-none dark:bg-slate-500 rounded-lg dark:text-slate-100 mb-2 mr-1 border-2 dark:border-0 dark:shadow-none shadow-lg" placeholder="birthdate"/>
                    <input type="search" class="p-2 pl-3 w-full outline-none dark:bg-slate-500 rounded-lg dark:text-slate-100 mb-2 mr-1 dark:placeholder-slate-100 border-2 dark:border-0 dark:shadow-none shadow-lg" placeholder="type"/>
                    <input type="search" class="p-2 pl-3 w-full outline-none dark:bg-slate-500 rounded-lg dark:text-slate-100 mb-2 mr-1 dark:placeholder-slate-100 border-2 dark:border-0 dark:shadow-none shadow-lg" placeholder="type"/>
                </div>
                <label class="dark:text-slate-100 text-xl">
                    filter by disease or chronic Conditions
                </label>

                <div class="flex flex-row justify-around my-3">
                    <input type="search" class="p-2 pl-3 w-full outline-none dark:bg-slate-500 rounded-lg dark:text-slate-100 mb-2 mr-1 dark:placeholder-slate-100 border-2 dark:border-0 dark:shadow-none shadow-lg" placeholder="disease"/>
                    <input type="search" class="p-2 pl-3 w-full outline-none dark:bg-slate-500 rounded-lg dark:text-slate-100 mb-2 mr-1 dark:placeholder-slate-100 border-2 dark:border-0 dark:shadow-none shadow-lg" placeholder="condition"/>
                </div>
                <label class="dark:text-slate-100 text-xl">
                    filter by doctor or nurse
                </label>

                <div class="flex flex-row justify-around mt-3">
                    <input type="search" class="p-2 pl-3 w-full outline-none dark:bg-slate-500 rounded-lg dark:text-slate-100 mb-2 mr-1 dark:placeholder-slate-100 border-2 dark:border-0 dark:shadow-none shadow-lg" placeholder="Doctor"/>
                    <input type="search" class="p-2 pl-3 w-full outline-none dark:bg-slate-500 rounded-lg dark:text-slate-100 mb-2 mr-1 dark:placeholder-slate-100 border-2 dark:border-0 dark:shadow-none shadow-lg" placeholder="nurse"/>
                </div>
            </div>
        </div>
        <div class="flex justify-between items-center text-slate-50 mx-2 my-4">
            <div class="w-fit font-bold sm:rounded-2xl rounded-full p-2 bg-sky-700 dark:bg-sky-900 justify-items-end hidden sm:inline">
                <router-link to="/add_patient">
                    <i>+</i>
                        add new patient
                </router-link>
            </div>
            <div class="flex space-x-4 justify-end">
                <button class="flex dark:bg-slate-700 bg-slate-500 p-2 rounded-2xl px-4">
                    <span class="mr-1">filter</span> <search/>
                </button>
                <button class="flex dark:bg-slate-700 bg-slate-500 p-2 rounded-2xl px-2">
                    <span class="mr-1">refresh</span> <search/>
                </button>
            </div>
        </div>

    </div>
    <div
        class="flex w-full flex-row items-center mt-10"
        v-for="(patient, index) in patientStore.patients"
        :key="index"
    >
        <div class="flex w-full flex-row sm:space-x-10 pr-4">
            <div class="p-10 items-center border-r border-r-slate-500 hidden sm:inline">
                <i class="py-4 ml-auto px-5 text-gray-300 border border-slate-300 rounded-full text-4xl">
                    <font-awesome-icon icon="fa-solid fa-user" />
                </i>
            </div>
            <div class="flex px-10 py-2 rounded-lg flex-row justify-between sm:dark:hover:bg-slate-800 dark:bg-slate-800 ml-4 sm:ml-0 sm:dark:bg-slate-900
            dark:hover:shadow-none dark:border-0 hover:border-t hover:shadow-xl ease-in transition-all duration-100 items-center w-full">
                <div class="">
                    <div class="dark:text-slate-100 font-bold text-2xl">
                        {{patient.last_name}}, {{patient.first_name}}
                    </div>
                    <div class="my-2">
                        <span class="text-slate-100">born on:</span> {{patient.date_of_birth}}
                    </div>
                    <div
                        v-if="patient.gender === 'M'"
                         class="font-extrabold">
                        MALE
                    </div>
                    <div v-else class="font-extrabold">
                        FEMALE
                    </div>
                    <div>
                        date of creation: {{patient.created_at}}
                    </div>
                    <div class="text-sky-500 hover:text-sky-300 hover:dark:text-sky-500 dark:text-sky-700 flex flex-row m-4 mb-0">
                        <router-link :to="`patients/${patient.id}/info`">
                        more information
                        <font-awesome-icon icon="fa-solid fa-arrow-right" />
                    </router-link>
                    </div>
                </div>
                <div class="mr-10">
                  <div class="mb-2 pb-1 border-b border-b-slate-500">
                        <div class="font-bold">
                        Doctors:
                    </div>
                    <div
                        v-for="(doctors, index) in patient.doctors"
                        :key="index"
                    >
                        <router-link to="/" class="dark:hover:text-sky-500 dark:text-sky-700 text-sky-500 hover:text-sky-300 ml-10">
                            {{doctors.name}}
                        </router-link>

                    </div>
                  </div>
                    <div class="mt-1">
                       <div class="font-bold">
                            nurses:
                       </div>
                    <div
                        v-for="(nurses, index) in patient.nurses"
                        :key="index"
                    >
                        <router-link to="/" class="dark:hover:text-sky-500 dark:text-sky-700 text-sky-500 hover:text-sky-300  ml-10">
                            {{nurses.name}}
                        </router-link>

                    </div>
                    </div>
                </div>
            </div>
        </div>
     <!--
       <router-link :to="`patients/${patient.id}/info`">
            <div class="items-center m-6 hover:cursor-pointer relative">
                <div class="flex items-center px-2 hover:dark:bg-slate-800 rounded-lg mb-2 relative
                        shadow hover:shadow-lg flex-col-reverse hover:bg-slate-100 p-6">

                    <div class="text-slate-900 dark:text-slate-100 p-8">
                        <strong>{{patient.first_name}} {{patient.last_name}}</strong><br>
                        <span class="text-gray-400">{{patient.date_of_birth}}</span>
                        <div v-for="doctor in patient.doctors">{{doctor.name}}</div>
                        <div v-for="nurse in patient.nurses">{{nurse.name}}</div>
                    </div>
                    <div class="bg-sky-800 absolute px-3 py-1 bottom-[-1px] right-[-1px] text-gray-50 rounded-br-lg rounded-tl-lg">
                        <font-awesome-icon icon="fa-solid fa-arrow-right" />
                    </div>
                </div>
            </div>
        </router-link>-->
    </div>
</template>
<script setup>

import { usePatientStore } from '@/stores/patient'
import {watch} from "vue";
import Search from "@/components/svgs/search.vue";

const patientStore = usePatientStore()

let patients = patientStore.patients

watch(() => patientStore.patients, (newVal) =>  {
        patients = newVal
    },
    {
        immediate: true
    })
patientStore.getPatients()

</script>