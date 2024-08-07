<template>
  <div>
    <div v-if="isOpen" class="fixed inset-0 flex items-center justify-center z-50">
      <div class="absolute inset-0 bg-gray-800 bg-opacity-10"></div>
      <div class="relative p-4 w-full max-w-md max-h-full bg-white rounded-lg shadow dark:bg-gray-700 z-10">
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
                <input v-model="phoneNumber" type="tel" name="tel" id="tel" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white" placeholder="0798335657" required />
              </div>
              <button type="submit" class="btn flex items-center justify-center" :disabled="loading">
                <v-icon v-if="loading" name="gi-spinning-blades" animation="spin" scale="1" class="mr-2" />
                <span v-if="loading">Processing...</span>
                <span v-else>Lipa Na Mpesa</span>
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
    <Loading v-if="isLoading" message="We are waiting for you. Please do not close this window." />
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';
import axios from 'axios';
import usePolling from '@/composables/usePolling';
import { useToast } from 'vue-toastify';
import { useUserStore } from '@/stores/user';
import Loading from '@/components/Tournaments/LoadingAnimation.vue';

const props = defineProps({
  isOpen: Boolean,
  amount: Number,
  eventId: Number,
});

const emit = defineEmits(['polling-started', 'polling-stopped', 'close', 'payment-success']);

const phoneNumber = ref('');
const checkoutRequestId = ref('');
const transactionResult = ref(null);
const toast = useToast();
const userStore = useUserStore();
const loading = ref(false);
const isLoading = ref(false);

const closeModal = () => {
  emit('close'); 
};

const submitPhoneNumber = async () => {
  loading.value = true;
  try {
    const data = {
      amount: props.amount,
      phone_number: phoneNumber.value,
    };
    const response = await axios.post(`pay-enrollment-fee/${props.eventId}/`, data, {
      headers: {
        Authorization: `Bearer ${userStore.user.access}`,
      },
    });
    
    if (response.status === 200) {
      const responseDescription = response.data.ResponseDescription;
      toast.success(responseDescription);
      checkoutRequestId.value = response.data.CheckoutRequestID;
      closeModal(); 
    } else {
      toast.error(response.data?.error || 'Something went wrong, try later');
    }
  } catch (error) {
    if (error.response) {
      toast.error(error.response.data?.error || 'Something went wrong, try later');
    } else if (error.request) {
      toast.error('Network error. Please check your connection and try again.');
    } else {
      toast.error('An unexpected error occurred. Please try again later.');
    }
  } finally {
    loading.value = false;
  }
};

const checkTransactionStatus = async () => {
  if (!checkoutRequestId.value) return;

  try {
    const response = await axios.get(`check-transaction-status/${checkoutRequestId.value}/`, {
      headers: {
        Authorization: `Bearer ${userStore.user.access}`,
      },
    });
    const resultCode = response.data?.ResultCode;
    const resultDesc = response.data?.ResultDesc;

    transactionResult.value = { resultCode, resultDesc };

    if (resultCode === '0') {
      toast.success(resultDesc || 'Transaction completed successfully');
      emit('payment-success', props.eventId);
      checkoutRequestId.value = ''; 
      stopPolling();
    } else if (!resultCode && !resultDesc) {
      console.log('Transaction status not available yet, retrying...');
    } else {
      toast.error(`Transaction failed: ${resultDesc || 'Unknown error'}`);
      checkoutRequestId.value = ''; 
      stopPolling(); 
    }
  } catch (error) {
    console.error('Polling error:', error);
    stopPolling();
  }
};

const { start, stop } = usePolling(checkTransactionStatus, 1000, (loadingState) => {
  isLoading.value = loadingState;
});

const pollingTimeout = ref(null);

const startPollingWithTimeout = () => {
  emit('polling-started');
  start();

  // Set a timeout to stop polling after 5 seconds
  pollingTimeout.value = setTimeout(() => {
    console.log('Polling timeout reached. Assuming success.');
    toast.success('Transaction completed successfully');
    emit('payment-success', props.eventId);
    checkoutRequestId.value = '';
    stop();
  }, 10000);
};

const stopPolling = () => {
  emit('polling-stopped');
  stop();
  if (pollingTimeout.value) {
    clearTimeout(pollingTimeout.value);
    pollingTimeout.value = null;
  }
};

watch(checkoutRequestId, (newValue) => {
  if (newValue) {
    startPollingWithTimeout();
  } else {
    stopPolling();
  }
}, { immediate: true });

</script>
