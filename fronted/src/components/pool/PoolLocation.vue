<template>
  <div class="mt-10">
    <div ref="mapContainer" style="width: 100%; height: 400px;"></div>
    <button @click="getLocation" class="btn mt-10">Get Location</button>
    <p class="text-white text-xl">{{ lat }} , {{ lng }}</p>
    <p class="text-white text-xl">{{ address }}</p>
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

onMounted(() => {
  if (!map.value) {
    map.value = L.map(mapContainer.value).setView([51.505, -0.09], 13);
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 19,
      attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    }).addTo(map.value);
  }
});

onUnmounted(() => {
  if (map.value) {
    map.value.remove();
    map.value = null;
  }
});

function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.watchPosition(
      (position) => {
        lat.value = position.coords.latitude;
        lng.value = position.coords.longitude;
        map.value.setView([lat.value, lng.value], 13);

        L.marker([lat.value, lng.value], { draggable: true })
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
</script>

<style scoped>
#mapContainer {
  width: 100%;
  height: 400px;
}
</style>
