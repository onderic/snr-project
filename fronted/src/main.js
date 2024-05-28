import './assets/base.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import plugin from 'vue-toastify';
import 'vue-toastify/index.css';


import { OhVueIcon, addIcons } from "oh-vue-icons";
import { CoHome,IoLocateOutline,IoCreateOutline,PxNext,CoLibraryAdd,IoCheckmarkDoneOutline } from "oh-vue-icons/icons";

addIcons(CoHome,IoLocateOutline,IoCreateOutline,PxNext,CoLibraryAdd,IoCheckmarkDoneOutline);

const app = createApp(App)

app.component("v-icon", OhVueIcon);

app.use(plugin, {});

app.use(createPinia())
app.use(router)

app.mount('#app')
