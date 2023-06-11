<template>
    <section>
        <div class="flex flex-col items-center justify-center px-6 py-8 mx-auto h-screen lg:py-0">
            <div class="w-full rounded-lg md:mt-0 sm:max-w-md xl:p-0">
                <div class="p-6 space-y-4 md:space-y-6 sm:p-8 bg-slate-300 dark:bg-slate-500 rounded-xl">
                    <h1 class="text-xl font-bold leading-tight tracking-tight md:text-2xl">
                        Login
                    </h1>
                    <form class="space-y-4 md:space-y-6" action="#">
                        <div>
                            <label for="username" class="block mb-2 text-sm font-medium ">username</label>
                            <input type="text" name="username" id="username" class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block w-full p-2.5 dark:bg-slate-700 dark:border-slate-600" placeholder="username" required="">
                        </div>
                        <div>
                            <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Password</label>
                            <input type="password" name="password" id="password" placeholder="password" class="border border-gray-300 sm:text-sm rounded-lg block w-full p-2.5 dark:bg-slate-700 dark:border-slate-600" required="">
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
                            <a href="#" class="text-sm font-medium  hover:underline ">Forgot password?</a>
                            <div>
                                <button @click="signupForm" class="text-gray-100 text-sm hover:underline ">create new account</button>
                            </div>
                        </div>
                        <button type="submit" class="text-gray-50 bg-sky-800 hover:bg-sky-600 rounded-lg text-sm px-5 py-2.5">Sign in</button>
                    </form>
                    <div class="flex justify-around">
                        <button @click="$emit('closeForm')">back</button>
                        <button @click="$emit('changeForm')">signup</button>
                    </div>
                </div>
            </div>
        </div>
    </section>

</template>
<script>
import signupForm from "@/components/signupForm.vue";

export default {
    name: 'loginform',
    computed: {
        signupForm() {
            return signupForm
        }
    }
}
</script>