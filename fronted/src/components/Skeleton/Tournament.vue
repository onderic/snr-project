<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <div>
    <div v-for="n in placeholders" :key="n" class="shadow-md rounded-lg overflow-hidden flex flex-col md:flex-row animate-pulse">
          <div class="md:w-40 md:h-full w-full h-36 overflow-hidden bg-gray-300 dark:bg-gray-700">
            <v-icon name="bi-image-fill" class=" w-full h-24 " />
          </div>
          <div class="md:flex gap-10 md:items-end flex-1 py-4 px-6 w-full">
            <div>
              <div class="h-2.5 bg-gray-200 rounded-full w-48 dark:bg-gray-700  mb-1"></div>
              <div class="h-4 bg-gray-200 rounded-full dark:bg-gray-700 w-48 mb-3"></div>
              <div class="h-2.5 bg-gray-200 rounded-full dark:bg-gray-700 w-20 mb-1 mt-3"></div>
              <div class="text-xs flex gap-16 dark:text-gray-300">
                <div class="h-2 bg-gray-200 rounded-full dark:bg-gray-700 w-16"></div>
                <div class="md:block hidden">·</div>
                <div class="h-2 bg-gray-200 rounded-full dark:bg-gray-700 w-20"></div>
              </div>
            </div>
          </div>
          <div class="flex flex-col sm:flex-row items-center gap-2 self-end pt-2 sm:justify-end mb-4">
            <div class="dark:bg-slate-700 bg-gray-300 dark:text-white px-2 py-1 rounded-lg w-full sm:w-auto h-8"></div>
            <div class="px-2.5 py-2 w-full sm:w-auto bg-gray-300 dark:bg-gray-700 rounded-lg h-8"></div>
          </div>
</div>
  </div>
</template>

<script  setup>
import { ref } from 'vue';
const placeholders = ref(6); 
</script>
