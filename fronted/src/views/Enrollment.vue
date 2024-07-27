<template>
  <div>
    <!-- Show Loading Animation if showLoading is true -->
    <div v-if="showLoading">
      <LoadingAnimation message="We are waiting for the transaction to be confirmed. Please do not close this window." />
    </div>

    <!-- Main Content -->
    <div v-else>
      <div class="2xl:max-w-[1220px] max-w-[1065px] mx-auto mt-10">
        <div class="sm:px-6 w-full">
          <div class="mb-5">
            <div class="flex items-center justify-between">
              <p class="focus:outline-none text-base dark:text-white sm:text-lg md:text-xl lg:text-2xl font-bold leading-normal text-gray-800">My Events</p>
            </div>
          </div>
          <div class="dark:bg-slate-800 bg-white py-4 md:py-7 px-4 md:px-8 xl:px-10 rounded-md">
            <div class="text-center">
              <h1 class="text-xl dark:text-white font-semibold capitalize">my Enrolled Tournaments</h1>
            </div>
            <div class="mt-7 overflow-x-auto">
              <table class="w-full">
                <tbody v-if="loading">
                  <tr v-for="n in 5" :key="n" class="focus:outline-none h-16 rounded animate-pulse">
                    <td class="pl-5">
                      <div class="w-32 h-5 bg-gray-300 rounded-sm"></div>
                    </td>
                    <td class="pl-5">
                      <div class="w-32 h-5 bg-gray-300 rounded-sm"></div>
                    </td>
                    <td class="pl-24">
                      <div class="w-24 h-5 bg-gray-300 rounded-sm"></div>
                    </td>
                    <td class="pl-5">
                      <div class="w-10 h-5 bg-gray-300 rounded-sm"></div>
                    </td>
                    <td class="pl-5">
                      <div class="w-12 h-5 bg-gray-300 rounded-sm"></div>
                    </td>
                    <td class="pl-5">
                      <div class="w-32 h-5 bg-gray-300 rounded-sm"></div>
                    </td>
                    <td class="pl-4">
                      <div class="w-32 h-5 bg-gray-300 rounded-sm"></div>
                    </td>
                  </tr>
                </tbody>
                <tbody v-else>
                  <tr v-for="event in events" :key="event.id" tabindex="0" class="focus:outline-none h-16 rounded">
                    <td></td>
                    <td>
                      <div class="flex items-center pl-5 dark:text-white">
                        <p class="text-base font-medium leading-none text-gray-700 dark:text-white mr-2">{{ event.tournament.title }}</p>
                        <v-icon name="co-eventbrite" />
                      </div>
                    </td>
                    <td class="pl-24">
                      <div class="flex items-center dark:text-white">
                        <v-icon :name="event.paid ? 'hi-check-circle' : 'hi-status-offline'" />
                        <p class="text-sm leading-none text-gray-600 dark:text-white ml-2">
                          {{ event.paid ? 'Paid' : 'Unpaid' }}
                        </p>
                      </div>
                    </td>
                    <td class="pl-5">
                      <div class="flex items-center dark:text-white">
                        <v-icon name="co-user" />
                        <p class="text-sm leading-none text-gray-600 dark:text-white ml-2"> {{ event.tournament.attendees_count }}</p>
                      </div>
                    </td>
                    <td class="pl-5">
                      <button class="py-3 px-3 text-sm focus:outline-none leading-none text-green-500 rounded">
                        <span class="dark:text-white text-gray-700">Starts On</span> {{ event.tournament.start_time }}
                      </button>
                    </td>
                    <td class="pl-5">
                      <div class="flex items-center dark:text-white">
                        <p class="text-sm leading-none text-gray-600 dark:text-white ml-2">Ksh {{ event.tournament.enrollment_fee }}</p>
                      </div>
                    </td>
                    <td class="pl-4">
                      <a :class="{ 
                          'px-4 py-2 rounded-lg font-semibold focus:outline-none text-green-500': event.paid, 
                          'px-4 py-2 rounded-lg font-semibold focus:outline-none text-gray-300': !event.paid 
                      }">
                        {{ event.paid ? 'Complete' : 'Incomplete' }}
                      </a>
                    </td>
                    <td class="pl-5">
                      <div class="flex items-center dark:text-white">
                        <!-- Conditionally hide the Pay button if event.paid is true -->
                        <button v-if="!event.paid" @click="openModal(event.tournament.enrollment_fee, event.id)" class="btn">Pay</button>
                        <Mpesa
                          :isOpen="isModalOpen"
                          :amount="selectedAmount"
                          :eventId="selectedEventId"
                          @payment-success="updateEventStatus"
                          @close="closeModal"
                        />
                      </div>
                    </td>
                    <td>
                      <div class="relative px-5 pt-2 dark:text-white">
                        <div class="dropdown-content bg-white shadow w-24 absolute z-30 right-0 mr-6 hidden">
                          <div tabindex="0" class="focus:outline-none focus:text-indigo-600 text-xs w-full hover:bg-indigo-700 py-4 px-4 cursor-pointer hover:text-white">
                            <p>Edit</p>
                          </div>
                          <div tabindex="0" class="focus:outline-none focus:text-indigo-600 text-xs w-full hover:bg-indigo-700 py-4 px-4 cursor-pointer hover:text-white">
                            <p>Delete</p>
                          </div>
                        </div>
                      </div>
                    </td>
                  </tr>
                  <tr class="h-3"></tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useUserStore } from '@/stores/user';
import Mpesa from '@/components/Tournaments/Mpesa.vue';
import LoadingAnimation from '@/components/Tournaments/LoadingAnimation.vue';

const loading = ref(false);
const events = ref([]);
const userStore = useUserStore();

const isModalOpen = ref(false);
const selectedAmount = ref(0);
const selectedEventId = ref(null);
const showLoading = ref(false);

const openModal = (amount, eventId) => {
  isModalOpen.value = true;
  selectedAmount.value = amount;
  selectedEventId.value = eventId;
};

const closeModal = () => {
  isModalOpen.value = false;
};

const updateEventStatus = (eventId) => {
  const event = events.value.find(e => e.id === eventId);
  if (event) {
    event.paid = true;
  }
};

async function get_user_events() {
  try {
    loading.value = true;
    const response = await axios.get('user-enrollments/', {
      headers: {
        Authorization: `Bearer ${userStore.user.access}`
      }
    });
    events.value = response.data;
    console.log("my events", response.data);
  } catch (error) {
    console.error('Error fetching user events:', error.message);
  } finally {
    loading.value = false;
  }
}

onMounted(() => {
  get_user_events();
});
</script>

<style scoped>
/* Add your scoped styles here */
</style>
