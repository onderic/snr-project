<template>
  <div>
    <div  class="w-full">
      <ol class="flex items-center w-full mb-4 sm:mb-5 mt-16">
      <li class="flex w-full items-center text-blue-600 dark:text-blue-500 after:content-[''] after:w-full after:h-1 after:border-b after:border-blue-100 after:border-4 after:inline-block dark:after:border-blue-800">
          <div class="flex items-center justify-center w-10 h-10 bg-blue-100 rounded-full lg:h-12 lg:w-12 dark:bg-blue-800 shrink-0">
              <v-icon name="co-library-add"   scale=""/> 
          </div>
      </li>
      <li class="flex w-full items-center after:content-[''] after:w-full after:h-1 after:border-b after:border-gray-100 after:border-4 after:inline-block dark:after:border-gray-700">
          <div class="flex items-center justify-center w-10 h-10 bg-gray-100 rounded-full lg:h-12 lg:w-12 dark:bg-white shrink-0">
              <v-icon name="io-locate-outline" animation="spin" color="blue"  scale=""/> 
          </div>
      </li>
      <li class="flex items-center w-full">
          <div class="flex items-center justify-center w-10 h-10 bg-gray-100 rounded-full lg:h-12 lg:w-12 dark:bg-white shrink-0">
              <v-icon name="io-checkmark-done-outline"   scale=""/> 
          </div>
      </li>
  </ol>
  <form action="#">
      <h3 class="mb-4 text-lg font-medium leading-none text-gray-900 dark:text-white capitalize">Pool registration here</h3>
      <div class="grid gap-4 mb-4 sm:grid-cols-2">
          <div>
              <label for="title" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Title</label>
              <input type="text" name="title" id="title" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Pool Name" required="">
          </div>
          <div>
              <label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Owner Email</label>
              <input type="email" name="email" id="email" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="name@pool.com" required="">
          </div>
          <div>
              <label for="number" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Number of  Tables</label>
              <input type="number" name="number" id="number" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="23" required="">
          </div>                        <div>
              <label for="height" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Table Height</label>
              <input type="number" name="height" id="height" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="3fts" required="">
          </div>
      </div>
      
  </form>
  </div>
  
    <div class="mt-10">
      <h1 class="dark:text-white text-xl font-semibold mb-4">Location Section</h1>
      <div ref="mapContainer" style="width: 100%; height: 400px;"></div>
      <div class="mt-5">
      <div class="dark:bg-gray-700 p-5 rounded-md space-y-3">
        <p class="text-white text-xl">Coordinates: <span class="font-bold">{{ lat }}, {{ lng }}</span></p>
        <p class="text-white text-lg mt-3">Address: <span class="italic">{{ address }}</span></p>
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
    <button type="submit" class="btn">
         Submit 
      </button>
  </div>
  </template>
  
  <script setup>
  import 'leaflet/dist/leaflet.css';
  import { onMounted, ref, onUnmounted } from 'vue';
  import L from 'leaflet';
  import { useToast } from 'vue-toastify';
  
  const lat = ref(0);
  const lng = ref(0);
  const address = ref('');
  const map = ref(null);
  const mapContainer = ref(null);
  const toast = useToast();
  
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
    height: 500px;
  }
  </style>  