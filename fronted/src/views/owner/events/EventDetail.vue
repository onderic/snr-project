<template>
    <div class="">
  <div v-if="!event" class="2xl:max-w-[1220px] max-w-[1065px] mx-auto mt-20">
  <div>
    <div class="bg-white dark:bg-slate-800 shadow lg:rounded-b-2xl lg:-mt-10 dark:bg-dark2">
      <div class="relative overflow-hidden w-full">
        <div class="h-96 bg-gray-300 dark:bg-slate-700 w-full"></div>
        <div class="w-full bottom-0 absolute left-0 bg-gradient-to-t from-black/60 pt-10 z-10"></div>
      </div>

      <div class="lg:px-10 md:p-5 p-3">
        <div class="flex flex-col justify-center md:-mt-20 -mt-12">
          <div class="md:w-20 md:h-20 w-12 h-12 bg-gray-300 dark:bg-slate-700 shadow-md rounded-md z-10 mb-5"></div> 
          <div class="flex lg:items-center justify-between max-lg:flex-col max-lg:gap-2">
            <div class="flex-1">
              <div class="h-3 w-80 bg-gray-300 dark:bg-slate-700 mb-1.5"></div> 
              <div class="h-8 w-full bg-gray-300 dark:bg-slate-700"></div>
              <div class="font-normal text-gray-500 mt-2 flex gap-2 dark:text-white/80">
                <div class="h-3 w-56 bg-gray-300 dark:bg-slate-700"></div>
                <div class="h-3 w-28 bg-gray-300 dark:bg-slate-700"></div>
                <div class="h-3 w-64 bg-gray-300 dark:bg-slate-700"></div>
              </div>
            </div>
            <div>
              <div class="h-10 w-64 bg-gray-300 dark:bg-slate-700"></div>
            </div>
          </div>
        </div>
      </div>

      <div class="flex items-center justify-between px-2 max-md:flex-col">
        <div class="flex items-center gap-2 text-sm py-2 pr-1 lg:order-1">
          <div class="h-8 w-64 bg-gray-300 dark:bg-slate-700"></div>
          <div class="btn">
            <div class="h-4 w-64 bg-gray-300 dark:bg-slate-700"></div>
            <span class="text-sm">Fee: <span class="h-4 w-40 bg-gray-300 dark:bg-slate-700"></span></span>
          </div>
        </div>

        <nav class="flex gap-0.5 rounded-xl overflow-hidden -mb-px text-gray-500 font-medium text-sm overflow-x-auto dark:text-white/80">
          <div class="inline-block py-3 leading-8 px-3.5 h-8 w-64 bg-gray-300 dark:bg-slate-700"></div>
          <div class="inline-block py-3 leading-8 px-3.5 h-8 w-64 bg-gray-300 dark:bg-slate-700"></div>
        </nav>
      </div>
    </div>

    <div class="flex 2xl:gap-12 gap-10 mt-8 max-lg:flex-col" id="js-oversized">
      <div class="flex-1 space-y-4">
        <div class="bg-white dark:bg-slate-800 p-5 px-6 relative">
          <div class="h-8 w-full bg-gray-300 dark:bg-slate-700"></div> 
          <div class="space-y-4 leading-7 tracking-wide mt-4 text-black text-sm dark:text-white">
            <div class="h-6 w-full bg-gray-300 dark:bg-slate-700"></div>
            <div class="h-6 w-4/5 bg-gray-300 dark:bg-slate-700"></div>
            <div class="h-6 w-3/4 bg-gray-300 dark:bg-slate-700"></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>


  <div v-else class="2xl:max-w-[1220px] max-w-[1065px] mx-auto lg:mt-20 mt-4">
    <div>
      <div class="bg-white dark:bg-slate-800 shadow lg:rounded-b-2xl lg:-mt-10 dark:bg-dark2">
        <div class="relative overflow-hidden w-full">
          <img src="@/assets/event.png" alt="" class="h-full w-full object-cover inset-0">
          <div class="w-full bottom-0 absolute left-0 bg-gradient-to-t from-black/60 pt-10 z-10"></div>
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
                <h3 class="md:text-2xl text-base font-bold text-black dark:text-white">{{ event.title }}</h3>
                <p class="font-normal text-gray-500 mt-2 flex gap-2 dark:text-white/80">
                  <span> Free </span>
                  <span> • </span>
                  <span> Physical event </span>
                </p>
              </div>
              <div>
                <Counter v-if="event" :startTime="event.start_time"/>
              </div>
            </div>
          </div>
        </div>

        <div class="flex items-center justify-between px-2 max-md:flex-col">
          <div class="flex items-center gap-2 text-sm py-2 pr-1 lg:order-1">
            <Enroll v-if="event" :eventId="event.id"/>
            <div class="btn">
              <ion-icon name="checkmark-circle-outline" class="text-xl md hydrated" role="img" aria-label="checkmark circle outline"></ion-icon>
              <span class="text-sm">Fee: {{ event.enrollment_fee }} </span>
            </div>
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

          <div class="bg-white dark:bg-slate-800 p-5 px-6 relative">
            <h3 class="font-semibold text-lg text-black dark:text-white"> Discussions </h3>
            <div class="text-sm font-normal space-y-4 relative mt-4">
              <div class="flex items-start gap-3 relative">
                <a class="dark:bg-white bg-gray-200 rounded-full p-1"><v-icon name="co-user" scale="2"/></a>
                <div class="flex-1">
                  <a href="timeline.html" class="text-black font-medium inline-block dark:text-white"> Monroe Parker </a>
                  <p class="mt-0.5 dark:text-gray-300">Cant wait to snooker them </p>
                </div>
              </div>
              <div class="flex items-start gap-3 relative">
                <a class="dark:bg-white bg-gray-200 rounded-full p-1"><v-icon name="co-user" scale="2"/></a>
                <div class="flex-1">
                  <a href="timeline.html" class="text-black font-medium inline-block dark:text-white"> John Michael </a>
                  <p class="mt-0.5 dark:text-gray-300">You captured the moment.😎</p>
                </div>
              </div>
              <div class="flex items-start gap-3 relative">
                <a class="dark:bg-white bg-gray-200 rounded-full p-1"><v-icon name="co-user" scale="2"/></a>
                <div class="flex-1">
                  <a href="timeline.html" class="text-black font-medium inline-block dark:text-white"> James Lewis </a>
                  <p class="mt-0.5 dark:text-gray-300">Cant wait to snooker them </p>
                </div>
              </div>
              <div class="flex items-start gap-3 relative">
                <a class="dark:bg-white bg-gray-200 rounded-full p-1"><v-icon name="co-user" scale="2"/></a>
                <div class="flex-1">
                  <a href="timeline.html" class="text-black font-medium inline-block dark:text-white"> Martin Gray </a>
                  <p class="mt-0.5 dark:text-gray-300">You captured the moment.😎</p>
                </div>
              </div>
              <div>
                <button type="button" class="btn">
                  More Comment
                </button>
              </div>
            </div>

            <div class="sm:px-4 sm:py-3 p-2.5 border-t border-gray-100 flex items-center gap-1 -m-6 mt-0 bg-gray-100 dark:bg-slate-700 dark:border-slate-700/40">
              <v-icon name="co-user" scale="2"/>
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
                  <div class="p-2 inline-flex rounded-full bg-rose-50 self-center"><ion-icon name="heart" class="text-2xl text-rose-600 md hydrated" role="img" aria-label="heart"></ion-icon></div>
                  <div>
                    <h3 class="sm:text-xl sm:font-semibold mt-1 text-black dark:text-white text-base font-normal">162</h3>
                    <p class="dark:text-white">Interested</p>
                  </div>
                </div>
                <div class="flex gap-3">
                  <div class="p-2 inline-flex rounded-full bg-rose-50 self-center"><ion-icon name="leaf-outline" class="text-2xl text-rose-600 md hydrated" role="img" aria-label="leaf outline"></ion-icon></div>
                  <div>
                    <h3 class="sm:text-xl sm:font-semibold mt-1 text-black dark:text-white text-base font-normal">{{event.attendees_count}}</h3>
                    <p class="dark:text-white">Going</p>
                  </div>
                </div>
              </div>
            </div>

            <div class="bg-white p-5 dark:bg-slate-800 px-6 lg:order-1">
              <h3 class="font-semibold text-lg text-black dark:text-white"> Location </h3>
              <div class="relative overflow-hidden rounded-md w-full mt-4 aspect-video bg-red-500">
                <iframe 
                    :src="getGoogleMapsUrl(event.pool_space.latitude, event.pool_space.longitude)"
                    allowfullscreen
                ></iframe>
              </div>
              <div class="text-black dark:text-white mt-2 font-semibold text-sm space-y-2">
                <p class="m-0">{{event.location}}</p>
              </div>
            </div>

         
          </div>
        </div>
      </div>
    </div>
  </div>

    </div>


</template>
<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useRoute } from 'vue-router';
import Counter from '@/components/Tournaments/CountDown.vue';
import Enroll from '@/components/Tournaments/EnrollTournament.vue';

const event = ref(null);
const route = useRoute();

// Function to construct Google Maps URL
function getGoogleMapsUrl(latitude, longitude) {
  return `https://maps.google.com/maps?q=${latitude},${longitude}&hl=en&z=14&output=embed`;
}

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