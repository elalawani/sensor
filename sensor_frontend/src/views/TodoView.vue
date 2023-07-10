<template>
    <div class="container mx-auto mt-10 p-4">
        <div class="flex flex-col justify-center">
            <h1 class="text-4xl font-extrabold mb-4">Todo</h1>
            <ul class="flex flex-col h-screen overflow-auto">
                <li
                    v-for="(task, index) in tasks"
                    :key="index"
                    class="px-2 py-4 bg-slate-800 mb-1 flex flex-row justify-between items-center
                    hover:border-b border-b-slate-500 hover:shadow-inner"
                >
                    <span
                        v-if="!task.editing"
                        class="py-2 px-4 mb-4 rounded cursor-pointer"
                        @click="editTask(task, index)"
                    >
                        <span>{{index+1}} - </span>{{ task.name }}
                        <div>{{task.created_at}}</div>
                    </span>
                    <input
                        v-else
                        :ref="`editInput-${index}`"
                        v-model="taskName"
                        class="bg-slate-800 border border-gray-300 rounded py-2 px-4 mb-4 w-full"
                        @blur="updateTask(task.id)"
                        @keydown.enter="updateTask(task.id)"
                    >
                    <div class="flex flex-row">
                        <button
                            @click="deleteTask(task.id)"
                            class="text-red-900 p-3 hover:text-red-700"
                        >
                            Delete
                        </button>
                        <button
                            @click="doneTasks(task)"
                            class="text-sky-900 p-3 hover:text-sky-700"
                        >
                            Done
                        </button>
                    </div>
                </li>
            </ul>
            <div class="mt-4">
                <input
                    type="text"
                    v-model="newTask"
                    class="border border-gray-300 rounded w-full py-2 px-4 mb-4"
                    placeholder="Enter a new task"
                    @keydown.enter="addTask"
                >
                <button
                    @click="addTask"
                    class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
                >
                    Add Task
                </button>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {

    data() {
        return {
            tasks: [],
            newTask: '',
            taskName: '',
        };
    },
    methods: {
        editTask(task, index) {
            this.tasks.forEach((t) => {
                if (t !== task) t.editing = false;
            });
            task.editing = true;
            this.taskName = task.name;
            this.$nextTick(() => {
                this.$refs[`editInput-${index}`][0].focus();
            });
        },
        doneTasks(task) {
            // later after add a documentations can send done tasks there
        },
        updateTask(taskId) {
            console.log(this.taskName)
            axios.put(`api/todo/update/${taskId}/`, {
                name: this.taskName
            })
                .then(response => {
                    let task = this.tasks.find(task => task.id === taskId);
                    if (task) {
                        task.name = this.taskName;
                        task.editing = false;
                    }
                }).catch(error => {
                console.log(error)
            })
        },
        deleteTask(index) {
            axios
                .delete(`api/todo/delete/${index}/`)
                .then( response => {
                    console.log(response.data)
                    window.location.reload();

                    }
                ).catch(error => {
                    console.log(error)
            })
        },
        addTask() {
            if (this.newTask !== '') {
                axios
                    .post('api/todo/create/', {
                        name: this.newTask
                    })
                    .then(
                        response => {
                            console.log(response.data)
                            this.newTask = ''
                            this.get_tasks()
                        }
                    ).
                catch(error => {
                    console.log(error)
                })

            }
        },
        get_tasks(){
            axios.get('api/todo/').then(response => {
                console.log(response.data)
                this.tasks = (response.data)
                console.log(this.tasks)
            }).catch(
                error => {
                    console.log(error)
                }
            )
        }
    },
    mounted() {
        this.get_tasks()
    }
};
</script>
