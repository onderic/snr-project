<template>
  <div class="w-full dark:bg-slate-800 bg-white p-5 rounded-md">
    <div>
      <ol class="flex items-center w-full mb-4 sm:mb-5">
        <li class="flex w-full items-center text-blue-600 dark:text-blue-500 after:content-[''] after:w-full after:h-1 after:border-b after:border-blue-100 after:border-4 after:inline-block dark:after:border-blue-800">
          <div class="flex items-center justify-center w-10 h-10 bg-blue-100 rounded-full lg:h-12 lg:w-12 dark:bg-blue-800 shrink-0">
            <v-icon name="co-library-add" scale="" />
          </div>
        </li>
        <li class="flex w-full items-center after:content-[''] after:w-full after:h-1 after:border-b after:border-gray-100 after:border-4 after:inline-block dark:after:border-gray-700">
          <div class="flex items-center justify-center w-10 h-10 bg-gray-100 rounded-full lg:h-12 lg:w-12 dark:bg-white shrink-0">
            <v-icon name="io-locate-outline" animation="spin" color="blue" scale="" />
          </div>
        </li>
        <li class="flex items-center w-full">
          <div class="flex items-center justify-center w-10 h-10 bg-gray-100 rounded-full lg:h-12 lg:w-12 dark:bg-white shrink-0">
            <v-icon name="io-checkmark-done-outline" scale="" />
          </div>
        </li>
      </ol>
      <h3 class="mb-4 text-lg font-medium leading-none text-gray-900 dark:text-white capitalize">Pool registration here..</h3>
      <div class="grid gap-4 mb-4 sm:grid-cols-2">
        <div>
          <label for="title" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Title</label>
          <input v-model="title" type="text" id="title" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Pool Name" required="">
        </div>
        <div>
          <label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Owner Email</label>
          <input v-model="email" type="email" id="email" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="name@pool.com" required="">
        </div>
        <div>
          <label for="number" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Number of Tables</label>
          <input v-model="number" type="number" id="number" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="23" required="">
        </div>
        <div>
          <label for="height" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Table Height</label>
          <input v-model="height" type="number" id="height" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="3fts" required="">
        </div>
      </div>
    </div>

    <div class="mt-10">
      <h1 class="dark:text-white text-dark text-xl font-semibold mb-4">Location Section</h1>
      <div class="relative">
        <!-- Map Container -->
        <div ref="mapContainer" class="w-full" style="height: 300px;"></div>
        
        <!-- Loading Spinner -->
        <div v-if="mapLoading" class="absolute inset-0 flex items-center justify-center bg-gray-100 bg-opacity-75 z-10">
          <v-icon name="gi-spinning-blades" animation="spin" scale="2" />
        </div>
      </div>

      <div class="mt-5">
        <div class="dark:bg-gray-700 bg-gray-100 p-5 rounded-md space-y-3">
          <p class="dark:text-white text-dark text-xl">Coordinates: <span class="font-bold">{{ lat }}, {{ lng }}</span></p>
          <p class="dark:text-white text-dark text-lg mt-3">Address: <span class="italic font-semibold">{{ truncatedAddress }}</span></p>
        </div>

        <div class="flex mt-4 items-center p-4 mb-4 text-sm text-blue-800 border border-blue-300 rounded-lg bg-blue-50 dark:bg-gray-800 dark:text-blue-400 dark:border-blue-800" role="alert">
          <v-icon name="fc-info" class="mr-2" />
          <span class="sr-only">Info</span>
          <div>
            <span class="font-medium">Info alert!</span> You can alternatively drag the marker on the map to choose a different location.
          </div>
        </div>
      </div>
    </div>
    <button @click="submitForm" type="submit" class="btn">
      <v-icon v-if="loading" name="gi-spinning-blades" animation="spin" scale="1"/> 
      Submit 
    </button>
  </div>
</template>

<script setup>
import 'leaflet/dist/leaflet.css';
import { onMounted, ref, onUnmounted, computed } from 'vue';
import L from 'leaflet';
import { useToast } from 'vue-toastify';
import { useUserStore } from '@/stores/user';
import axios from 'axios';
import { useLoading } from '@/composables/loading';
import router from '@/router'; 

const lat = ref(0);
const lng = ref(0);
const address = ref('');
const map = ref(null);
const mapContainer = ref(null);
const mapLoading = ref(true);
const toast = useToast();
const userStore = useUserStore();
const loading = useLoading();

const truncatedAddress = computed(() => {
  const maxLength = 200;
  return address.value.length > maxLength ? address.value.slice(0, maxLength) + '...' : address.value;
});

function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.watchPosition(
      (position) => {
        lat.value = position.coords.latitude;
        lng.value = position.coords.longitude;
        
        if (!map.value) {
          map.value = L.map(mapContainer.value).setView([lat.value, lng.value], 13);
          L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
            attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
          }).addTo(map.value);
        } else {
          map.value.setView([lat.value, lng.value], 13);
        }
        
        const marker = L.marker([lat.value, lng.value], { draggable: true })
          .addTo(map.value)
          .on('dragend', (event) => {
            const newLatLng = event.target.getLatLng();
            lat.value = newLatLng.lat;
            lng.value = newLatLng.lng;
            getAddress(newLatLng.lat, newLatLng.lng);
          });
        
        getAddress(lat.value, lng.value);
        mapLoading.value = false; 
      },
      (error) => {
        if (error.code === error.PERMISSION_DENIED) {
          toast.error('Location access denied by user.');
        }
      }
    );
  } else {
    toast.error('Geolocation is not supported by this browser.');
  }
}

async function getAddress(latitude, longitude) {
  try {
    const response = await fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${latitude}&lon=${longitude}`);
    const data = await response.json();
    address.value = data.display_name;
  } catch (error) {
    console.error('Error fetching address:', error);
    address.value = 'Unable to fetch address';
  }
}

async function submitForm() {
  try {
    loading.value = true;
    const formData = {
      title: title.value,
      email: email.value,
      number: number.value,
      height: height.value,
    };
    const data = {
      ...formData,
      latitude: lat.value,
      longitude: lng.value,
      address: address.value,
      user: userStore.user.id
    };
    console.log(data);
    const response = await axios.post('create-pool/', data);
    console.log('Response:', response.data);
    toast.success('Pool space created successfully pending approval');
    router.push('/manage-pool');
    userStore.updateUserRole('owner');
  } catch (error) {
    console.error('Error creating event:', error);
    toast.error('Something went wrong');
  } finally {
    loading.value = false;
  }
}

onMounted(() => {
  getLocation();
});

onUnmounted(() => {
  if (map.value) {
    map.value.remove();
    map.value = null;
  }
});
</script>

<style scoped>
#mapContainer {
  width: 100%;
  height: 300px;
}

#mapContainer .leaflet-container {
  position: relative;
}

#mapContainer .loading-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(255, 255, 255, 0.7);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 10;
}
</style>
