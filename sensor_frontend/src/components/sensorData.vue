<template>
  <div class="grid grid-cols-2 bg-gray-200 text-slate-900 mr-5">
      <div class=" text-center p-3">
          <div>
              <div class="py-5 border"> die Messungen von Patient id: {{patient[0].id}}</div>
          </div>
          <div class="row-span-2 grid grid-cols-2">
              <div class="p-4 m-2 bg-gray-50 shadow-lg text-center">
                  <span class=" text-sky-600"> 50 % </span><br>
                  <span class="mb-4 inline-block"> sleep </span><br>
                  <div class="mb-3">
                      <span class="p-3 border-r" >  {{ patient[0].measurements.sleep }} </span>
                      <span class="p-3"> {{ patient[0].measurements.sleep }}</span>
                  </div>

                  <span class="text-gray-400 mr-3">max sleep</span>
                  <span class="text-gray-400 ml-3"> sleep</span>
              </div>
              <div class="p-4 m-2 bg-gray-50 shadow-lg text-center">
                  <span class=" text-sky-600"> 50 % </span><br>
                  <span class="mb-4 inline-block"> example </span><br>
                  <div class="mb-3">
                      <span class="p-3 border-r" >  22 </span>
                      <span class="p-3"> 15 </span>
                  </div>

                  <span class="text-gray-400 mr-3">max </span>
                  <span class="text-gray-400 ml-3"> normal</span>
              </div>
          </div>
          <div class="row-span-3 ">
              <div class="text-start ml-8 p-4">
                  letzte messungen:
              </div>
              <div class="justify-between bg-gray-50">
                  <table id="customers" class="w-full  p-8 border ">
                      <thead class="bg-slate-400">
                      <tr>
                          <th>name</th>
                          <th>date</th>
                          <th>type</th>
                          <th>result</th>
                      </tr>
                      </thead>
                      <tbody>
                      <tr>
                          <td>herz</td>
                          <td>12.05.2023</td>
                          <td>-</td>
                          <td>80.20 pbH</td>

                      </tr>
                       <tr>
                          <td>herz</td>
                          <td>04.05.2023</td>
                          <td>-</td>
                          <td>80.80 pbH</td>

                      </tr>
                       <tr>
                          <td>herz</td>
                          <td>01.05.2023</td>
                          <td>-</td>
                          <td>80.00 pbH</td>

                      </tr>
                       <tr>
                          <td>herz</td>
                          <td>12.05.2023</td>
                          <td>-</td>
                          <td>80.20 pbH</td>

                      </tr>
                       <tr>
                          <td>herz</td>
                          <td>04.05.2023</td>
                          <td>-</td>
                          <td>80.80 pbH</td>

                      </tr>
                       <tr>
                          <td>herz</td>
                          <td>01.05.2023</td>
                          <td>-</td>
                          <td>80.00 pbH</td>

                      </tr>
                      </tbody>
                  </table>
              </div>
          </div>
      </div>
      <div class="p-3">
          <div class="row-span-1 grid grid-cols-2 gap-2 pr-2">
              <div class="col-span-1 bg-gray-50 shadow-xl rounded-lg mb-2 relative">
                  <div class="px-3 relative top-2">
                      <span class="text-2xl font-bold"> {{patient[0].measurements.Temperature}}</span>
                  <i class="text-sky-800 px-3">
                      <font-awesome-icon size="xl" icon="fa-solid fa-temperature-half" />
                  </i>
                  </div>
                  <div class="pl-3 py-3 text-gray-500">
                      Körper Temperatur
                  </div>
                  <i class="bg-sky-800 absolute px-3 py-1 bottom-[-1px] right-[-1px] text-gray-50 rounded-br-lg rounded-tl-lg">
                      <font-awesome-icon icon="fa-solid fa-info" />
                  </i>
              </div>
              <div class="col-span-1 bg-gray-50 shadow-xl rounded-lg mb-2 relative">
                  <div class="px-3 relative top-2">
                      <span class="text-2xl font-bold"> {{patient[0].measurements.blood_cholesterol}}</span>
                  <i class="text-sky-800 px-3">
                      <font-awesome-icon size="xl" icon="fa-solid fa-droplet" />
                  </i>
                  </div>
                  <div class="pl-3 py-3 text-gray-500">
                      blut kolesterol
                  </div>
                  <i class="bg-sky-800 absolute px-3 py-1 bottom-[-1px] right-[-1px] text-gray-50 rounded-br-lg rounded-tl-lg">
                      <font-awesome-icon icon="fa-solid fa-info" />
                  </i>
              </div>
          </div>
          <div class="row-span-1 grid grid-cols-2 gap-2 pr-2">
              <div class="col-span-1 bg-gray-50 shadow-xl rounded-lg mb-2 relative">
                  <div class="px-3 relative top-2">
                      <span class="text-xl font-bold"> {{patient[0].measurements.heart_rate}}</span>
                  <i class="text-sky-800 px-3">
                      <font-awesome-icon size="xl" icon="fa-solid fa-heartbeat" />
                  </i>
                  </div>
                  <div class="pl-3 py-3 text-gray-500">
                      hertz rate
                  </div>
                  <i class="bg-sky-800 absolute px-3 py-1 bottom-[-1px] right-[-1px] text-gray-50 rounded-br-lg rounded-tl-lg">
                      <font-awesome-icon icon="fa-solid fa-info" />
                  </i>
              </div>
              <div class="col-span-1 bg-gray-50 shadow-xl rounded-lg mb-2 relative">
                  <div class="px-3 relative top-2">
                      <span class="text-2xl font-bold"> {{patient[0].measurements.Respiration_rate}}</span>
                  <i class="text-sky-800 px-3">
                      <font-awesome-icon size="xl" icon="fa-solid fa-lungs" />
                  </i>
                  </div>
                  <div class="pl-3 py-3 text-gray-500">
                      respirations rate
                  </div>
                  <i class="bg-sky-800 absolute px-3 py-1 bottom-[-1px] right-[-1px] text-gray-50 rounded-br-lg rounded-tl-lg">
                      <font-awesome-icon icon="fa-solid fa-info" />
                  </i>
              </div>
          </div>
          <div class="row-span-1 grid grid-cols-2 gap-2 pr-2">
              <div class="col-span-1 bg-gray-50 shadow-xl rounded-lg mb-2 relative">
                  <div class="px-3 relative top-2">
                      <span class="text-2xl font-bold"> {{patient[0].measurements.blood_glucose}}</span>
                  <i class="text-sky-800 px-3">
                      <font-awesome-icon size="xl" icon="fa-solid fa-droplet" />
                  </i>
                  </div>
                  <div class="pl-3 py-3 text-gray-500">
                      blut glokuse
                  </div>
                  <i class="bg-sky-800 absolute px-3 py-1 bottom-[-1px] right-[-1px] text-gray-50 rounded-br-lg rounded-tl-lg">
                      <font-awesome-icon icon="fa-solid fa-info" />
                  </i>
              </div>
              <div class="col-span-1 bg-gray-50 shadow-xl rounded-lg mb-2 relative">
                  <div class="px-3 relative top-2">
                      <span class="text-2xl font-bold"> {{patient[0].measurements.blood_pressure}}</span>
                  <i class="text-sky-800 px-3">
                      <font-awesome-icon size="xl" icon="fa-solid fa-droplet" />
                  </i>
                  </div>
                  <div class="pl-3 py-3 text-gray-500">
                      blut druck
                  </div>
                  <i class="bg-sky-800 absolute px-3 py-1 bottom-[-1px] right-[-1px] text-gray-50 rounded-br-lg rounded-tl-lg">
                      <font-awesome-icon icon="fa-solid fa-info" />
                  </i>
              </div>
          </div>
          <div class="row-span-2 shadow-lg border p-3 bg-gray-50">
              <bar
                   id="my-chart-id"
                    :options="chartOptions"
                    :data="chartData"
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

