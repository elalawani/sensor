<template class="border-b">
    <div class="flex flex-row h-full justify-around">
        <div class="left flex flex-col justify-center items-center border-r border-r-slate-500 w-full p-2">
            <div class="text-slate-700 dark:text-slate-100 font-bold p-4 w-full">patient: {{patient[0].firstName}}</div>
            <div class="flex flex-row p-2 justify-around items-center w-full ">
                <div class="relative text-slate-700 dark:text-slate-100 overflow-hidden shadow-lg flex flex-col items-center
                justify-center p-2 rounded-br-lg w-full m-1 dark:bg-slate-500">
                    <div class="w-full text-xl font-extrabold px-4 py-2">
                       <span>
                            37.3 °C
                       </span>
                        <i class="dark:text-sky-900 text-sky-700 px-3">
                            <font-awesome-icon size="xl" icon="fa-solid fa-temperature-half" />
                        </i>
                    </div>
                    <div class="w-fit font-bold my-2">
                        Körper Temperature
                    </div>
                    <div class="font-extralight w-full text-xs">
                            am 12.12.2023
                    </div>
                     <i class="dark:bg-sky-900 bg-sky-700 absolute px-3 py-1 bottom-[-1px] right-[-1px] text-gray-50 rounded-br-lg rounded-tl-lg">
                      <font-awesome-icon icon="fa-solid fa-info" />
                  </i>
                </div>
            <div class="relative text-slate-700 dark:text-slate-100 overflow-hidden shadow-lg flex flex-col items-center
                justify-center p-2 rounded-br-lg w-full m-1 dark:bg-slate-500">
                    <div class="w-full text-xl font-extrabold px-4 py-2">
                       <span>
                            37.3 °C
                       </span>
                        <i class="dark:text-sky-900 text-sky-700 px-3">
                            <font-awesome-icon size="xl" icon="fa-solid fa-temperature-half" />
                        </i>
                    </div>
                    <div class="w-fit font-bold my-2">
                        Körper Temperature
                    </div>
                    <div class="font-extralight w-full text-xs">
                            am 12.12.2023
                    </div>
                     <i class="dark:bg-sky-900 bg-sky-700 absolute px-3 py-1 bottom-[-1px] right-[-1px] text-gray-50 rounded-br-lg rounded-tl-lg">
                      <font-awesome-icon icon="fa-solid fa-info" />
                  </i>
                </div>
            </div>
            <div class="w-full">
                <div class="m-2 text-slate-900 dark:text-slate-100">
                last measurement of: <span class="text-sky-700 border-b">name of clicked one</span>
                </div>
                <div class="w-full">
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
        <div class="right flex flex-col w-full p-2">
            <div class="flex flex-row justify-around items-center w-full h-full">
                <div class="relative text-slate-700 dark:text-slate-100 overflow-hidden shadow-lg flex flex-col items-center
                            justify-center p-1 rounded-tl-xl rounded-br-lg w-full h-fit  m-1 dark:bg-slate-500">
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
                            justify-center p-1 rounded-tl-xl rounded-br-lg w-full h-fit  m-1 dark:bg-slate-500">
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


            </div>
           <div class="flex flex-row justify-around items-center w-full h-full">
                <div class="relative text-slate-700 dark:text-slate-100 overflow-hidden shadow-lg flex flex-col items-center
                            justify-center p-2 rounded-tl-xl rounded-br-lg w-full h-fit m-1 dark:bg-slate-500">
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
                            justify-center p-2 rounded-tl-xl rounded-br-lg w-full h-fit m-1 dark:bg-slate-500">
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
            <div class="flex flex-row justify-around items-center w-full h-full">
                <div class="relative text-slate-700 dark:text-slate-100 overflow-hidden shadow-lg flex flex-col items-center
                            justify-center p-2 rounded-tl-xl rounded-br-lg w-full h-fit m-1 dark:bg-slate-500">
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
                            justify-center p-2 rounded-tl-xl rounded-br-lg w-full h-fit m-1 dark:bg-slate-500">
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
            <div>
                <bar
                    id="my-chart-id"
                    :options="chartOptions"
                    :data="chartData"
                    class="p-5 h-full"
                />
            </div>

        </div>
    </div>
</template>
<script>
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)


export default {
    data() {
        return {
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
        labels: [ 'January', 'February', 'March' ],
        datasets: [ { data: [40, 20, 12] } ]
      },
      chartOptions: {
        responsive: true
      }
        }
    },
    components: {
        Bar,
    }
}


</script>

