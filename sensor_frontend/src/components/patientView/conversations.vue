<template>
  <div class="flex flex-col h-full">
      <div
          v-for="(chat, index) in chats"
          :key="index"
      >
          <div
              v-if="chat.user.id === currentUser"
              class="m-2">
              <div class="flex flex-row-reverse items-center">
                  <div class="text-slate-400 p-4 rounded-full border border-slate-400 m-3">
                      <i class="items-center flex justify-center">
                          <font-awesome-icon icon="fa-solid fa-user" />
                      </i>
                  </div>
                  <div class="m-2">
                      <div class="rounded-lg rounded-tr-none shadow-xl border dark:border-none overflow-auto dark:bg-sky-900 w-fit px-10 py-1">
                          {{ chat.content }}
                      </div>
                      <span class="font-extralight text-xs">{{ chat.created_at_formatted }} ago</span>
                  </div>
              </div>
          </div>
          <div
              v-else
              class="m-5">
              <div class="flex flex-row items-center">
                  <div class="text-slate-400 p-4 rounded-full border border-slate-400 m-3">
                      <i class="items-center flex justify-center">
                          <font-awesome-icon icon="fa-solid fa-user" />
                      </i>
                  </div>
                  <div class="">
                      <div class="font-extralight mb-1 pr-2 hover:font-light text-xs flex justify-end">
                          <span
                              v-if="!tasksAdded[index]"
                              class="hover:cursor-pointer border-b border-b-slate-500"
                              @click="addTask(chat.content, index); editTask(index)"
                          >
                              add to Tasks
                          </span>
                      </div>
                      <div class="rounded-lg flex flex-col rounded-tl-none shadow-xl border dark:border-none overflow-auto dark:bg-slate-500 w-fit px-10 py-1">
                          {{ chat.content }}
                      </div>
                      <span class="font-extralight text-xs flex justify-end pr-2">{{ chat.created_at_formatted }} ago</span>
                  </div>
              </div>
          </div>
      </div>
      <div class="flex flex-row border-t border-t-slate-500 justify-around items-center p-2 w-full dark:bg-slate-600 bg-gray-50 mt-1 py-4 sticky bottom-0 px-3 backdrop-blur">
          <input
              type="text"
              class="shadow-xl w-full p-2 rounded-lg mx-2 dark:bg-slate-500 dark:text-slate-100 text-slate-900"
              placeholder="write anything"
              v-model="content"
          />
          <button
              @click="send_message"
              class="px-3 py-2 rounded-full dark:bg-sky-900 text-slate-100
                      dark:hover:bg-sky-700 bg-sky-700 hover:bg-sky-600"
          >
              <font-awesome-icon icon="fa-solid fa-paper-plane" />
          </button>
      </div>

  </div>
</template>
<script>
import axios from "axios";
import {useRoute} from "vue-router";
import {useUserStore} from "@/stores/user";
import {reactive} from "vue";

export default {
    name: 'conversation',
    setup() {

    },
    data() {
        return {
            content: '',
            tasksAdded: reactive({}),
            chats: [],
            conversation_id: '',
            patient_id: useRoute().params.id,
            currentUser: useUserStore().user.id
        }
    },
    mounted() {
        this.get_conversation()
        this.loadTasks()
    },
    methods: {
        loadTasks() {
            const tasksAddedStorage = JSON.parse(localStorage.getItem('tasksAdded'));
            if (tasksAddedStorage) {
                this.tasksAdded = tasksAddedStorage;
            }
        },
        async get_conversation() {
            console.log(this.conversation_id)
            await axios
                .get(`/api/conversation/${this.patient_id}`)
                .then(response => {
                    console.log(response.data)
                    this.conversation_id = response.data.id
                    console.log(this.conversation_id)
                    this.get_messages()
                })
                .catch(error => {
                    console.log(error)
                })
        },
        async send_message() {
            const message = {
                content: this.content,
            };
            console.log(this.conversation_id)
            await axios
                .post(`/api/conversation/${this.conversation_id}/message/`, message)
                .then(
                    response => {
                        console.log(response.data)
                        this.content = ''
                        this.get_messages()
                    }
                )
                .catch(error =>{
                    console.log(error.response.data)
                })
        },
        async get_messages() {
            console.log(this.conversation_id)
            await axios
                .get(`/api/conversation/${this.conversation_id}/messages/`)
                .then(response => {
                    this.chats = response.data
                })
                .catch(error =>{
                    console.log(error.response.data)
                })
        },
        addTask(text, num) {
            axios
                .post('api/todo/create/', {
                    name: text
                })
                .then(
                    response => {
                        console.log(response.data)
                        this.tasksAdded[num] = true;
                        this.saveTasks();

                    }
                ).
            catch(error => {
                console.log(error)
            })

        },
        editTask(num) {
         this.tasksAdded[num] = true;
         this.saveTasks();

        },
        saveTasks() {
            localStorage.setItem('tasksAdded', JSON.stringify(this.tasksAdded));
        },
    },
}


</script>