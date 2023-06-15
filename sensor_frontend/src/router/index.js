import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/LoginView.vue';
import SignupView from '../views/SignupView.vue';
import DashboardView from '../views/DashboardView.vue';
import PatientsListView from "@/views/PatientsListView.vue";
import NewPatientFormView from "@/views/NewPAtientFormView.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'dashboard',
            component: DashboardView
        },
        {
            path: '/login',
            name: 'login',
            component: LoginView
        },
        {
            path: '/signup',
            name: 'signup',
            component: SignupView
        },
        {
            path: '/all_patients',
            name: 'all_patients',
            component: PatientsListView
        },
        {
            path: '/add_patient',
            name: 'add_patient',
            component: NewPatientFormView
        },

    ]
})

export default router
