import './assets/index.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'


import App from './App.vue'
import router from './router'
import axios from "axios";

import Multiselect from '@vueform/multiselect'
import "@vueform/multiselect/themes/default.css"



/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import {
    faInfo, faArrowRight, faUser, faHouseChimney, faUsers, faMessage, faStethoscope,
    faEnvelope, faFemale, faMale, faLungs, faTemperatureHalf, faHeartbeat, faDroplet, faPaperPlane,
} from '@fortawesome/free-solid-svg-icons'
import {
    faTwitter, faYoutube, faLinkedin, faGithub
} from "@fortawesome/free-brands-svg-icons";


/* add icons to the library */
library.add(
    faArrowRight, faInfo, faUser, faUsers, faLinkedin,
    faStethoscope, faEnvelope, faMessage, faHouseChimney, faFemale, faMale, faYoutube, faTwitter, faGithub, faLungs,
    faTemperatureHalf, faHeartbeat, faDroplet, faPaperPlane
)


// 8000 port witch django uses
axios.defaults.baseURL = 'http://127.0.0.1:8000'

const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)


const app = createApp(App)

app.use(pinia)
app.use(router, axios)
app.component('font-awesome-icon', FontAwesomeIcon)
app.component('multi-select', Multiselect)


app.mount('#app')
