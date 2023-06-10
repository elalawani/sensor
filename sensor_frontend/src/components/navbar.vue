<template>
    <nav class="dark:bg-slate-900 bg-gray-50 flex justify-between fixed z-50 top-0 w-full border-b border-b-sky-800">
        <div class="m-4">
            <router-link to="/">
                <span class="hover:text-slate-400 text-2xl sm:text-4xl">
                    MSD
                </span>
            </router-link>
        </div>
        <div class="m-6 hidden sm:block">
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
            <router-link to="/">
                <i class="p-4 hover:bg-sky-800 hover:text-slate-200 text-sky-800 bg-slate-300 rounded-full mx-2">
                <font-awesome-icon icon="fa-solid fa-search" />
            </i>
            </router-link>
        </div>
        <div class="m-6 hidden sm:block">
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
            <!-- add a dropdown to switch between login logout show profile -->
            <router-link to="/login">
                <i class="py-4 px-[18px] hover:bg-sky-800 hover:text-slate-200 text-sky-800 bg-slate-200 rounded-full mx-2">
                <font-awesome-icon icon="fa-solid fa-user" />
            </i>
            </router-link>
        </div>

    </nav>
</template>


<script>
export default {
    name: 'navbar',
    data() {
        return {
            isLight: false,
        }
    },
    methods: {
        toggleTheme() {
            this.isLight = !this.isLight;
        },
    }
}
</script>