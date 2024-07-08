<template>
  <div >
    <div v-if="loading">
      <Pool />
    </div>
    <div v-else class="flex-col space-y-6 dark:bg-slate-800 bg-white p-5 rounded-md">
      <h1 class="font-semibold text-2xl capitalize dark:text-white">
        Discover pool spaces around you
      </h1>
      <div v-for="poolSpace in poolSpaces" :key="poolSpace.id" class="dark:bg-slate-700 mb-5 rounded-xl shadow-xl text-sm font-medium dark:text-white w-full">
        <div class="flex gap-3 sm:p-4 p-2.5 text-sm font-medium">
          <a :href="'/profile/' + poolSpace.user.id">
            <img src="@/assets/ball.jpeg" alt="" class="w-9 h-9 rounded-full">
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
        <div class="sm:rounded-lg w-full h-full object-cover p-4">
          <GoogleMap :latitude="poolSpace.latitude" :longitude="poolSpace.longitude" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import axios from 'axios';
import { useLoading } from '@/composables/loading';
import { useToast } from 'vue-toastify';
import GoogleMap from "@/components/dahsboard/Map.vue";
import Pool from '@/components/Skeleton/Pool.vue';


const poolSpaces = ref([]);
const loading = useLoading();
const toast = useToast();

const defaultLatitude = 1.3028463; 
const defaultLongitude = 36.5355534;

async function getPoolSpaces(latitude, longitude) {
  if (latitude === undefined || longitude === undefined) {
    console.error('Latitude and longitude are required to fetch pool spaces.');
    return;
  }

  try {
    loading.value = true;
    const response = await axios.get('/pools/', {
      params: {
        latitude: latitude,
        longitude: longitude
      }
    });
    poolSpaces.value = response.data;
  } catch (error) {
    console.error('Error fetching pool spaces:', error.message);
  } finally {
    loading.value = false;
  }
}

function getUserLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      position => {
        const latitude = position.coords.latitude;
        const longitude = position.coords.longitude;
        getPoolSpaces(latitude, longitude);
      },
      error => {
        console.error('Error getting user location:', error.message);
        toast.error('Location access denied by user.');
        getPoolSpaces(defaultLatitude, defaultLongitude);
      }
    );
  } else {
    console.error('Geolocation is not supported by this browser.');
    toast.error('Geolocation is not supported by this browser.');
    getPoolSpaces(defaultLatitude, defaultLongitude);
  }
}

onMounted(() => {
  getUserLocation();
});


</script>
