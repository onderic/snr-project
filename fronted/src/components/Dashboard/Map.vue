<template>
  <div>
    <div class="relative">
      <!-- Loader for small map iframe -->
      <div v-if="mapLoading" class="absolute inset-0 flex items-center justify-center bg-gray-100 bg-opacity-75 z-10">
        <v-icon name="gi-spinning-blades" animation="spin" scale="2" />
      </div>

      <!-- Small Map -->
      <iframe
        width="500"
        height="450"
        frameborder="0"
        style="border:0"
        :src="mapUrl"
        @load="onIframeLoad"
        allowfullscreen
      ></iframe>
    </div>

    <!-- Toggle Button -->
    <div class="flex justify-between p-4">
      <button></button>
      <button @click="openModal" class="btn">
        <v-icon name="io-expand-sharp" />
        View
      </button>
    </div>

    <!-- Modal -->
    <div v-if="isModalOpen" @click="closeModal" class="fixed inset-0 z-50 flex items-center justify-center w-full h-full bg-black bg-opacity-75">
      <div @click.stop class="relative p-4 w-full max-w-7xl max-h-full">
        <!-- Modal content -->
        <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
          <!-- Modal header -->
          <div class="flex justify-end p-2">
            <button @click="closeModal" class="text-gray-400 hover:text-gray-900 dark:hover:text-white">
              <v-icon name="io-close-sharp" />
            </button>
          </div>
          <!-- Modal body -->
          <div class="relative p-4 md:p-5 space-y-4">
            <!-- Loader for modal iframe -->
            <div v-if="mapLoading" class="absolute inset-0 flex items-center justify-center bg-gray-100 bg-opacity-75 z-10">
              <v-icon name="gi-spinning-blades" animation="spin" scale="2" />
            </div>

            <iframe
              width="100%"
              height="650"
              frameborder="0"
              style="border:0"
              :src="mapUrl"
              @load="onIframeLoad"
              allowfullscreen
            ></iframe>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import config from '../../../config'; 
import { ref, computed } from 'vue';

const apiKey = config.Googl_API_KEY;

const props = defineProps({
  latitude: {
    type: Number,
    required: true
  },
  longitude: {
    type: Number,
    required: true
  }
});

const isModalOpen = ref(false);
const mapLoading = ref(true);

function openModal() {
  isModalOpen.value = true;
  mapLoading.value = true; // Reset loading state when opening the modal
}

function closeModal() {
  isModalOpen.value = false;
}

function onIframeLoad() {
  mapLoading.value = false;
}

const mapUrl = computed(() => {
  return `https://www.google.com/maps/embed/v1/place?key=${apiKey}&q=${props.latitude},${props.longitude}`;
});
</script>

<style scoped>
.fixed {
  position: fixed;
}
.inset-0 {
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
}
.z-50 {
  z-index: 50;
}
.absolute {
  position: absolute;
}
.bg-opacity-75 {
  background-opacity: 0.75;
}
</style>
