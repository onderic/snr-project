import './assets/base.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import PrimeVue from 'primevue/config';
import Lara from './presets/lara';
import 'primeicons/primeicons.css'


const app = createApp(App)

app.use(PrimeVue, {
    unstyled: true,
    pt: Lara
});

app.use(createPinia())
app.use(router)

app.mount('#app')
