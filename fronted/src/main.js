import './assets/base.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import plugin from 'vue-toastify';
import 'vue-toastify/index.css';
import axios  from 'axios'
import { useUserStore } from './stores/user';


import { OhVueIcon, addIcons } from "oh-vue-icons";
import { CoHome,
    IoLocateOutline,
    IoCreateOutline,
    PxNext,CoLibraryAdd,
    IoCheckmarkDoneOutline,
    FcInfo,
    FcCalendar,
    HiSolidUsers,
    CiColorPot,
    HiLogin,
    FcSettings,
    MdDarkmode,
    FaSun,
    PxNotification,
    CoUser,
    RiShareForwardFill,
    GiSpinningBlades,
    MdLogin,
    PxCheckboxOn
 } from "oh-vue-icons/icons";

addIcons(CoHome,
    IoLocateOutline
    ,IoCreateOutline,
    PxNext,
    CoLibraryAdd,
    IoCheckmarkDoneOutline,
    FcInfo,
    FcCalendar,
    HiSolidUsers,
    CiColorPot,
    HiLogin,
    FcSettings,
    MdDarkmode,
    FaSun,
    PxNotification,
    CoUser,
    RiShareForwardFill,
    GiSpinningBlades,
    MdLogin,
    PxCheckboxOn
);

axios.defaults.baseURL = 'http://127.0.0.1:8000/api/v1/'

const app = createApp(App)

app.component("v-icon", OhVueIcon);

app.use(plugin, {});

app.use(createPinia())
app.use(router,axios)

app.mount('#app')

const userStore = useUserStore();
userStore.initStore();
