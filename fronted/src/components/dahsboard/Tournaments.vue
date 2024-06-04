<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <div>
    <ProgressBar :loading="loading" />
    <div class="box p-5 dark:bg-slate-800 bg-white shadow-xl rounded-md">
      <h1 class="font-semibold text-2xl capitalize dark:text-white mb-4">Top curated Tournaments for you</h1>
      <div v-if="loading" class="space-y-4">
        <Skeleton/>
      </div>
      <div v-else>
        <div v-for="event in events" :key="event.id" class="shadow-md rounded-lg overflow-hidden flex flex-col md:flex-row">
          <div class="md:w-40 md:h-full w-full h-36 overflow-hidden">
            <router-link :to="{ name: 'event-detail', params: { id: event.id } }">
              <img src="https://cdn.pixabay.com/photo/2020/08/15/03/19/billiards-5489526_1280.jpg" alt="Event Image" class="w-full h-full object-cover">
            </router-link>
          </div>
          <div class="md:flex gap-10 md:items-end flex-1 py-4 px-6">
            <div>
              <p class="text-xs font-medium text-green-500 mb-1">{{ event.start_time }}</p>
              <router-link :to="{ name: 'event-detail', params: { id: event.id } }">
                <h3 class="text-base font-semibold dark:text-white">{{ event.title }}</h3>
              </router-link>
              <p class="text-xs font-medium mb-1 mt-3 text-black dark:text-white">Nandi County</p>
              <div class="text-xs flex gap-2 dark:text-gray-300">
                <div>272 Interested</div>
                <div class="md:block hidden">·</div>
                <div>126.9K going</div>
              </div>
            </div>
          </div>
          <div class="flex flex-col sm:flex-row items-center gap-2 self-end pt-2 sm:justify-end mb-4">
            <button type="button" class="dark:bg-slate-700 dark:text-white px-2 py-1 rounded-lg w-full sm:w-auto">Interested</button>
            <button type="button" class="px-2.5 py-2 w-full sm:w-auto"><ion-icon name="arrow-redo" class="text-base"></ion-icon></button>
          </div>
        </div>

        <hr class="card-list-divider" />
      </div>
    </div>
    <div class="flex justify-center my-6">
      <button type="button" class="bg-white py-2 px-5 rounded-full shadow-md font-semibold text-sm dark:bg-dark2">Load more...</button>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { provideLoading } from '@/composables/loading';
import ProgressBar from '@/components/ProgressBar.vue';
import Skeleton from '@/components/Skeleton/Tournament.vue';

const loading = provideLoading();
const events = ref([]);


async function get_events() {
  try {
    loading.value = true;
    const response = await axios.get('events/');
    events.value = response.data;
    console.log("events", response.data);
  } catch (error) {
    console.error('Error fetching pool spaces:', error.message);
  } finally {
    loading.value = false;
  }
}

onMounted(() => {
  get_events();
});
</script>

<style>
/* Your existing styles */
</style>
