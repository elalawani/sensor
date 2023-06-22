import { createRouter, createWebHistory } from 'vue-router'
import { useUserStore } from '@/stores/user'
import LoginView from '../views/LoginView.vue';
import SignupView from '../views/SignupView.vue';
import DashboardView from '../views/DashboardView.vue';
import PatientsListView from "@/views/PatientsListView.vue";
import PatientsView from "@/views/PatientView.vue";
import NewPatientFormView from "@/views/NewPAtientFormView.vue";
import patientInfo from "@/components/patientInfo.vue";
import medications from "@/components/medications.vue";
import sensorData from "@/components/sensorData.vue";
import conversations from "@/components/conversations.vue";
import documentations from "@/components/documentations.vue";
import ProfileView from "@/views/ProfileView.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'dashboard',
            component: DashboardView,
            meta: { requiresAuth: true }
        },
        {
            path: '/login',
            name: 'login',
            component: LoginView,
        },
        {
            path: '/signup',
            name: 'signup',
            component: SignupView
        },
        {
            path: '/all_patients',
            name: 'all_patients',
            component: PatientsListView,
            meta: { requiresAuth: true }
        },
        {
            path: '/add_patient',
            name: 'add_patient',
            component: NewPatientFormView,
            meta: { requiresAuth: true }
        },
        {
            path: '/profile',
            name: 'profile',
            component: ProfileView,
            meta: { requiresAuth: true }
        },
        {
            path: '/patients/:id',
            name: 'patients',
            component: PatientsView,
            meta: { requiresAuth: true },
            children: [
                {
                    path: '/patients/:id/info',
                    name: 'patientInfo',
                    component: patientInfo
                },
                {
                    path: '/patients/:id/medications',
                    name: 'medications',
                    component: medications
                },
                 {
                    path: '/patients/:id/sensorData',
                    name: 'sensorData',
                    component: sensorData
                },
                {
                    path: '/patients/:id/conversations',
                    name: 'conversations',
                    component: conversations
                },
                {
                    path: '/patients/:id/documentations',
                    name: 'documentations',
                    component: documentations
                },
            ]
        },
    ]
})

router.beforeEach((to, from, next) => {
  const userStore = useUserStore()
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth)

  if (requiresAuth && !userStore.user.isAuthenticated) {
    next('/login')
  } else {
    next()
  }
})

export default router
