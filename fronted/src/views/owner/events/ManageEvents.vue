<template>
   <div class="2xl:max-w-[1220px] max-w-[1065px] mx-auto lg:mt-20 mt-4">
    <div class="sm:px-6 w-full">
        <div class="mb-5">
          <div class="flex items-center justify-between">
            <p class="focus:outline-none text-base dark:text-white sm:text-lg md:text-xl lg:text-2xl font-bold leading-normal text-gray-800">My Events</p>
          </div>
        </div>
        <div class="dark:bg-slate-800 bg-white py-4 md:py-7 px-4 md:px-8 xl:px-10">
          <div class="sm:flex items-center justify-between">
            <div class="flex items-center dark:text-white">
              <a  class="rounded-full focus:outline-none focus:ring-2 focus:bg-indigo-50 focus:ring-indigo-800 ml-4 sm:ml-8" href="javascript:void(0)">
                <div class="py-2 px-8 bg-indigo-100 text-indigo-700 rounded-full">
                  <p>All</p>
                </div>
              </a>
              
            </div>
            <AddTournaments @event-added="get_owner_events" />
          </div>
          <div class="mt-7 overflow-x-auto">
            <table class="w-full whitespace-nowrap">
              <tbody v-if="loading">
                <tr v-for="n in 5" :key="n" class="focus:outline-none h-16  rounded animate-pulse">
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
                  <td class="pl-4">
                    <div class="w-24 h-5 bg-gray-300 rounded-sm"></div>
                  </td>
                </tr>
              </tbody>
              <tbody v-else>
                <tr v-for="event in events" :key="event.id" tabindex="0" class="focus:outline-none h-16  rounded">
                
                  <td class="">
                    <div class="flex items-center pl-5 dark:text-white">
                      <p class="text-base font-medium leading-none text-gray-700 dark:text-white mr-2">{{ event.title }}</p>
                      <v-icon name="co-eventbrite" />
                    </div>
                  </td>
                  <td class="pl-24">
                    <div class="flex items-center dark:text-white">
                      <v-icon name="hi-status-offline" />
                      <p class="text-sm leading-none text-gray-600 dark:text-white ml-2">{{ event.status }}</p>
                    </div>
                  </td>
                  <td class="pl-5">
                    <div class="flex items-center dark:text-white">
                      <v-icon name="co-user" />
                      <p class="text-sm leading-none text-gray-600 dark:text-white ml-2">23</p>
                    </div>
                  </td>
                  <td class="pl-5">
                    <div class="flex items-center dark:text-white">
                      <p class="text-sm leading-none text-gray-600 dark:text-white ml-2">04/07</p>
                    </div>
                  </td>
                  <td class="pl-5">
                    <button class="py-3 px-3 text-sm focus:outline-none leading-none text-green-700 bg-green-100 rounded">Starts On {{ event.start_time }}</button>
                  </td>
                    <td class="pl-4 flex items-center px-6 py-4">
                    <a href="#" class="font-medium text-blue-600 dark:text-blue-500 hover:underline">Edit</a>
                    <a @click="deleteEvent(event.id)" class="font-medium text-red-600 dark:text-red-500 hover:underline ms-3">Remove</a>
                  </td>
                 
                </tr>
                <tr class="h-3"></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import AddTournaments from '@/components/Tournaments/CreateTournament.vue';
  import axios from 'axios';
  import { ref, onMounted, computed } from 'vue';
  import { useLoading } from '@/composables/loading';
  import { useToast } from 'vue-toastify';
  import { useUserStore } from '@/stores/user';
  
  const loading = useLoading();
  const toast = useToast();
  const events = ref([]);
  const userStore = useUserStore();

  
  async function get_owner_events() {
    try {
      loading.value = true;
      const response = await axios.get(`owner_events/${userStore.user.id}`);
      events.value = response.data;
      console.log("events", response.data);
    } catch (error) {
      console.error('Error fetching pool spaces:', error.message);
    } finally {
      loading.value = false;
    }
  }

  async function deleteEvent(eventId) {
    try {
      await axios.delete(`/tournaments_delete/${eventId}/`);
      get_owner_events();
      toast.success('Event deleted successfully');
    } catch (error) {
      console.error('Error deleting event:', error.message);
      toast.error('Failed to delete event');
    }
  }
  
  onMounted(() => {
    get_owner_events();
  });

  </script>
  
  <style>
  /* Add any necessary custom styles here */
  </style>
  