<template>
    <div  class="2xl:max-w-[1220px] max-w-[1065px] mx-auto mt-10">
 <!-- component -->
<div class="sm:px-6 w-full">
            <div class=" mb-5">
                <div class="flex items-center justify-between">
                    <p class="focus:outline-none text-base dark:text-white sm:text-lg md:text-xl lg:text-2xl font-bold leading-normal text-gray-800">My Events</p>
                   
                </div>
            </div>
            <div class="dark:bg-slate-800 bg-white py-4 md:py-7 px-4 md:px-8 xl:px-10">
                <div class="text-center">
              
                   <h1 class="text-xl dark:text-white font-semibold capitalize ">my registered tournaments</h1>
                </div>
                <div class="mt-7 overflow-x-auto">
                    <table class="w-full whitespace-nowrap">
                        <tbody  v-for="event in events" :key="event.id" >
                            
                            <tr tabindex="0" class="focus:outline-none h-16 border border-gray-100 rounded">
                                <td>
                                    <div class="ml-5">
                                        <div class="bg-gray-200 rounded-sm w-5 h-5 flex flex-shrink-0 justify-center items-center relative">
                                            <input placeholder="checkbox" type="checkbox" class="focus:opacity-100 checkbox opacity-0 absolute cursor-pointer w-full h-full" />
                                            <div class="check-icon hidden bg-indigo-700 text-white rounded-sm">
                                               
                                            </div>
                                        </div>
                                    </div>
                                </td>
                                <td class="">
                                    <div class="flex items-center pl-5 dark:text-white">
                                        <p class="text-base font-medium leading-none text-gray-700 dark:text-white mr-2">{{event.tournament.title}}</p>
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
                                    <button class="py-3 px-3 text-sm focus:outline-none leading-none text-green-700 bg-green-100 rounded">Starts On {{event.tournament.start_time}}</button>
                                </td>
                                <td class="pl-5">
                                    <div class="flex items-center dark:text-white">
                                        
                                        <p class="text-sm leading-none text-gray-600 dark:text-white ml-2">Ksh {{event.tournament.enrollment_fee}}</p>
                                    </div>
                                </td>
                                <td class="pl-5">
                                    <div class="flex items-center dark:text-white">
                                        <!-- Conditionally render the button based on the `paid` status -->
                                        <!-- v-if="!event.paid" -->
                                        <button  @click="openModal(event.tournament.enrollment_fee, event.id)" class="btn">Pay</button>
                                        <Mpesa :isOpen="isModalOpen" :amount="selectedAmount" :eventId="selectedEventId" @close="closeModal" />
                                    </div>
                                </td>

                               
                                <td class="pl-4">
                                    <button :class="{ 
                                        'px-4 py-2 rounded-lg font-semibold focus:outline-none bg-green-500 text-white': event.paid, 
                                        'px-4 py-2 rounded-lg font-semibold focus:outline-none bg-gray-300 text-gray-700': !event.paid 
                                    }">
                                        {{ event.paid ? 'Complete' : 'Incomplete' }}
                                    </button>
                                </td>

                                                            <td>
                                    <div class="relative px-5 pt-2 dark:text-white">
                                        <button class="focus:ring-2 rounded-md focus:outline-none" role="button" aria-label="option">
                                           ...
                                        </button>
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
</template>

<script setup>


import axios from 'axios';
import { ref, onMounted, computed } from 'vue';
import { useLoading } from '@/composables/loading';
import { useUserStore } from '@/stores/user';
import Mpesa from '@/components/Tournaments/Mpesa.vue';

const loading = useLoading()
const events = ref([])
const userStore = useUserStore();

const isModalOpen = ref(false);
const selectedAmount = ref(0);
const selectedEventId = ref(null);

const openModal = (amount, eventId) => {
  isModalOpen.value = true;
  selectedAmount.value = amount;
  selectedEventId.value = eventId
};

const closeModal = () => {
  isModalOpen.value = false;
};


async function get_user_events(){
    try{
        loading.value = true
        const response = await axios.get('user-enrollments/', {
            headers: {
                Authorization: `Bearer ${userStore.user.access}`
            }
        })
        events.value = response.data;
        console.log("my events", response.data)
    }catch (error){
        console.error('Error fetching pool spaces:', error.message);
    }finally{
        loading.value = false
    }
}


onMounted(() =>{
    get_user_events()
})



</script>

<style>

</style>