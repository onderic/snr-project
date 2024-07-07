<template>
    <div class="xl:w-[680px] sm:w-96 sm:relative rounded-xl overflow-hidden z-20 bg-gray-100 dark:bg-slate-900 max-md:hidden w-screen left-0 max-sm:fixed max-sm:top-2 dark:!bg-white/5">
      <input
        type="text"
       class="w-full !pl-10 !font-normal !bg-transparent h-12 !text-sm"
        placeholder="Search..."
        v-model="query"
        @input="onSearch"
      />
      <div v-if="searchResults.length > 0" class="absolute w-full bg-white dark:bg-gray-800 rounded-md shadow-lg mt-1">
        <ul>
          <li v-for="event in searchResults" :key="event.id" class="p-2 hover:bg-gray-100 dark:hover:bg-gray-700">
            {{ event.title }}
          </li>
        </ul>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import axios from 'axios';
  import { useDebounceFn } from '@vueuse/core';
  
  const query = ref("");
  const searchResults = ref([]);
  
  const onSearch = useDebounceFn(async () => {
    if (query.value) {
      try {
        const response = await axios.get(`/events/search?query=${query.value}`);
        searchResults.value = response.data;
      } catch (error) {
        console.error('Error fetching search results:', error.message);
      }
    } else {
      searchResults.value = [];
    }
  }, 300);
  </script>
  
  <style>
  /* Your existing styles */
  </style>
  