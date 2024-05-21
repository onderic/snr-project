import './assets/base.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import PrimeVue from 'primevue/config';
import Aura from '@/presets/aura';
import 'primeicons/primeicons.css'; 

const app = createApp(App)

app.use(PrimeVue, {
    unstyled: true,
    pt: Aura
});

app.use(createPinia())
app.use(router)

app.mount('#app')
