<template>
    <div class="border-t sm:border-t-0 sm:border-r border-t-sky-800 border-r-sky-800 sm:top-[21%]
  flex sm:flex-col justify-around items-center sm:fixed">
        <router-link :to="`/patients/${id}/info`" class="relative m-2 sm:m-4 p-3 group">
          <i class="py-4 px-4 hover:bg-sky-800 hover:text-slate-200 text-sky-800 bg-slate-200 rounded-3xl hover:cursor-pointer">
              <font-awesome-icon icon="fa-solid fa-user" />
          </i>
          <span class="absolute w-auto p-3 m-2 min-w-max left-0 bottom-10 rounded-md shadow-2xl text-sky-800 bg-slate-200
          text-xs font-bold transition-all scale-0  duration-300 ease-linear group-hover:scale-100">
              PATIENT INFO
          </span>
      </router-link>
      <router-link :to="`/patients/${id}/medications`" class="relative m-2 sm:m-4 p-3 group">
           <i class="py-4 px-4 hover:bg-sky-800 hover:text-slate-200 text-sky-800 bg-slate-200 rounded-3xl hover:cursor-pointer">
              <font-awesome-icon icon="fa-solid fa-stethoscope" />
          </i>
          <span class="absolute w-auto p-3 m-2 min-w-max left-0 bottom-10 rounded-md shadow-2xl text-sky-800 bg-slate-200
          text-xs font-bold transition-all scale-0  duration-300 ease-linear group-hover:scale-100">
              Profile
          </span>
      </router-link>
      <router-link :to="`/patients/${id}/sensorData`" class="relative m-2 sm:m-4 p-3 group">
          <i class="py-4 px-4 hover:bg-sky-800 hover:text-slate-200 text-sky-800 bg-slate-200 rounded-3xl hover:cursor-pointer">
              <font-awesome-icon icon="fa-solid fa-user" />
          </i>
          <span class="absolute w-auto p-3 m-2 min-w-max left-0 bottom-10 rounded-md shadow-2xl text-sky-800 bg-slate-200
          text-xs font-bold transition-all scale-0  duration-300 ease-linear group-hover:scale-100">
              PATIENT INFO
          </span>
      </router-link>
      <router-link :to="`/patients/${id}/conversations`" class="relative m-2 sm:m-4 p-3 group">
          <i class="py-4 px-4 hover:bg-sky-800 hover:text-slate-200 text-sky-800 bg-slate-200 rounded-3xl hover:cursor-pointer">
              <font-awesome-icon icon="fa-solid fa-user" />
          </i>
          <span class="absolute w-auto p-3 m-2 min-w-max left-0 bottom-10 rounded-md shadow-2xl text-sky-800 bg-slate-200
          text-xs font-bold transition-all scale-0  duration-300 ease-linear group-hover:scale-100">
              PATIENT INFO
          </span>
      </router-link>
        <router-link :to="`/patients/${id}/documentations`" class="relative m-2 sm:m-4 p-3 group">
          <i class="py-4 px-4 hover:bg-sky-800 hover:text-slate-200 text-sky-800 bg-slate-200 rounded-3xl hover:cursor-pointer">
              <font-awesome-icon icon="fa-solid fa-user" />
          </i>
          <span class="absolute w-auto p-3 m-2 min-w-max left-0 bottom-10 rounded-md shadow-2xl text-sky-800 bg-slate-200
          text-xs font-bold transition-all scale-0  duration-300 ease-linear group-hover:scale-100">
              PATIENT INFO
          </span>
      </router-link>
  </div>
</template>
<script setup>
import {useRoute} from "vue-router";

let id = useRoute().params.id
</script>
<style>
.router-link-active i {
    background: #1b6d85;
    color: white;
}
</style>