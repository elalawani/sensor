<template>
  <div class="grid grid-cols-2 bg-gray-200 text-slate-900 mr-5">
      <div class="flex col-span-1 border-r border-r-slate-400 items-center text-center flex-col px-2 py-5">
          <i class="px-6 py-5 bg-gray-400 text-gray-50 rounded-full mb-5">
              <font-awesome-icon size="4x" icon="fa-solid fa-user" />
          </i>
          <div class="font-bold text-2xl"> test </div>
          <div class="text-gray-500 mb-6">  test</div>
          <div class="p-3"> Termine </div>
          <div class="flex flex-row ">
              <div class="px-3 my-3 border-r border-r-slate-300">
                  <span class="font-bold">4</span><br>
                  <span class="text-gray-400"> vergangen </span>
              </div>
              <div class="px-3 my-3">
                  <span class="font-bold">2</span><br>
                  <span class="text-gray-400"> active </span>
              </div>
          </div>
          <button class="text-gray-50 py-3 px-8 rounded-xl bg-sky-800 hover:bg-sky-600 my-3"> Send Email </button>
      </div>
      <div class="grid grid-cols-2">
          <div class="col-span-1">
              <div class="grid grid-rows-4">
                  <div class="grid row-span-1 text-start ml-4 p-5">
                      <span class="text-gray-400 inline-block mb-4">Gender</span>
                      <span class="border-b border-b-slate-300 pb-2">test</span>
                  </div>
                  <div class="grid row-span-1 text-start ml-4 p-5">
                      <span class="text-gray-400 inline-block mb-4">Phone</span>
                      <span class="border-b border-b-slate-300 pb-2 whitespace-nowrap">test</span>
                  </div>
                  <div class="grid row-span-1 text-start ml-4 p-5">
                      <span class="text-gray-400 inline-block mb-4">City</span>
                      <span class="border-b border-b-slate-300 pb-2">test</span>
                  </div>
                  <div class="grid row-span-1 text-start ml-4 p-5">
                      <span class="text-gray-400 inline-block mb-4">active seit</span>
                      <span class=" pb-2">12.05.2020</span>
                  </div>
              </div>
          </div>
          <div class="col-span-1">
              <div class="grid grid-rows-4">
                  <div class="grid row-span-1 text-start ml-4 p-5">
                      <span class="text-gray-400 inline-block mb-4">birthdate</span>
                      <span class="border-b border-b-slate-300 pb-2">test</span>
                  </div>

                  <div class="grid row-span-1 text-start ml-4 p-5">
                      <span class="text-gray-400 inline-block mb-4">Address</span>
                      <span class="border-b border-b-slate-300 pb-2">test</span>
                  </div>
                  <div class="grid row-span-1 text-start ml-4 p-5">
                      <span class="text-gray-400 inline-block mb-4">PLZ</span>
                      <span class="border-b border-b-slate-300 pb-2">test</span>
                  </div>
                  <div class="grid row-span-1 text-start ml-4 p-5">
                      <span class="text-gray-400 inline-block mb-4">Status</span>
                      <span class=" pb-2">im Haus</span>
                  </div>
              </div>
          </div>


      </div>
  </div>
</template>
<script>
export default {
    name: 'patientInfo',
}
</script>