<template>
    <div class="mt-24 mx-4">
        <div> hi <span> {{ userStore.user.name }} </span></div>

        <div class="flex flex-col sm:flex-row justify-around mt-20">
            <div class=" w-full sm:w-2/5 mb-4 ">
                <div class="flex justify-between">
                    <span>
                        my Todos
                    </span>
                    <router-link to="/">
                        all
                    </router-link>
                </div>
                <div>
                    <hr>
                    <ul class="list">
                        <li class="my-3">
                            <input type="checkbox" name="" id="">
                            <span> meeting with doctor </span>
                        </li>
                        <li class="mb-3">
                            <input type="checkbox" name="" id="">
                            <span> write a Documentation </span>
                        </li>
                        <li class="mb-3">
                            <input type="checkbox" name="" id="">
                            <span> check around before i go</span>
                        </li>
                    </ul>
                </div>
            </div>
            <div class=" w-full sm:w-2/5 mb-4 ">
                <div class="flex justify-between">
                    <span>
                        patient
                    </span>
                    <router-link to="/all_patients">
                        search
                    </router-link>
                    <router-link to="/add_patient">
                        add new patient
                    </router-link>
                </div>
                <div>
                    <hr>
                    <ul class="list">
                        <li class="my-3">
                            <input type="checkbox" name="" id="">
                            <span> first </span>
                        </li>
                        <li class="mb-3">
                            <input type="checkbox" name="" id="">
                            <span> second </span>
                        </li>
                        <li class="mb-3">
                            <input type="checkbox" name="" id="">
                            <span> third </span>
                        </li>
                    </ul>
                </div>
            </div>

        </div>
    </div>
</template>
<script setup>
import {useUserStore} from "@/stores/user";

const userStore = useUserStore()

</script>