<template>
    <div class="flex flex-row h-full">
        <div class="left flex flex-col items-center h-full border-r border-r-slate-500 w-full p-2">
            <div class="flex flex-col w-[80%]">
                <div class="flex flex-row border-b items-center border-b-slate-500">
                    <button
                        class="border-r border-r-slate-500 text-slate-500 overflow-hidden
                        flex flex-col items-center justify-center p-2 m-1 hover:font-bold"
                        @click="showChart"
                        :class="dataView === 'chart' ? 'font-extrabold dark:text-white ' : ''"
                    >
                        Chart
                    </button>
                    <button
                        class="text-slate-500 overflow-hidden
                        flex flex-col items-center justify-center p-2 m-1 hover:font-bold"
                        @click="showTable"
                        :class="dataView === 'table' ? 'font-extrabold dark:text-white' : ''"
                    >
                        table
                    </button>
                </div>
                <div  class="h-full justify-center shadow dark:bg-slate-800 mt-1">
                    <Line
                        v-if="dataView === 'chart'"
                        :data="chartData"
                        :options="chartOptions"
                    />
                    <div
                        v-else-if="dataView === 'table'"
                        class="w-full">
                        <div class="shadow-md rounded-lg">
                            <table class="rounded text-sm text-left text-slate-500 dark:text-slate-100 w-full">
                                <thead class="text-slate-100 bg-sky-700 uppercase dark:bg-sky-900 dark:text-slate-300">
                                <tr>
                                    <th class="pl-2 py-3">
                                        nr.
                                    </th>
                                    <th class="pl-4 py-3">
                                        Date
                                    </th>
                                    <th class="pl-4 py-3">
                                        Evaluation
                                    </th>
                                    <th class="px-4 py-3">
                                        measure
                                    </th>
                                </tr>
                                </thead>
                                <tbody>
                                <tr class="border-b dark:bg-slate-800 dark:border-slate-700 hover:shadow  dark:hover:bg-slate-700">
                                    <th class="pl-2 py-4">
                                        1.
                                    </th>
                                    <td class="pl-4 py-4">
                                        19.12.2022
                                    </td>
                                    <td class="pl-4 py-4">
                                        3 of 5
                                    </td>
                                    <td class="px-4 py-4">
                                        37.3 °C
                                    </td>
                                </tr>
                                <tr class="border-b dark:bg-slate-800 dark:border-slate-700 hover:shadow  dark:hover:bg-slate-700">
                                    <th class="pl-2 py-4">
                                        2.
                                    </th>
                                    <td class="pl-4 py-4">
                                        18.12.2022
                                    </td>
                                    <td class="pl-4 py-4">
                                        4 of 5
                                    </td>
                                    <td class="px-4 py-4">
                                        37.3 °C
                                    </td>
                                </tr>
                                <tr class="border-b dark:bg-slate-800 dark:border-slate-700 hover:shadow dark:hover:bg-slate-700">
                                    <th class="pl-2 py-4">
                                        3.
                                    </th>
                                    <td class="pl-4 py-4">
                                        15.12.2022
                                    </td>
                                    <td class="pl-4 py-4">
                                        3 of 5
                                    </td>
                                    <td class="px-4 py-4">
                                        37.3 °C
                                    </td>
                                </tr>
                                </tbody>

                            </table>
                        </div>

                    </div>
                </div>
            </div>
            <div
                class="relative max-h-[50%] overflow-auto mt-3"
                v-if="dataView === 'chart'">
                <div class="font-bold dark:bg-slate-600 sticky top-0 px-3 backdrop-blur dark:text-slate-100 text-slate-700">
                    comments
                </div>
                <div class="rounded shadow-xl border dark:border-none overflow-auto dark:bg-slate-600">
                    <div class="flex flex-col  rounded-tl-xl rounded-tr-xl rounded-br-xl dark:bg-slate-500 bg-sky-700 w-fit text-slate-100 p-2 my-2 mx-6">
                        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eaque, et!
                    </div>
                    <div class="flex flex-col  rounded-tl-xl rounded-tr-xl rounded-br-xl dark:bg-slate-500 bg-sky-700 w-fit text-slate-100 p-2 my-2 mx-6">
                        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eaque, et!
                    </div>
                    <div class="flex flex-col rounded-tl-xl rounded-tr-xl rounded-br-xl dark:bg-slate-500 bg-sky-700 w-fit text-slate-100 p-2 my-2 mx-6">
                        Lorem ipsum, et!
                    </div>
                    <div class="flex flex-col  rounded-tl-xl rounded-tr-xl rounded-br-xl dark:bg-slate-500 bg-sky-700 w-fit text-slate-100 p-2 my-2 mx-6">
                        Lorem ipsum, et!
                    </div>
                    <div class="flex flex-col  rounded-tl-xl rounded-tr-xl rounded-br-xl dark:bg-slate-500 bg-sky-700 w-fit text-slate-100 p-2 my-2 mx-6">
                        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eaque, et!
                    </div>
                </div>
                <div class="flex flex-row border-t border-t-slate-500 justify-around items-center p-2 w-full dark:bg-slate-600 bg-gray-50 mt-1 py-4 sticky bottom-0 px-3 backdrop-blur">
                    <input type="text" class="shadow-xl w-full p-2 rounded-lg mx-2 dark:bg-slate-500 dark:text-slate-100 text-slate-900" placeholder="add Comment"/>
                    <button class="px-3 py-2 rounded-full dark:bg-sky-900 text-slate-100 dark:hover:bg-sky-700
                    bg-sky-700 hover:bg-sky-600"
                    >
                        comment
                    </button>
                </div>
            </div>
        </div>
        <div class=" flex flex-col w-[50%] p-2">
            <div class="mb-16 space-y-2 flex flex-col items-center">
                <router-link :to="`/patients/${id}/add_data`" class="p-2 bg-sky-700 rounded">add data +</router-link>
                <label class="text-sm font-medium text-gray-900 dark:text-white" for="file_input">or Upload FHIR</label>
                <input
                    class=" text-sm text-slate-700 border border-slate-500 rounded-lg cursor-pointer
                    bg-gray-50 dark:text-slate-300 focus:outline-none dark:bg-slate-500 dark:border-slate-600
                    dark:placeholder-gray-400"
                    aria-describedby="file_input_help"
                    id="file_input"
                    type="file"
                >
            </div>
            <div class="overflow-auto h-1/2 relative">
                <div class="relative text-slate-700 dark:text-slate-100 overflow-hidden shadow-lg flex flex-col items-center
                            justify-center p-1 rounded-xl w-full my-1 dark:bg-slate-500">
                <div class="w-full font-extrabold px-2 py-1">
                    <span>
                        37.3 °C
                    </span>
                    <i class="dark:text-sky-900 text-sky-700 px-2">
                        <font-awesome-icon size="xl" icon="fa-solid fa-temperature-half" />
                    </i>
                </div>
                <div class="w-full">
                    Körper Temperature
                </div>
                <i class="dark:bg-sky-900 bg-sky-700 absolute px-2 bottom-[-1px] right-[-1px] text-gray-50 rounded-br-lg rounded-tl-lg">
                    <font-awesome-icon icon="fa-solid fa-info" />
                </i>
            </div>
                <div class="relative text-slate-700 dark:text-slate-100 overflow-hidden shadow-lg flex flex-col items-center
                            justify-center p-1 rounded-xl w-full my-1 dark:bg-slate-500">
                <div class="w-full font-extrabold px-2 py-1">
                    <span>
                        37.3 °C
                    </span>
                    <i class="dark:text-sky-900 text-sky-700 px-2">
                        <font-awesome-icon size="xl" icon="fa-solid fa-temperature-half" />
                    </i>
                </div>
                <div class="w-full">
                    Körper Temperature
                </div>
                <i class="dark:bg-sky-900 bg-sky-700 absolute px-2 bottom-[-1px] right-[-1px] text-gray-50 rounded-br-lg rounded-tl-lg">
                    <font-awesome-icon icon="fa-solid fa-info" />
                </i>
            </div>
                <div class="relative text-slate-700 dark:text-slate-100 overflow-hidden shadow-lg flex flex-col items-center
                            justify-center p-1 rounded-xl w-full my-1 dark:bg-slate-500">
                <div class="w-full font-extrabold px-2 py-1">
                    <span>
                        37.3 °C
                    </span>
                    <i class="dark:text-sky-900 text-sky-700 px-2">
                        <font-awesome-icon size="xl" icon="fa-solid fa-temperature-half" />
                    </i>
                </div>
                <div class="w-full">
                    Körper Temperature
                </div>
                <i class="dark:bg-sky-900 bg-sky-700 absolute px-2 bottom-[-1px] right-[-1px] text-gray-50 rounded-br-lg rounded-tl-lg">
                    <font-awesome-icon icon="fa-solid fa-info" />
                </i>
            </div>
                <div class="relative text-slate-700 dark:text-slate-100 overflow-hidden shadow-lg flex flex-col items-center
                            justify-center p-1 rounded-xl w-full my-1 dark:bg-slate-500">
                <div class="w-full font-extrabold px-2 py-1">
                    <span>
                        37.3 °C
                    </span>
                    <i class="dark:text-sky-900 text-sky-700 px-2">
                        <font-awesome-icon size="xl" icon="fa-solid fa-temperature-half" />
                    </i>
                </div>
                <div class="w-full">
                    Körper Temperature
                </div>
                <i class="dark:bg-sky-900 bg-sky-700 absolute px-2 bottom-[-1px] right-[-1px] text-gray-50 rounded-br-lg rounded-tl-lg">
                    <font-awesome-icon icon="fa-solid fa-info" />
                </i>
            </div>
                <div class="relative text-slate-700 dark:text-slate-100 overflow-hidden shadow-lg flex flex-col items-center
                            justify-center p-1 rounded-xl w-full my-1 dark:bg-slate-500">
                <div class="w-full font-extrabold px-2 py-1">
                    <span>
                        37.3 °C
                    </span>
                    <i class="dark:text-sky-900 text-sky-700 px-2">
                        <font-awesome-icon size="xl" icon="fa-solid fa-temperature-half" />
                    </i>
                </div>
                <div class="w-full">
                    Körper Temperature
                </div>
                <i class="dark:bg-sky-900 bg-sky-700 absolute px-2 bottom-[-1px] right-[-1px] text-gray-50 rounded-br-lg rounded-tl-lg">
                    <font-awesome-icon icon="fa-solid fa-info" />
                </i>
            </div>
                <div class="relative text-slate-700 dark:text-slate-100 overflow-hidden shadow-lg flex flex-col items-center
                            justify-center p-1 rounded-xl w-full my-1 dark:bg-slate-500">
                <div class="w-full font-extrabold px-2 py-1">
                    <span>
                        37.3 °C
                    </span>
                    <i class="dark:text-sky-900 text-sky-700 px-2">
                        <font-awesome-icon size="xl" icon="fa-solid fa-heartbeat" />
                    </i>
                </div>
                <div class="w-full">
                    hertz rate
                </div>
                <i class="dark:bg-sky-900 bg-sky-700 absolute px-2 bottom-[-1px] right-[-1px] text-gray-50 rounded-br-lg rounded-tl-lg">
                    <font-awesome-icon icon="fa-solid fa-info" />
                </i>
            </div>
                 <div class="relative text-slate-700 dark:text-slate-100 overflow-hidden shadow-lg flex flex-col items-center
                            justify-center p-2 rounded-xl w-full my-1 dark:bg-slate-500">
                <div class="w-full font-extrabold px-2 py-1">
                    <span>
                        37.3 °C
                    </span>
                    <i class="dark:text-sky-900 text-sky-700 px-2">
                        <font-awesome-icon size="xl" icon="fa-solid fa-temperature-half" />
                    </i>
                </div>
                <div class="w-full">
                    Körper Temperature
                </div>
                <i class="dark:bg-sky-900 bg-sky-700 absolute px-2 bottom-[-1px] right-[-1px] text-gray-50 rounded-br-lg rounded-tl-lg">
                    <font-awesome-icon icon="fa-solid fa-info" />
                </i>
            </div>
                 <div class="relative text-slate-700 dark:text-slate-100 overflow-hidden shadow-lg flex flex-col items-center
                            justify-center p-2 rounded-xl w-full my-1 dark:bg-slate-500">
                <div class="w-full font-extrabold px-2 py-1">
                    <span>
                        37.3 °C
                    </span>
                    <i class="dark:text-sky-900 text-sky-700 px-2">
                        <font-awesome-icon size="xl" icon="fa-solid fa-temperature-half" />
                    </i>
                </div>
                <div class="w-full">
                    Körper Temperature
                </div>
                <i class="dark:bg-sky-900 bg-sky-700 absolute px-2 bottom-[-1px] right-[-1px] text-gray-50 rounded-br-lg rounded-tl-lg">
                    <font-awesome-icon icon="fa-solid fa-info" />
                </i>
            </div>
            </div>
        </div>
    </div>
