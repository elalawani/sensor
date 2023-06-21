<template>
  <div
          class="sm:fixed sm:border-r sm:top-[21%] sm:flex sm:flex-col border-r-sky-800">
      <router-link to="/" class="relative m-4 p-3 group">
          <i class="py-4 px-4 hover:bg-sky-800 hover:text-slate-200 text-sky-800 bg-slate-200 rounded-3xl hover:cursor-pointer">
              <font-awesome-icon icon="fa-solid fa-house-chimney" />
          </i>
          <span class="absolute w-auto p-3 m-2 min-w-max left-0 bottom-10 rounded-md shadow-2xl text-sky-800 bg-slate-200
          text-xs font-bold transition-all scale-0  duration-300 ease-linear group-hover:scale-100">
              Home
          </span>
      </router-link>
      <router-link to="/" class="relative m-4 p-3 group">
           <i class="py-4 px-4 hover:bg-sky-800 hover:text-slate-200 text-sky-800 bg-slate-200 rounded-3xl hover:cursor-pointer">
              <font-awesome-icon icon="fa-solid fa-stethoscope" />
          </i>
          <span class="absolute w-auto p-3 m-2 min-w-max left-0 bottom-10 rounded-md shadow-2xl text-sky-800 bg-slate-200
          text-xs font-bold transition-all scale-0  duration-300 ease-linear group-hover:scale-100">
              Profile
          </span>
      </router-link>
      <router-link to="messages" class="relative m-4 p-3 group">
           <i class="py-4 px-4 hover:bg-sky-800 hover:text-slate-200 text-sky-800 bg-slate-200 rounded-3xl hover:cursor-pointer">
              <font-awesome-icon icon="fa-solid fa-message" />
          </i>
          <span class="absolute w-auto p-3 m-2 min-w-max left-0 bottom-10 rounded-md shadow-2xl text-sky-800 bg-slate-200
          text-xs font-bold transition-all scale-0  duration-300 ease-linear group-hover:scale-100">
              Nachrichten
          </span>
      </router-link>
      <router-link to="patients" class="relative m-4 p-3 group">
           <i class="py-4 px-4 hover:bg-sky-800 hover:text-slate-200 text-sky-800 bg-slate-200 rounded-3xl hover:cursor-pointer">
              <font-awesome-icon icon="fa-solid fa-users" />
          </i>
          <span class="absolute w-auto p-3 m-2 min-w-max left-0 bottom-10 rounded-md shadow-2xl text-sky-800 bg-slate-200
          text-xs font-bold transition-all scale-0  duration-300 ease-linear group-hover:scale-100">
              Alle Patienten
          </span>
      </router-link>
      <router-link to="contact" class="relative m-4 p-3 group">
           <i class="py-4 px-4 hover:bg-sky-800 hover:text-slate-200 text-sky-800 bg-slate-200 rounded-3xl hover:cursor-pointer">
              <font-awesome-icon icon="fa-solid fa-envelope" />
          </i>
          <span class="absolute w-auto p-3 m-2 min-w-max left-0 bottom-10 rounded-md shadow-2xl text-sky-800 bg-slate-200
          text-xs font-bold transition-all scale-0  duration-300 ease-linear group-hover:scale-100">
              Kontakt
          </span>
      </router-link>
  </div>
</template>