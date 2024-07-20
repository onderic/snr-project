<template>
  <div>
    <!-- Progress Bar at the very top -->
    <ProgressBar :loading="loadingWithDelay" />

    <div class="flex h-screen overflow-hidden">
      <!-- Sidebar -->
      <Sidebar />

      <!-- Content Area -->
      <div class="relative flex flex-1 flex-col overflow-y-auto overflow-x-hidden">
        <!-- Header -->
        <HeaderArea/>

        <!-- Main Content -->
        <div class="p-4 sm:ml-64">
          <div class=" border-gray-200 border-none rounded-lg dark:border-gray-700">
            <router-view />
          </div>
        </div>
        
      </div>
    </div>
  </div>
</template>

<script setup>

import Sidebar from '@/components/Sidebar/SideBar.vue'
import HeaderArea from '@/components/Header/HeaderArea.vue'
import ProgressBar from '@/components/ProgressBar.vue'
import { refMinDelay } from '@/composables/refMinDelay'
import { provideLoading } from '@/composables/loading'
import { useToast } from 'vue-toastify';
import { ref, onMounted } from 'vue';


  const loading = provideLoading();
  const loadingWithDelay = refMinDelay(loading, 3000);
  const userCoordinates = ref({ latitude: null, longitude: null });
  const toast = useToast()

  function getUserLocation() {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        position => {
          userCoordinates.value.latitude = position.coords.latitude;
          userCoordinates.value.longitude = position.coords.longitude;
        },
        error => {
          console.error('Error getting user location:', error.message);
          toast.error('Location access denied by user.');
          // Fallback or default location
          userCoordinates.value.latitude = defaultLatitude;
          userCoordinates.value.longitude = defaultLongitude;
        }
      );
    } else {
      console.error('Geolocation is not supported by this browser.');
      // Fallback or default location
      userCoordinates.value.latitude = defaultLatitude;
      userCoordinates.value.longitude = defaultLongitude;
    }
  }

  onMounted(() => {
    getUserLocation();
  });

</script>
