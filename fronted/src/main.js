import './assets/base.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import PrimeVue from 'primevue/config';
import Lara from './presets/lara';
import 'primeicons/primeicons.css'
import ConfirmationService from 'primevue/confirmationservice';
import ToastService from 'primevue/toastservice';
import Toast from 'primevue/toast';



const app = createApp(App)

app.use(PrimeVue, {
    unstyled: true,
    pt: Lara
});
app.use(ConfirmationService);
app.use(ToastService);
app.component('Toast', Toast);

app.use(createPinia())
app.use(router)

app.mount('#app')
