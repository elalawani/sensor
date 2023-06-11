<template>
    <section class="mt-14">
        <div class="flex flex-col items-center justify-center px-6 py-10 mx-auto h-screen lg:py-0">
            <div class="w-full rounded-lg md:mt-0 sm:max-w-md xl:p-0">
                <div class="p-6 space-y-4 md:space-y-6 sm:p-8 bg-slate-300 dark:bg-slate-500 rounded-xl">
                    <h1 class="text-xl font-bold leading-tight tracking-tight md:text-2xl">
                        sign up
                    </h1>
                    <form class="space-y-4 md:space-y-6" @submit.prevent="submitform">
                        <div>
                            <label for="username" class="block mb-2 text-sm font-medium ">username</label>
                            <input type="text" v-model="form.name" name="username" id="username" class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block w-full p-2.5 dark:bg-slate-700 dark:border-slate-600" placeholder="username" required="">
                        </div>
                         <div>
                            <label for="email" class="block mb-2 text-sm font-medium ">email</label>
                            <input type="email" v-model="form.email" name="email" id="email" class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block w-full p-2.5 dark:bg-slate-700 dark:border-slate-600" placeholder="your Email" required="">
                        </div>
                        <div>
                            <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Password</label>
                            <input type="password" v-model="form.password1" name="password" placeholder="password" class="border border-gray-300 sm:text-sm rounded-lg block w-full p-2.5 dark:bg-slate-700 dark:border-slate-600" required="">
                        </div>
                        <div>
                            <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">repeat Password</label>
                            <input type="password" v-model="form.password2" name="password"  placeholder="repeat password" class="border border-gray-300 sm:text-sm rounded-lg block w-full p-2.5 dark:bg-slate-700 dark:border-slate-600" required="">
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
                        <button type="submit" class="text-gray-50 bg-sky-800 hover:bg-sky-600 rounded-lg text-sm px-5 py-2.5">Sign up</button>
                    </form>

                    <div v-if="errors.length">
                        <div class="bg-red-300 text-gray-50 rounded"></div>
                        <p v-for="error in errors" :key="error">
                            {{ error }}
                        </p>
                    </div>

                    <div class="flex justify-around">
                        <button @click="$emit('closeForm')">back</button>
                        <button @click="$emit('changeForm')">Login</button>
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
            errors: [],
        }
    },
    methods: {
        submitform() {
            this.errors = []

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

            if (this.errors.length === 0) {
                axios
                    .post('/api/signup', this.form)
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
                                'please try agin',
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