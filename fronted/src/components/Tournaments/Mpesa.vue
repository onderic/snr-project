
<template>
    <div v-if="isOpen" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
      <div class="relative p-4 w-full max-w-md max-h-full">
        <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
          <div class="flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600">
            <h3 class="text-xl font-semibold text-gray-900 dark:text-white">Lipa Na Mpesa</h3>
            <button @click="closeModal" class="end-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white">
              <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>
              </svg>
              <span class="sr-only">Close modal</span>
            </button>
          </div>
          <div class="p-4 md:p-5">
            <form @submit.prevent="submitPhoneNumber" class="space-y-4">
              <div>
                <label for="tel" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your Phone Number</label>
                <input v-model="phoneNumber" type="tel" name="tel" id="tel" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white" placeholder="123-456-7890" required />
              </div>
              <button @click="enroll" type="submit" class="btn" :disabled="loading">
                <v-icon v-if="loading" name="gi-spinning-blades" animation="spin" scale="1" />
                <span>Lipa Na Mpesa</span>
            </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </template>
  
<script setup>
import { ref } from 'vue';
import { useLoading } from '@/composables/loading';
import { useUserStore } from '@/stores/user';
import axios from 'axios';
import { useToast } from 'vue-toastify';

const props = defineProps({
  isOpen: {
    type: Boolean,
    required: true
  },
  amount: {
    type: Number,
    required: true
  },
  eventId: {
    type: Number,
    required: true
  }
});

const emit = defineEmits(['close']);
const phoneNumber = ref('');

const toast = useToast();
const userStore = useUserStore();
const loading = useLoading();

const closeModal = () => {
  emit('close');
};

const submitPhoneNumber = async () => {
  loading.value = true;
  try {
    const data = {
      amount: props.amount,
      phone_number: phoneNumber.value
    };
    const response = await axios.post(`pay-enrollment-fee/${props.eventId}/`, data, {
      headers: {
        Authorization: `Bearer ${userStore.user.access}`,
      },
    });
    if (response.status === 200) {
      toast.success('An stk push has been sent to your phone');
      closeModal();
    } else {
      toast.error(response.data?.error || 'Something went wrong, try later');
    }
  } catch (error) {
    toast.error('Something went wrong, try later');
  } finally {
    loading.value = false;
  }
};
  
</script>
  
