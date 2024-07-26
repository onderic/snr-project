<template>
    <div class="flex flex-col items-center">
      <div class="relative w-16 h-16">
        <div class="absolute inset-0 flex items-center justify-center">
          <div class="w-8 h-8 border-t-4 border-blue-500 border-solid rounded-full animate-spin"></div>
        </div>
      </div>
      <p class="mt-4 text-sm font-medium text-gray-900 dark:text-white">{{ message }}</p>
    </div>
  </template>
  
  <script setup>
  import { defineProps } from 'vue';
  
  const props = defineProps({
    message: {
      type: String,
      default: 'Processing...'
    }
  });
  </script>
  
  <style scoped>
  /* Spinner animation */
  @keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }
  
  .animate-spin {
    animation: spin 1s linear infinite;
  }
  </style>
  