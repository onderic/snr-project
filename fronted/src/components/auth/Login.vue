<template>
  <div class="flex justify-center items-center h-screen bg-gray-50 dark:bg-gray-900">

<section class="">
    <div class="py-8 px-4 mx-auto max-w-screen-xl lg:py-16 grid lg:grid-cols-2 gap-8 lg:gap-16">
        <div class="flex flex-col justify-center">
            <h1 class="mb-4 text-4xl font-extrabold tracking-tight leading-none text-gray-900 md:text-5xl lg:text-6xl dark:text-white">Join to elavete your pool game🎱</h1>
            <p class="mb-6 text-lg font-normal text-gray-500 lg:text-xl dark:text-gray-400">  Connect with other players and pool owners to enhance your gaming experience! 
  Discover new strategies, find teammates, and create lasting gaming friendships.
  Join a vibrant community of players passionate about your favorite games.</p>
            <a href="#" class="text-blue-600 dark:text-blue-500 hover:underline font-medium text-lg inline-flex items-center">Experience more here
                <v-icon name="ri-share-forward-fill" scale="3"  /> 
            </a>
        </div>
        <div>
            <div class="w-full lg:max-w-xl p-6 space-y-8 sm:p-8 bg-white rounded-lg shadow-xl dark:bg-gray-800">
                <h2 class="text-2xl font-bold text-gray-900 dark:text-white">
                    Sign in to CueConnect
                </h2>
                <form class="mt-8 space-y-6"  @submit.prevent="login">
                    <div>
                        <label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your email</label>
                        <input  v-model="formData.email" type="email" name="email" id="email" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="name@company.com" required />
                    </div>
                    <div>
                        <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your password</label>
                        <input  v-model="formData.password" type="password" name="password" id="password" placeholder="••••••••" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required />
                    </div>
                    <div class="flex items-start">
                        <div class="flex items-center h-5">
                            <input id="remember" aria-describedby="remember" name="remember" type="checkbox" class="w-4 h-4 border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-blue-300 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:bg-gray-700 dark:border-gray-600"  />
                        </div>
                        <div class="ms-3 text-sm">
                        <label  class="font-medium text-gray-500 dark:text-gray-400">Remember this device</label>
                        </div>
                        <a href="#" class="ms-auto text-sm font-medium text-blue-600 hover:underline dark:text-blue-500">Lost Password?</a>
                    </div>
                    <button type="submit" class="btn">
                         
                            <v-icon v-if="loading" name="gi-spinning-blades" animation="spin"  scale="1"/> 
                
                         Login to your account
                        </button>
                    <div class="text-sm font-medium text-gray-900 dark:text-white">
                        Not registered yet? <router-link to="/auth/register"> <a class="text-blue-600 hover:underline dark:text-blue-500">Create account</a></router-link>
                    </div>
                </form>
            </div>
        </div>
    </div>
</section>
</div>
</template>

<script setup>
import { reactive, ref } from 'vue';
import axios from 'axios';
import { useToast } from 'vue-toastify';
import { useRouter, useRoute } from 'vue-router';
import { useUserStore } from '@/stores/user';

const props = defineProps({
  formData: {
    type: Object,
    required: true,
    default: () => ({
      email: '',
      password: ''
    })
  }
});

const formData = reactive(props.formData);
const toast = useToast();
const router = useRouter();
const route = useRoute();
const userStore = useUserStore();

const loading = ref(false);

const login = async () => {
  try {
    loading.value = true
    const response = await axios.post('login/', {
      email: formData.email,
      password: formData.password
    });

    userStore.setToken(response.data);
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + response.data.access;

    const userinfo = await axios.get('user');
    userStore.setUserInfo(userinfo.data);

    const intendedPage = route.query.to || '/';
    router.push(intendedPage);
    toast.success('Login successful!');
 
  } catch (error) {
    console.error('Login error:', error);
    toast.error('Login failed. Please check your credentials.');
  }finally{
    loading.value = false
  }
};
</script>

<style>

</style>