<template>
    <div class="p-5">
         <div
                class="flex justify-center p-6 items-center"
        >
            <h1 class="text-4xl">
                please select a measurement to add
            </h1>
        </div>

        <div class="flex flex-row space-x-4 items-center justify-around overflow-auto w-full">
            <button
                v-for="(myOption, index) in options"
                :key="index"
                class="p-4 bg-slate-500 rounded shadow-xl h-20"
                @click="option = myOption"
        >
                {{myOption}}
            </button>
        </div>
    </div>
  <div v-if="option === 'temperature'">
      <add-temperature/>
  </div>
  <div v-if="option === 'blood cholesterol'">
      <add-blood-cholesterol/>
  </div>
  <div v-if="option === 'blood glucose'">
      <add-blood-glucose/>
  </div>
  <div v-if="option === 'blood pressure'">
      <add-blood-pressure/>
  </div>
  <div v-if="option === 'heart rate'">
      <add-heart-rate/>
  </div>
  <div v-if="option === 'parkinson'">
      <add-parkinson/>
  </div>
  <div v-if="option === 'respiration rate'">
      <add-respiration-rate/>
  </div>
</template>
<script>

import AddTemperature from "@/components/dataForms/addTemperature.vue";
import AddBloodCholesterol from "@/components/dataForms/addBloodCholesterol.vue";
import AddBloodGlucose from "@/components/dataForms/addBloodGlucose.vue";
import AddBloodPressure from "@/components/dataForms/addBloodPressure.vue";
import AddHeartRate from "@/components/dataForms/addHeartRate.vue";
import AddParkinson from "@/components/dataForms/addParkinson.vue";
import AddRespirationRate from "@/components/dataForms/addRespirationRate.vue";

export default {
    name: 'NewDataFormView',
    data() {
        return {
            option: '',
            options: [
                'parkinson',
                'temperature',
                'heart rate',
                'blood pressure',
                'blood glucose',
                'respiration rate',
                'blood cholesterol'
            ],
        }
    },

    components: {
        AddRespirationRate,
        AddParkinson,
        AddHeartRate,
        AddBloodPressure,
        AddBloodGlucose,
        AddBloodCholesterol,
        AddTemperature

    }
}
</script>