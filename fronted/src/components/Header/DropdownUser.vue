<template>
<div>
      <!-- profile -->
      <button
    id="dropdownInformationButton"
    data-dropdown-toggle="dropdownInformation"
    type="button"
    class="sm:p-2 p-1 rounded-full relative sm:bg-gray-100 dark:bg-slate-900 dark:text-white"
    >
    <v-icon name="co-user" scale="1.5" />
    
    </button>
    <!-- Dropdown menu -->
    <div id="dropdownInformation" class="z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow w-44 dark:bg-gray-700 dark:divide-gray-600">
        <div class="px-4 py-3 text-sm text-gray-900 dark:text-white">
        <div>{{ userStore.user.username }}</div>
        <div class="font-medium truncate">name@flowbite.com</div>
        </div>
        <ul class="py-2 text-sm text-gray-700 dark:text-gray-200" aria-labelledby="dropdownInformationButton">
        <li>
            <a href="/" class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Feed</a>
        </li>
        <li>
            <a href="#" class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Settings</a>
        </li>
       
        </ul>
        <div  v-if="isAuthenticated"  class="py-2">
        <a @click="handleLogout" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white">Sign out</a>
        </div>
    </div>
</div>
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
