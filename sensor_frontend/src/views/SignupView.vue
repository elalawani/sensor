<template>
    <section class="mt-14">
        <div class="flex flex-col items-center justify-center px-6 py-10 mx-auto h-screen lg:py-0">
            <div class="w-full rounded-lg md:mt-0 sm:max-w-md xl:p-0">
                <div class="p-6 space-y-4 md:space-y-6 sm:p-8 border shadow-xl dark:bg-slate-500 rounded-xl">
                    <h1 class="text-xl font-bold leading-tight tracking-tight md:text-2xl">
                        sign up
                    </h1>
                    <form class="space-y-4 md:space-y-6" @submit.prevent="submitForm">
                        <div>
                            <label for="username" class="block mb-2 text-sm font-medium ">username</label>
                            <input
                                type="text"
                                v-model="form.name"
                                name="username"
                                id="username"
                                :class="errors.name ? 'border-red-500 dark:border' : ''"
                                class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block w-full p-2.5 dark:bg-slate-700 dark:border-slate-600"
                                placeholder="username">
                            <span v-if="errors.name" class="ml-4 text-red-500">{{errors.name}}</span>
                        </div>
                         <div>
                            <label for="email" class="block mb-2 text-sm font-medium ">email</label>
                            <input
                                type="email"
                                v-model="form.email"
                                name="email"
                                id="email"
                                :class="errors.email ? 'border-red-500 dark:border' : ''"
                                class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block w-full p-2.5 dark:bg-slate-700 dark:border-slate-600"
                                placeholder="your Email">
                             <span v-if="errors.email" class="ml-4 text-red-500">{{errors.email}}</span>
                        </div>

                        <div>
                            <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Password</label>
                            <input
                                type="password"
                                v-model="form.password1"
                                name="password"
                                placeholder="password"
                                :class="errors.password1 ? 'border-red-500 dark:border' : ''"
                                class="border border-gray-300 sm:text-sm rounded-lg block w-full p-2.5 dark:bg-slate-700 dark:border-slate-600">
                            <span v-if="errors.password1" class="ml-4 text-red-500">{{errors.password1}}</span>

                        </div>
                        <div>
                            <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">repeat Password</label>
                            <input
                                type="password"
                                v-model="form.password2"
                                name="password"
                                placeholder="repeat password"
                                :class="errors.matchError ? 'border-red-500 dark:border' : ''"
                                class="border border-gray-300 sm:text-sm rounded-lg block w-full p-2.5 dark:bg-slate-700 dark:border-slate-600">
                         <span v-if="errors.matchError" class="ml-4 text-red-500">{{errors.matchError}}</span>

                        </div>
                        <div class="flex items-center justify-between">
                            <div class="flex items-start">
                                <div class="flex items-center h-5">
                                    <input id="remember" aria-describedby="remember" type="checkbox" class="w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-primary-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-primary-600 dark:ring-offset-gray-800">
                                </div>
                                <div class="ml-3 text-sm">
                                    <label for="remember">Remember me</label>
                                </div>
                            </div>
                        </div>
                        <div class="flex justify-around">
                                    <button type="submit" class="text-sky-700 hover:text-white border dark:border-0 border-sky-700 dark:text-slate-100 dark:bg-sky-700 hover:bg-sky-700 dark:hover:bg-sky-500 rounded-lg text-sm px-14 py-2.5">Sign up</button>
                        </div>
                    </form>
                    <div class="flex justify-around">
                        <router-link to="/login">Login</router-link>
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
            form: {
                email: '',
                name: '',
                password1: '',
                password2: '',
            },
            errors: {
                email: '',
                name: '',
                password1: '',
                matchError: '',
            },
        }
    },
    methods: {
        submitForm() {
            this.errors.email = ''
            this.errors.name = ''
            this.errors.password1 = ''
            this.errors.matchError = ''


            if (this.form.email === ''){
                this.errors.email = 'please enter your email'
            }

            if (this.form.name === ''){
                this.errors.name = 'please enter your name'
            }
            if (this.form.password1 === ''){
                this.errors.password1 = 'please enter password'
            }

            if (this.form.password1 !== this.form.password2){
                this.errors.matchError = 'no match found'
            }


            if (this.errors.name === '' && this.errors.email === '' && this.errors.password1 === '' && this.errors.matchError === '') {
                axios
                    .post('/api/signup/', this.form)
                    .then(response => {
                        if (response.data.message === 'success') {

                            this.toastStore.showToast(
                                5000,
                                'registered, please login',
                                'bg-emerald-400'
                            )

                            this.form.email = ''
                            this.form.name = ''
                            this.form.password1 = ''
                            this.form.password2 = ''
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
            }
        }
    }
}
</script>