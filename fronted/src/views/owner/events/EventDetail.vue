<template>
 <div v-if="event" class="2xl:max-w-[1220px] max-w-[1065px] mx-auto mt-20">

    <div >

        <!-- cover  -->
        <div class="bg-white dark:bg-slate-800 shadow lg:rounded-b-2xl lg:-mt-10 dark:bg-dark2">

            <!-- cover -->
            <div class="relative overflow-hidden w-full">
                <img src="@/assets/event.png" alt="" class="h-full w-full object-cover inset-0 ">

                <!-- overly -->
                <div class="w-full bottom-0 absolute left-0 bg-gradient-to-t from -black/60 pt-10 z-10"></div>

            </div>

            <div class="lg:px-10 md:p-5 p-3">

                <div class="flex flex-col justify-center md:-mt-20 -mt-12">

                    <div class="md:w-20 md:h-20 w-12 h-12 overflow-hidden bg-white shadow-md rounded-md z-10 mb-5">
                        <div class="w-full md:h-5 bg-rose-500 h-3"></div>
                        <div class="grid place-items-center text-black font-semibold md:text-3xl text-lg h-full md:pb-5 pb-3">
                            09
                        </div>
                    </div>
                
                    <div class="flex lg:items-center justify-between max-lg:flex-col max-lg:gap-2">

                        <div class="flex-1"> 
                            <p class="text-sm font-semibold text-rose-600 mb-1.5"> {{ event.start_time }} – {{ event.end_time }} </p>
                            <h3 class="md:text-2xl text-base font-bold text-black dark:text-white">{{ event.title }} </h3>
                            <p class="font-normal text-gray-500 mt-2 flex gap-2 dark:text-white/80">
                                <span> Free </span>
                                <span> • </span>
                                <span> Physical event </span>
                            </p>
                        </div>

                        <div>
                            <Counter/>
                        </div>

                    </div>

                </div>

            </div>

            <div class="flex items-center justify-between px-2 max-md:flex-col">

                <div class="flex items-center gap-2 text-sm py-2 pr-1 lg:order-1">
                    <button type="button" class="btn">  
                        <ion-icon name="star-outline" class="text-xl md hydrated" role="img" aria-label="star outline"></ion-icon> 
                        <span class="text-sm"> Join Now </span>
                    </button>
                    <button type="button" class="btn"> 
                        <ion-icon name="checkmark-circle-outline" class="text-xl md hydrated" role="img" aria-label="checkmark circle outline"></ion-icon> 
                        <span class="text-sm"> Going </span>
                    </button>
                

            
                    
                </div>

                <nav class="flex gap-0.5 rounded-xl overflow-hidden -mb-px text-gray-500 font-medium text-sm overflow-x-auto dark:text-white/80">
                    <a href="#" class="inline-block py-3 leading-8 px-3.5 border-b-2 border-blue-600 text-blue-600">About </a>
                    <a href="#" class="inline-block py-3 leading-8 px-3.5">Discussion</a> 
                </nav> 

            </div>


        </div>

        <div class="flex 2xl:gap-12 gap-10 mt-8 max-lg:flex-col" id="js-oversized">

            <div class="flex-1 space-y-4">

                <div class="bg-white dark:bg-slate-800 p-5 px-6 relative">
                    
                    <h3 class="font-semibold text-lg text-black dark:text-white"> About </h3>
                
                    <div class="space-y-4 leading-7 tracking-wide mt-4 text-black text-sm dark:text-white"> 
                        <p>{{ event.description }}</p>
                    </div> 

                </div>  

                <!-- comments -->  
                <div class="bg-white dark:bg-slate-800 p-5 px-6 relative">
                    <h3 class="font-semibold text-lg text-black dark:text-white"> Discussions </h3>

                    <div class=" text-sm font-normal space-y-4 relative mt-4"> 
                
                        <div class="flex items-start gap-3 relative">
                            <a class="dark:bg-white bg-gray-200 rounded-full p-1">   <v-icon name="co-user" scale="2" /> </a>
                            <div class="flex-1">
                                <a href="timeline.html" class="text-black font-medium inline-block dark:text-white"> Monroe Parker </a>
                                <p class="mt-0.5 dark:text-gray-300">Cant wait to snooker them </p>
                            </div>
                        </div>
                        <div class="flex items-start gap-3 relative">
                            <a class="dark:bg-white bg-gray-200 rounded-full p-1">   <v-icon name="co-user" scale="2" /> </a>
                            <div class="flex-1">
                                <a href="timeline.html" class="text-black font-medium inline-block dark:text-white"> John Michael </a>
                                <p class="mt-0.5 dark:text-gray-300">   You captured the moment.😎 </p>
                            </div>
                        </div>
                        <div class="flex items-start gap-3 relative">
                            <a class="dark:bg-white bg-gray-200 rounded-full p-1">   <v-icon name="co-user" scale="2" /> </a>
                            <div class="flex-1">
                                <a href="timeline.html" class="text-black font-medium inline-block dark:text-white"> James Lewis </a>
                                <p class="mt-0.5 dark:text-gray-300">Cant wait to snooker them </p>
                            </div>
                        </div>
                        <div class="flex items-start gap-3 relative">
                            <a class="dark:bg-white bg-gray-200 rounded-full p-1">   <v-icon name="co-user" scale="2" /> </a>
                            <div class="flex-1">
                                <a href="timeline.html" class="text-black font-medium inline-block dark:text-white"> Martin Gray </a>
                                <p class="mt-0.5 dark:text-gray-300">   You captured the moment.😎 </p>
                            </div>
                        </div>
                        <div>
                            <button type="button" class="btn">
                                More Comment
                            </button>
                        </div>

                    </div>

                    <!-- add comment -->
                    <div class="sm:px-4 sm:py-3 p-2.5 border-t border-gray-100 flex items-center gap-1 -m-6 mt-0 bg-gray-100 dark:bg-slate-700 dark:border-slate-700/40">
                        
                        <v-icon name="co-user" scale="2" />
                        
                        <div class="flex-1 relative overflow-hidden h-10">
                            <textarea placeholder="Add Comment...." class="w-full rounded-md py-3"></textarea>
                        </div>
                        
                        <button type="submit" class="btn"> Replay</button>
                    </div> 


                </div>

            </div>

            <div class="lg:w-[400px]"> 

                <div class="lg:space-y-4 lg:pb-8 max-lg:grid sm:grid-cols-2 max-lg:gap-6 uk-sticky">

                    <div class="bg-white p-5 dark:bg-slate-800 px-6 pr-0">

                        <h3 class="font-semibold text-lg text-black dark:text-white"> Status </h3> 

                        <div class="grid grid-cols-2 gap-2 text-sm mt-4">
                            <div class="flex gap-3">
                                <div class="p-2 inline-flex rounded-full bg-rose-50 self-center"> <ion-icon name="heart" class="text-2xl text-rose-600 md hydrated" role="img" aria-label="heart"></ion-icon></div>
                                <div>
                                    <h3 class="sm:text-xl sm:font-semibold mt-1 text-black dark:text-white text-base font-normal">162</h3>
                                    <p class="dark:text-white">Interested</p>
                                </div>
                            </div>
                            <div class="flex gap-3">
                                <div class="p-2 inline-flex rounded-full bg-rose-50 self-center"> <ion-icon name="leaf-outline" class="text-2xl text-rose-600 md hydrated" role="img" aria-label="leaf outline"></ion-icon></div>
                                <div>
                                    <h3 class="sm:text-xl sm:font-semibold mt-1 text-black dark:text-white text-base font-normal">162</h3>
                                    <p class="dark:text-white">Going</p>
                                </div>
                            </div> 
                        </div> 
                    

                        
                    </div>

                    <div class="bg-white p-5 dark:bg-slate-800 px-6">

                        <div class="flex items-baseline justify-between text-black dark:text-white">
                            <h3 class="font-bold text-base"> Verified Snookers In </h3>
                            <a href="#" class="text-sm text-blue-500">See all</a>
                        </div>

                        <div class="flex flex-col space-y-4 mt-4">

                            <div class="flex  justify-between">
                            <a href="timeline.html">
                                <img src="" alt="" class="side-list-image rounded-full">
                            </a>
                            <div class="flex-1 ">
                                <a href="timeline.html">
                                <h4 class="dark:text-white">Monroe Parker</h4>
                                </a>
                                <div class="dark:text-gray-300">Turkey</div>
                            </div>
                            <button class="btn">Verified</button>
                            </div>


                            <div class="flex  justify-between">
                                <a href="timeline.html">
                                    <img src="" alt="" class="side-list-image rounded-full">
                                </a>
                                <div class="flex-1">
                                    <a href="timeline.html"><h4 class="dark:text-white">  Martin Gray </h4></a>
                                    <div class="dark:text-gray-300"> Dubai</div>
                                </div>
                                <button class="btn">Verified</button>
                            </div>

                            <div class="flex  justify-between">
                                <a href="timeline.html">
                                    <img src="" alt="" class="side-list-image rounded-full">
                                </a>
                                <div class="flex-1">
                                    <a href="timeline.html"><h4 class="dark:text-white">  James Lewis </h4></a>
                                    <div class="dark:text-gray-300"> London</div>
                                </div>
                                <button class="btn">Verified</button>
                            </div>
                            
                        </div>

                    </div>
                    
                    <div class="bg-white dark:bg-slate-800 p-5 px-6 space-y-4">
                    
                        <h3 class="font-bold text-base text-black dark:text-white"> Created by </h3> 
                    
                        <div class="flex  justify-between">
                            <a href="timeline.html">
                                <img src="" alt="" class="side-list-image rounded-full">
                            </a>
                            <div class="flex-1">
                                <a href="timeline.html"><h4 class="dark:text-white">  Maria Gray</h4></a>
                                <div class="dark:text-gray-300">Turkey </div>
                            </div>
                            <!-- <a href="timeline.html" class="bg-secondery/60 button rounded-full">Profile</a> -->
                        </div>

                        <ul class="text-gray-600 space-y-4 text-sm dark:text-white/80">

                            <li class="flex items-center gap-3"> 
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 19.128a9.38 9.38 0 002.625.372 9.337 9.337 0 004.121-.952 4.125 4.125 0 00-7.533-2.493M15 19.128v-.003c0-1.113-.285-2.16-.786-3.07M15 19.128v.106A12.318 12.318 0 018.624 21c-2.331 0-4.512-.645-6.374-1.766l-.001-.109a6.375 6.375 0 0111.964-3.07M12 6.375a3.375 3.375 0 11-6.75 0 3.375 3.375 0 016.75 0zm8.25 2.25a2.625 2.625 0 11-5.25 0 2.625 2.625 0 015.25 0z"></path>
                                </svg>
                                <div> <span class="font-semibold text-black dark:text-white"> 5 </span> Events  </div>
                            </li>
                            <li class="flex items-center gap-3"> 
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M20.25 14.15v4.25c0 1.094-.787 2.036-1.872 2.18-2.087.277-4.216.42-6.378.42s-4.291-.143-6.378-.42c-1.085-.144-1.872-1.086-1.872-2.18v-4.25m16.5 0a2.18 2.18 0 00.75-1.661V8.706c0-1.081-.768-2.015-1.837-2.175a48.114 48.114 0 00-3.413-.387m4.5 8.006c-.194.165-.42.295-.673.38A23.978 23.978 0 0112 15.75c-2.648 0-5.195-.429-7.577-1.22a2.016 2.016 0 01-.673-.38m0 0A2.18 2.18 0 013 12.489V8.706c0-1.081.768-2.015 1.837-2.175a48.111 48.111 0 013.413-.387m7.5 0V5.25A2.25 2.25 0 0013.5 3h-3a2.25 2.25 0 00-2.25 2.25v.894m7.5 0a48.667 48.667 0 00-7.5 0M12 12.75h.008v.008H12v-.008z"></path>
                                </svg>
                                <div> on CueConnect since  <span class="font-semibold text-black dark:text-white"> 2020</span> </div>
                            </li>
                            
                        </ul>
                
                    </div>

                </div><div class="uk-sticky-placeholder" hidden="" style="height: 724px; width: 400px; margin: 0px;"></div>

            </div>

        </div>
        
    </div>

</div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useRoute } from 'vue-router';
import Counter from '@/components/pool/CountDown.vue'

const event = ref(null);
const route = useRoute();

onMounted(() => {
  const eventId = route.params.id;
  fetchEvent(eventId);
});

async function fetchEvent(eventId) {
  try {
    const response = await axios.get(`events/${eventId}`);
    event.value = response.data;
  } catch (error) {
    console.error('Error fetching event details:', error.message);
  }
}
</script>

<style>

</style>