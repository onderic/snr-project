<template>
<aside
  class="fixed top-0 left-0 z-[99] mt-20 pt-[--m-top] overflow-hidden transition-transform xl:duration-500 max-xl:w-full max-xl:-translate-x-full"

  >
    <div
    class="p-2 max-xl:bg-white shadow-sm 2xl:w-72 sm:w-64 w-[80%] h-[calc(100vh-64px)] relative z-30 max-lg:border-r dark:max-xl:!bg-slate-700 dark:border-slate-700"
    >
      <div class="pr-4">
        <div  class="font-medium text-sm text-black  dark:text-white ">
          <h1 class="mb-3 font-semibold ">Dashboard</h1>
          <ul>
            
        <li>
          <router-link to="/dashboard" exact-active-class="bg-blue-500 text-white dark:bg-blue-600 dark:text-white" class="flex items-center space-x-2 py-2 px-4 rounded-lg hover:bg-gray-400 dark:hover:bg-slate-600 text-sm dark:text-white">
            <v-icon name="fc-home" class="" />
            <span>Feed</span>
          </router-link>
        </li>
        
        <li>
          <router-link to="/add-pool/location" exact-active-class="bg-blue-500 text-white dark:bg-blue-600 dark:text-white" class="flex items-center space-x-2 py-2 mt-2 px-4 rounded-lg hover:bg-gray-400 dark:hover:bg-slate-600 text-sm dark:text-white">
            <v-icon name="io-create" />
            <span>Create</span>
          </router-link>
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
                class="flex items-center space-x-2 py-2 px-4 rounded-lg hover:bg-gray-400 dark:hover:bg-slate-600  text-sm dark:text-white"
              >
              <v-icon name="hi-solid-users"   class="darkt:text-white" /> 
                <span>Manage Owners</span>
              </a>
              </router-link>
            </li>
            <li>
                  <router-link to="/admin-manage-pool" exact-active-class="bg-blue-500 text-white dark:bg-blue-600 dark:text-white" class="flex items-center space-x-2 py-2 px-4 rounded-lg hover:bg-gray-400 dark:hover:bg-slate-600 text-sm dark:text-white">
                    <v-icon name="ci-color-pot"   class="darkt:text-white" /> 
                  <span>Manage Pool Space</span>
                </router-link>
                </li>
             
            <li>
              <router-link to="/admin-manage-events" exact-active-class="bg-blue-500 text-white dark:bg-blue-600 dark:text-white" class="flex items-center space-x-2 py-2 px-4 rounded-lg hover:bg-gray-400 dark:hover:bg-slate-600 text-sm dark:text-white">
            <v-icon name="fc-calendar" class="darkt:text-white" />
            <span>Manage Tournaments</span>
          </router-link>
        </li>
             
           
              </ul>
          </div>
        <div  v-if="isAuthenticated" class="font-medium text-sm text-black border-t pt-3 mt-10 dark:text-white dark:border-slate-800">
            <h1 class="mb-3 font-semibold ">Owner</h1>
              <ul>
                <li>
                  <router-link to="/manage-pool" exact-active-class="bg-blue-500 text-white dark:bg-blue-600 dark:text-white" class="flex items-center space-x-2 py-2 px-4 rounded-lg hover:bg-gray-400 dark:hover:bg-slate-600 text-sm dark:text-white">
                    <v-icon name="ci-color-pot"   class="darkt:text-white" /> 
                  <span>Manage Pool Space</span>
                </router-link>
                </li>
             
            <li>
              <router-link to="/manage-events" exact-active-class="bg-blue-500 text-white dark:bg-blue-600 dark:text-white" class="flex items-center space-x-2 py-2 px-4 rounded-lg hover:bg-gray-400 dark:hover:bg-slate-600 text-sm dark:text-white">
            <v-icon name="fc-calendar" class="darkt:text-white" />
            <span>Manage Tournaments</span>
          </router-link>
        </li>
           
              </ul>
          </div>
        <div  class="font-medium text-sm text-black border-t pt-3 mt-10 dark:text-white dark:border-slate-800">
          <h1 class="mb-3 font-semibold ">User, {{ userStore.user.username }}</h1>
              <ul>
                <li>
                  <a v-if="isAuthenticated" @click.prevent="handleLogout" class="flex items-center space-x-2 py-2 px-4 rounded-lg hover:bg-gray-400 dark:hover:bg-slate-600 font-bold text-sm dark:text-white">
                    <v-icon name="hi-login"   class="darkt:text-white" /> 
                  <span>Logout</span>
                </a>

                 <router-link v-else to="/auth/login" class="flex items-center space-x-2 py-2 px-4 rounded-lg hover:bg-gray-400 dark:hover:bg-slate-600 font-bold text-sm dark:text-white">
                  <v-icon name="md-login"   class="darkt:text-white" /> 
                  <span>Login</span>
                </router-link>
                    
      
            </li>
           
              <li>
              <router-link  to="/dashboard">
              <a
                href="#"
                class="flex items-center space-x-2 py-2 px-4 rounded-lg hover:bg-gray-400 dark:hover:bg-slate-600 font-bold text-sm dark:text-white"
              >
              <v-icon name="fc-settings"   class="darkt:text-white" /> 
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