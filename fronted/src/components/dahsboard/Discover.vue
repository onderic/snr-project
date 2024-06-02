<template>
  <div class="flex-col space-y-6 bg-slate-600 p-5 rounded-md">
    <h1 class="font-semibold text-2xl capitalize dark:text-white">Discover pool spaces around you</h1>
    <div>
      <div v-for="poolSpace in poolSpaces" :key="poolSpace.id" class="dark:bg-slate-800 mb-5 rounded-xl shadow-sm text-sm font-medium dark:text-white w-full">
        <!-- Post heading -->
        <div class="flex gap-3 sm:p-4 p-2.5 text-sm font-medium">
          <a :href="'/profile/' + poolSpace.user.id">
            <img src="@/assets/ball.jpeg " alt="" class="w-9 h-9 rounded-full">
          </a>
          <div class="flex-1">
            <a :href="'/profile/' + poolSpace.user.id">
              <h4 class="text-black dark:text-white">{{ poolSpace.title }}</h4>
            </a>
            <div class="text-xs text-gray-500 dark:text-white/80">{{ poolSpace.address }}</div>
          </div>
          <div class="-mr-1">
            <button type="button" class="button-icon w-8 h-8" aria-haspopup="true" aria-expanded="false">
              <ion-icon class="text-xl md hydrated" name="ellipsis-horizontal" role="img" aria-label="ellipsis horizontal">...</ion-icon>
            </button>
          </div>
        </div>

        <!-- Post image -->
        <a href="#preview_modal">
          <div class="sm:rounded-lg w-full h-full object-cover p-4">
            <GoogleMap :latitude="poolSpace.latitude" :longitude="poolSpace.longitude" />
          </div>
        </a>

     
      </div>
    </div>
  </div>
</template>

<script setup>
import GoogleMap from "@/components/dahsboard/Map.vue";
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useLoading } from '@/composables/loading';

const poolSpaces = ref([]);
const loading = useLoading();

async function getPoolSpaces() {
  try {
    loading.value = true;
    const response = await axios.get('pools/');
    poolSpaces.value = response.data;
  } catch (error) {
    console.error('Error fetching pool spaces:', error.message);
  } finally {
    loading.value = false;
  }
}

onMounted(() => {
  getPoolSpaces();
});
</script>

<style scoped>
/* Add any custom styles here */
</style>
