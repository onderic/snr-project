<template>
    <div v-if="loading" class="progress-bar-container mt-10">
      <div class="progress-bar"></div>
    </div>
  </template>
  

<script lang="ts" setup>

const props = defineProps<{
  loading: boolean
}>()

</script>


<style scoped>
.progress-bar-container {
  width: 100%;
  height: 4px;
  background-color: #f3f3f3;
  overflow: hidden;
  position: relative;
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
