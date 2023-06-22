<template>
    <nav class="backdrop-blur flex justify-between sticky top-0 z-50 w-full  border-b border-b-sky-800">
        <div class="m-4 flex items-center">
            <router-link to="/">
                <span class="hover:text-slate-400 text-2xl sm:text-4xl">
                    MSD
                </span>
            </router-link>
        </div>
        <div class="m-6 hidden sm:block" v-if="userStore.user.isAuthenticated">
            <router-link to="/">
                <i class="p-4 hover:bg-sky-800 hover:text-slate-200 text-sky-800 bg-slate-300 rounded-full mx-2">
                <font-awesome-icon icon="fa-solid fa-house-chimney" />
            </i>
            </router-link>
            <router-link to="/">
                <i class="p-4 hover:bg-sky-800 hover:text-slate-200 text-sky-800 bg-slate-300 rounded-full mx-2">
                <font-awesome-icon icon="fa-solid fa-message"/>
            </i>
            </router-link>
            <router-link to="/all_patients">
                <i class="p-4 hover:bg-sky-800 hover:text-slate-200 text-sky-800 bg-slate-300 rounded-full mx-2">
                <font-awesome-icon icon="fa-solid fa-search" />
            </i>
            </router-link>
        </div>
        <div class="m-6 hidden sm:flex sm:items-center">
            <div>
                <a v-if="!isLight" href="#" class="m-4" @click="toggleTheme">
                    <i class="p-4 hover:text-sky-800 text-slate-600">
                        <font-awesome-icon icon="fa-solid fa-sun" />
                    </i>
            </a>
            <a v-else href="#" class="m-4" @click="toggleTheme">
                <i class="p-4 hover:text-sky-800 text-slate-600">
                    <font-awesome-icon icon="fa-solid fa-moon" />
                </i>
            </a>
            </div>
            <!-- add a dropdown to switch between login logout show profile -->
            <div class="relative" v-if="userStore.user.isAuthenticated">
                <button @click="toggleList">
                    <i class="py-4 px-[18px] hover:bg-sky-800 hover:text-slate-200 text-sky-800 bg-slate-200 rounded-full mx-2">
                        <font-awesome-icon icon="fa-solid fa-user" />
                    </i>
                </button>
                <div v-if="showList" class="absolute right-3 rounded top-10 flex flex-col bg-slate-700">
                    <router-link to="/profile" @click="toggleList" class="border-b border-b-gray-300 w-full p-8 ">view Profile</router-link>
                    <button @click="reloadPage" class="p-8">logout</button>
                </div>
            </div>
            <div v-else>
                <div class="flex items-center justify-center space-x-5">
                    <router-link
                        to="login"
                        class="p-3 bg-sky-800 rounded-lg hover:bg-sky-600"
                    >
                        Sign in
                    </router-link>
                    <router-link
                        to="signup"
                        class="p-3 bg-slate-500 rounded-lg hover:bg-slate-400"
                    >
                        Sign up
                    </router-link>
                </div>
            </div>
        </div>

    </nav>
</template>


<script>
import {useUserStore} from "@/stores/user";

export default {
    name: 'navbar',
    setup() {
        const userStore = useUserStore()

        return {
            userStore
        }
    },
    data() {
        return {
            isLight: false,
            showList: false,
            formState: '',
        }
    },
    methods: {
        toggleTheme() {
            this.isLight = !this.isLight;
        },
        toggleList() {
            this.showList = !this.showList;
        },
        reloadPage() {
            this.userStore.logout()
            window.location.reload();
        },
        showForm(form) {
      this.formState = form;
    }
    }
}
</script>