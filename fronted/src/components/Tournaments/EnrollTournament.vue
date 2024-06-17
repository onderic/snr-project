<template>
<div>
    <div class="block space-y-4 md:flex md:space-y-0 md:space-x-4 rtl:space-x-reverse">
    <!-- Modal toggle -->
    <button data-modal-target="small-modal" data-modal-toggle="small-modal" class="btn">
        <ion-icon name="star-outline" class="text-xl md hydrated" role="img" aria-label="star outline"></ion-icon> 
        <span class="text-sm"> Join Now </span>
    </button>
 
</div>

<!-- Small Modal -->
<div id="small-modal" tabindex="-1" class="fixed top-0 left-0 right-0 z-50 hidden w-full p-4 overflow-x-hidden overflow-y-auto md:inset-0 h-[calc(100%-1rem)] max-h-full">
    <div class="relative w-full max-w-md max-h-full">
        <!-- Modal content -->
        <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
            <!-- Modal header -->
            <div class="flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600">
                <h3 class="text-xl font-medium text-gray-900 dark:text-white">
                    Join Tournament
                </h3>
                <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white" data-modal-hide="small-modal">
                    <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>
                    </svg>
                    <span class="sr-only">Close modal</span>
                </button>
            </div>
            <!-- Modal body -->
            <div class="p-4 md:p-5 space-y-4">
                <p class="text-lg text-gray-600 dark:text-white">Are you sure you want to join this tournament?</p>
            </div>
            <!-- Modal footer -->
            <div class="flex items-center p-4 md:p-5 border-t border-gray-200 rounded-b dark:border-gray-600">
                <button @click="enroll" type="submit" class="btn" :disabled="loading">
                <v-icon v-if="loading" name="gi-spinning-blades" animation="spin" scale="1" />
                <span>Join</span>
                </button>
                <button data-modal-hide="small-modal" type="button" class="py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700">Decline</button>
            </div>
        </div>
    </div>
</div>

</div>
</template>

<script setup>
import { useToast } from 'vue-toastify';
import { useUserStore } from '@/stores/user';
import { useLoading } from '@/composables/loading';
import axios from 'axios';
import { defineProps } from 'vue';
import { initFlowbite } from 'flowbite';
import { onMounted } from 'vue';
import router from '@/router'; 

const toast = useToast();
const userStore = useUserStore();
const loading = useLoading();

const props = defineProps({
  eventId: Number
});

async function enroll() {
  try {
    loading.value = true;

    const data = {
      user: userStore.user.id,
      tournament: props.eventId
    };

    const response = await axios.post('enroll_event/', data, {
      headers: {
        Authorization: `Bearer ${userStore.user.access}`
      },
    });

    toast.success('Enrollment successful');
    
    // Verify if the router push is happening
    router.push('/enrollment-list').then(() => {
        window.location.reload();
    }).catch(err => {
      console.error('Navigation Error:', err);
    });

  } catch (error) {
    console.error('Error enrolling user:', error);
    toast.error(error.response?.data?.error || 'Something went wrong, try later');
  } finally {
    loading.value = false;
  }
}

onMounted(() => {
  initFlowbite();
});
</script>


<style>

</style>