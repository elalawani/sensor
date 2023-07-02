<template>
  <div class="bg-gray-200 text-slate-900 rounded-xl mr-5 min-w-max min-h-screen">
      <div class="col-span-3 space-y-4">
          <div class="bg-gray-100 shadow">
              <div class="flex grow flex-col p-4">
                  <div class="flex w-full mt-2 space-x-3 ml-auto justify-end">
                      <div>
                          <span class="text-xs text-gray-400 underline hover:cursor-pointer hover:text-slate-900">
                              add to my tasks
                          </span>
                          <div class="bg-sky-800 text-gray-50 p-3">
                              <p class="text-sm">
                                  Lorem ipsum dolor sit amet, consectetur adipisicing elit. Doloribus non quo tempore.
                              </p>
                          </div>
                          <span class="text-xs text-gray-400 leading-none">2 min ago</span>
                      </div>
                      <div class="flex-shrink-0 h-10 w-10">
                          <i class="py-4 px-4 text-gray-900 bg-slate-200 rounded-full">
                              <font-awesome-icon icon="fa-solid fa-user" />
                          </i>
                      </div>
                  </div>
                  <div class="flex w-full mt-2 space-x-3 max-w-md ml-auto justify-end">
                      <div>
                            <span class="text-xs text-gray-400 underline hover:cursor-pointer hover:text-slate-900">
                              add to my tasks
                          </span>
                          <div class="bg-sky-800 text-gray-50 p-3 rounded-l-lg rounded-br-lg">
                              <p class="text-sm">
                                  Lorem ipsum dolor sit amet, consectetur adipisicing elit. Consequuntur cum enim, esse
                                  fugit molestias nam perspiciatis quis! Accusantium commodi consectetur debitis delectus
                                  dignissimos eligendi explicabo, fugit incidunt labore minus modi, nostrum, obcaecati
                                  officiis pariatur perspiciatis repudiandae sed ullam unde vel vero. Accusamus adipisci
                                  distinctio hic iure molestiae quas quasi rem reprehenderit sunt totam. Adipisci labore
                                  nemo perferendis saepe vero. Architecto distinctio iusto labore quae quod? Animi blanditiis
                                  culpa cum dolor dolore enim hic illo ipsum, itaque laudantium magnam magni maxime nisi nobis
                                  odit quam quasi tempora tenetur veritatis voluptatum.
                                  Autem dolore eos eveniet explicabo laboriosam, perferendis quam ullam voluptates. In?
                              </p>
                          </div>
                          <span class="text-xs text-gray-400 leading-none">2 min ago</span>
                      </div>
                      <div class="flex-shrink-0 h-10 w-10">
                          <i class="py-4 px-4 text-gray-900 bg-slate-200 rounded-full">
                              <font-awesome-icon icon="fa-solid fa-user" />
                          </i>
                      </div>
                  </div>
                  <div class="flex w-full mt-2 space-x-3 max-w-md ml-auto justify-end">
                      <div>
                            <span class="text-xs text-gray-400 underline hover:cursor-pointer hover:text-slate-900">
                              add to my tasks
                          </span>
                          <div class="bg-sky-800 text-gray-50 p-3 rounded-l-lg rounded-br-lg">
                              <p class="text-sm">
                                  Lorem
                              </p>
                          </div>
                          <span class="text-xs text-gray-400 leading-none">2 min ago</span>
                      </div>
                      <div class="flex-shrink-0 h-10 w-10">
                          <i class="py-4 px-4 text-gray-900 bg-slate-200 rounded-full">
                              <font-awesome-icon icon="fa-solid fa-user" />
                          </i>
                      </div>
                  </div>
                  <div class="flex w-full mt-2 space-x-3 max-w-md">
                      <div class="flex-shrink-0 h-10 w-10">
                          <i class="py-4 px-4 text-gray-900 bg-slate-200 rounded-full">
                              <font-awesome-icon icon="fa-solid fa-user" />
                          </i>
                      </div>
                      <div>
                            <span class="text-xs text-gray-400 underline hover:cursor-pointer hover:text-slate-900">
                              add to my tasks
                          </span>
                          <div class="text-gray-900 bg-gray-200 p-3 rounded-r-lg rounded-bl-lg">
                              <p class="text-sm">
                                  Lorem ipsum  adipisicing elit. Doloribus non quo tempore.
                              </p>
                          </div>
                          <span class="text-xs text-gray-400 leading-none">4 min ago</span>
                      </div>

                  </div>
              </div>
          </div>
      <div class="bg-gray-50 ">
              <div class="p-4 relative">
                  <textarea class="p-1 w-[90%] border rounded-lg text-gray-900" placeholder="write anything"></textarea>
                  <a href="#" class="py-4 px-5 hover:bg-sky-800 bg-slate-200 text-sky-800 hover:text-slate-200 rounded-full absolute top-5 right-3 cursor-pointer">
                      <font-awesome-icon icon="fa-solid fa-paper-plane" />
                  </a>
              </div>

          </div>
      </div>
  </div>
</template>
<script>



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
                "chronicConditions": ["Asthma"],
                "medications": ["Albuterol"],
                "surgeries": []
            }
            ]
        }
    }
}


</script>