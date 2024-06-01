<template>
<aside
  class="fixed top-0 left-0 z-[99] mt-20 pt-[--m-top] overflow-hidden transition-transform xl:duration-500 max-xl:w-full max-xl:-translate-x-full"

  >
    <div
    class="p-2 max-xl:bg-white shadow-sm 2xl:w-72 sm:w-64 w-[80%] h-[calc(100vh-64px)] relative z-30 max-lg:border-r dark:max-xl:!bg-slate-700 dark:border-slate-700"
    >
      <div class="pr-4">
        <div >
          
          <ul>
            <li class="active">
              <router-link  to="/dashboard">
              <a
                href="#"
                class="flex items-center space-x-2 py-2 px-4 rounded-lg bg-blue-500 text-white dark:bg-blue-600 dark:text-white"
              >
              <v-icon name="co-home" scale="1.5" />
                <span>Feed</span>
              </a>
              </router-link>
            </li>
            <li>
              <a
                href="messages.html"
                class="flex items-center space-x-2 py-2 px-4 rounded-lg hover:bg-gray-100 dark:hover:bg-slate-600 font-bold text-sm dark:text-white"
              >
              
                <span>Messages</span>
              </a>
            </li>
         
          
            <li>
              <a
                href="pages.html"
                class="flex items-center space-x-2 py-2 px-4 rounded-lg hover:bg-gray-100 dark:hover:bg-slate-600 font-bold text-sm dark:text-white"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="w-6 h-6"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M3 6l5 5L3 16M21 6l-5 5 5 5"
                  ></path>
                </svg>
                <span>Pages</span>
              </a>
            </li>
            
          </ul>
          
        </div>
        <div  class="font-medium text-sm text-black border-t pt-3 mt-10 dark:text-white dark:border-slate-800">
            <h1 class="mb-3 font-semibold ">Administrator</h1>
              <ul>
                <li>
              <router-link  to="/dashboard">
              <a
                href="#"
                class="flex items-center space-x-2 py-2 px-4 rounded-lg hover:bg-gray-100 dark:hover:bg-slate-600  text-sm dark:text-white"
              >
              <v-icon name="hi-solid-users"  scale="1.5" class="darkt:text-white" /> 
                <span>Manage Owners</span>
              </a>
              </router-link>
            </li>
           
              <!-- <li>
              <router-link  to="/dashboard">
              <a
                href="#"
                class="flex items-center space-x-2 py-2 px-4 rounded-lg hover:bg-gray-100 dark:hover:bg-slate-600  text-sm dark:text-white"
              >
              <v-icon name="fc-calendar"  scale="1.5" class="darkt:text-white" /> 
                <span>Manage Events</span>
              </a>
              </router-link>
            </li> -->
           
              </ul>
          </div>
        <div  class="font-medium text-sm text-black border-t pt-3 mt-10 dark:text-white dark:border-slate-800">
            <h1 class="mb-3 font-semibold ">Owner</h1>
              <ul>
                <li>
              <router-link  to="/dashboard">
              <a
                href="#"
                class="flex items-center space-x-2 py-2 px-4 rounded-lg hover:bg-gray-100 dark:hover:bg-slate-600  text-sm dark:text-white"
              >
              <v-icon name="ci-color-pot"  scale="1.5" class="darkt:text-white" /> 
                <span>Manage Pool Space</span>
              </a>
              </router-link>
            </li>
           
              <li>
              <router-link  to="/dashboard">
              <a
                href="#"
                class="flex items-center space-x-2 py-2 px-4 rounded-lg hover:bg-gray-100 dark:hover:bg-slate-600  text-sm dark:text-white"
              >
              <v-icon name="fc-calendar"  scale="1.5" class="darkt:text-white" /> 
                <span>Manage Events</span>
              </a>
              </router-link>
            </li>
           
              </ul>
          </div>
        <div  class="font-medium text-sm text-black border-t pt-3 mt-10 dark:text-white dark:border-slate-800">
          <h1 class="mb-3 font-semibold ">User, {{ userStore.user.username }}</h1>
              <ul>
                <li>
                  <a v-if="isAuthenticated" @click.prevent="handleLogout" class="flex items-center space-x-2 py-2 px-4 rounded-lg hover:bg-gray-100 dark:hover:bg-slate-600 font-bold text-sm dark:text-white">
                    <v-icon name="hi-login"  scale="1.5" class="darkt:text-white" /> 
                  <span>Logout</span>
                </a>

                 <router-link v-else to="/auth/login" class="flex items-center space-x-2 py-2 px-4 rounded-lg hover:bg-gray-100 dark:hover:bg-slate-600 font-bold text-sm dark:text-white">
                  <v-icon name="md-login"  scale="1.5" class="darkt:text-white" /> 
                  <span>Login</span>
                </router-link>
                    
      
            </li>
           
              <li>
              <router-link  to="/dashboard">
              <a
                href="#"
                class="flex items-center space-x-2 py-2 px-4 rounded-lg hover:bg-gray-100 dark:hover:bg-slate-600 font-bold text-sm dark:text-white"
              >
              <v-icon name="fc-settings"  scale="1.5" class="darkt:text-white" /> 
                <span>Settings</span>
              </a>
              </router-link>
            </li>
           
              </ul>
          </div>
      </div>
    </div>
  </aside>
</template>


<script setup>
  import { computed } from 'vue';
  import { useRouter } from 'vue-router';
  import { useUserStore } from '@/stores/user';
  import { useToast } from 'vue-toastify';

  const router = useRouter();
  const userStore = useUserStore();
  const toast = useToast();

  const isAuthenticated = computed(() => userStore.user.isAuthenticated);

  const handleLogout = () => {
    userStore.removeToken();
    toast.success('Logged out successfully!');
    router.push('/dashboard');
  };
</script>