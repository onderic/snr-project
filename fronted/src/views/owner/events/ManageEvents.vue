<template>
    <div class="2xl:max-w-[1220px] max-w-[1065px] mx-auto mt-10">
 <!-- component -->
<div class="sm:px-6 w-full">
            <div class=" mb-5">
                <div class="flex items-center justify-between">
                    <p class="focus:outline-none text-base dark:text-white sm:text-lg md:text-xl lg:text-2xl font-bold leading-normal text-gray-800">My Events</p>
                   
                </div>
            </div>
            <div class="dark:bg-slate-800 bg-white py-4 md:py-7 px-4 md:px-8 xl:px-10">
                <div class="sm:flex items-center justify-between">
                    <div class="flex items-center dark:text-white">
                        <a @click="selectFilter('all')"  :class="{ 'text-indigo-700 bg-indigo-100': selectedFilter === 'all' }" class="rounded-full focus:outline-none focus:ring-2 focus:bg-indigo-50 focus:ring-indigo-800 ml-4 sm:ml-8" href="javascript:void(0)">
                            <div class="py-2 px-8 bg-indigo-100 text-indigo-700 rounded-full">
                                <p>All</p>
                            </div>
                        </a>
                        <a @click="selectFilter('upcoming')" :class="{ 'text-indigo-700 bg-indigo-100': selectedFilter === 'upcoming' }" class="rounded-full focus:outline-none focus:ring-2 focus:bg-indigo-50 focus:ring-indigo-800 ml-4 sm:ml-8" href="javascript:void(0)">
                            <div class="py-2 px-8 text-gray-600 dark:text-white hover:text-indigo-700 hover:bg-indigo-100 rounded-full ">
                                <p>Upcoming</p>
                            </div>
                        </a>
                        <a @click="selectFilter('past')" :class="{ 'text-indigo-700 bg-indigo-100': selectedFilter === 'past' }" class="rounded-full focus:outline-none focus:ring-2 focus:bg-indigo-50 focus:ring-indigo-800 ml-4 sm:ml-8" href="javascript:void(0)">
                            <div class="py-2 px-8 text-gray-600 dark:text-white hover:text-indigo-700 hover:bg-indigo-100 rounded-full ">
                                <p>Past</p>
                            </div>
                        </a>
                    </div>
                   <AddTournaments @event-added="get_owner_events"/>
                   
                </div>
                <div class="mt-7 overflow-x-auto">
                    <table class="w-full whitespace-nowrap">
                        <tbody  v-for="event in filteredEvents" :key="event.id" >
                            
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
                                        <p class="text-base font-medium leading-none text-gray-700 dark:text-white mr-2">{{event.title}}</p>
                                        <v-icon name="co-eventbrite" />
                                        
                                    </div>
                                </td>
                                <td class="pl-24">
                                    <div class="flex items-center dark:text-white">
                                        <v-icon name="hi-status-offline" />
                                      
                                        <p class="text-sm leading-none text-gray-600 dark:text-white ml-2">{{event.status}}</p>
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
                                    <button class="py-3 px-3 text-sm focus:outline-none leading-none text-green-700 bg-green-100 rounded">Starts On {{event.start_time}}</button>
                                </td>
                                <td class="pl-4">
                                    <button class="btn">View</button>
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
import AddTournaments from '@/components/Tournaments/CreateTournament.vue';

import axios from 'axios';
import { ref, onMounted, computed } from 'vue';
import { useLoading } from '@/composables/loading';
import { useToast } from 'vue-toastify';
import { useUserStore } from '@/stores/user';

const loading = useLoading()
const toast = useToast()
const events = ref([])
const userStore = useUserStore();

const selectedFilter = ref('all');

async function get_owner_events(){
    try{
        loading.value = true
        const response = await axios.get(`owner_events/${userStore.user.id}`)
        events.value = response.data;
        console.log("events", response.data)
    }catch (error){
        console.error('Error fetching pool spaces:', error.message);
    }finally{
        loading.value = false
    }
}

onMounted(() =>{
    get_owner_events()
})

const filteredEvents = computed(() => {
    if (selectedFilter.value === 'all') {
        return events.value;
    } else {
        return events.value.filter(event => event.status === selectedFilter.value);
    }
});

function selectFilter(filter) {
    selectedFilter.value = filter;
}

</script>

<style>

</style>