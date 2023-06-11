<template>
    <div class="mt-24 mx-4">
        <div> hi <span> nurse </span></div>

        <div class="flex flex-col sm:flex-row justify-around mt-20">
            <div class="w-2/5 mb-4 sm-mb-0">
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
            <div class="w-2/5 sm:ml-8">
                <span>
                    my Todos
                </span>
                <span>
                    all
                </span>
                <hr>
                <div>
                    <ul>
                        <li>
                            meeting with doctor
                        </li>
                    </ul>
                </div>
            </div>

        </div>
    </div>
</template>
<script setup>
</script>