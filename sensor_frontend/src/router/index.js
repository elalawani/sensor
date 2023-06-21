import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/LoginView.vue';
import SignupView from '../views/SignupView.vue';
import DashboardView from '../views/DashboardView.vue';
import PatientsListView from "@/views/PatientsListView.vue";
import PatientsView from "@/views/PatientView.vue";
import NewPatientFormView from "@/views/NewPAtientFormView.vue";
import patientInfo from "@/components/patientInfo.vue";

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
        {
            path: '/patients/:id',
            name: 'patients',
            component: PatientsView,
            children: [
                {
                    path: '',
                    name: 'patientInfo',
                    component: patientInfo
                },
            ]
        },
    ]
})

export default router
