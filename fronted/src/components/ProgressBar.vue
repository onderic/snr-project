<template>
  <div v-if="loading" class="progress-bar-container">
    <div class="progress-bar"></div>
  </div>
</template>

<script setup>
// eslint-disable-next-line no-unused-vars
const props = defineProps({
  loading: {
    type: Boolean,
    required: true
  }
});
</script>

<style>
.progress-bar-container {
  position: fixed;
  top: 64px; 
  left: 0;
  width: 100%;
  height: 4px; 
  background-color: #f3f3f3;
  overflow: hidden;
  z-index: 9999;
}

.progress-bar {
  width: 100%;
  height: 100%;
  background-color: #007bff;
  animation: loading 2s linear infinite;
}

@keyframes loading {
  0% {
    transform: translateX(-100%);
  }
  100% {
    transform: translateX(100%);
  }
}
</style>
