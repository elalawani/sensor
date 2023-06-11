<template>
        <signup-form v-if="formState === 'signup'" @closeForm="formState = ''" @changeForm="showForm('login')"/>
        <login-form v-if="formState === 'login'" @closeForm="formState = ''" @changeForm="showForm('signup')"/>
    <div v-else class="flex items-center justify-center space-x-5 px-6 py-8 h-screen">
        <button
            class="p-3 bg-sky-800 rounded-lg hover:bg-sky-600"
            v-if="formState === ''" @click="showForm('login')"
        >
            Sign in
        </button>
        <button
            class="p-3 bg-slate-500 rounded-lg hover:bg-slate-400"
            v-if="formState === ''" @click="showForm('signup')"
        >
            Sign up
        </button>
    </div>
</template>

<script>
import loginForm from '../components/loginForm.vue'
import signupForm from '../components/signupForm.vue'
export default {
    components: {
        loginForm,
        signupForm
    },

    data() {
        return {
            formState: '',
        }
    },
    methods: {
    showForm(form) {
      this.formState = form;
    }
  }
}

</script>