</template>
<script>
import { Line } from 'vue-chartjs'
import {Chart as ChartJS, Title, Tooltip, Legend, CategoryScale, LinearScale, LineElement, PointElement} from 'chart.js'
import {useRoute} from "vue-router";

ChartJS.register(Title,Legend, Tooltip, LineElement, PointElement, CategoryScale, LinearScale)


export default {
    data() {
        return {
            dataView: 'chart',
            id: '',
            patient: [{
                'id': 1,
                'firstName': 'Alice',
                'lastName': "Smith",
                'gender': 'Female',
                'dateOfBirth': '1990-03-12',
                'address': {
                    "street": "456 Elm St",
                    "city": "Los Angeles",
                    "state": "CA",
                    "zipcode": "90001"
                },
                "contact": {
                    "email": "alice.smith@example.com",
                    "phone": "+1 (555) 987-6543"
                },
                "medicalHistory": {
                    "allergies": ["Dust", "Pollen"]
                },
                'measurements': {
                    'heart_rate': '80.20 pbh',
                    'blood_pressure': '120 mmHg',
                    'blood_glucose': '120 mg/dL',
                    'Respiration_rate': '15bpm',
                    'Temperature': '37 °C',
                    'sleep': '6 hr',
                    'blood_cholesterol': '210 mg/dL',
                },
                "chronicConditions": ["Asthma"],
                "medications": ["Albuterol"],
                "surgeries": []
            }
            ],
            chartData: {
                labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
                datasets: [{
                    label: 'Data One',
                    backgroundColor: '#0369a1',
                    data: [40, 39, 10, 40, 39, 80, 40],
                }],

            },
            chartOptions: {
                responsive: true,
            }
        }
    },
    components: {
        Line,
    },
    mounted() {
      this.id = useRoute().params.id
    },
    methods: {
        showTable() {
            this.dataView = 'table';
        },
        showChart() {
            this.dataView = 'chart';
        },
    }
}


</script>

