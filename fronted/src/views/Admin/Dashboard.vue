<template>
    <div class="px-4 md:px-32 w-full mt-20">
      <div class="rounded-lg p-8 dark:border-gray-700 bg-white dark:bg-gray-800">
        <h1 class="mb-10 text-5xl font-serif dark:text-white">Dashboard</h1>
        <div class="flex flex-col gap-8 md:flex-row md:justify-between">
          <!-- card 1 -->
          <div
            class="flex flex-col gap-2 h-40 rounded-xl shadow-md p-6 w-full bg-white dark:bg-gray-700 bg-opacity-30 backdrop-filter backdrop-blur-lg"
          >
            <div class="font-semibold text-lg dark:text-white">Today</div>
            <div class="font-semibold text-5xl tracking-tight dark:text-white">${{ totals.daily.toFixed(2) }}</div>
            <div class="font-normal dark:text-gray-400">Gross volume</div>
          </div>
  
          <!-- card 2 -->
          <div
            class="flex flex-col gap-2 h-40 rounded-xl shadow-md p-6 w-full bg-white dark:bg-gray-700 bg-opacity-30 backdrop-filter backdrop-blur-lg"
          >
            <div class="font-semibold text-lg dark:text-white">Last Week</div>
            <div class="font-semibold text-5xl tracking-tight dark:text-white">${{ totals.weekly.toFixed(2) }}</div>
            <div class="font-normal dark:text-gray-400">Gross volume</div>
          </div>
  
          <!-- card 3 -->
          <div
            class="flex flex-col gap-2 h-40 rounded-xl shadow-md p-6 w-full bg-white dark:bg-gray-700 bg-opacity-30 backdrop-filter backdrop-blur-lg"
          >
            <div class="font-semibold text-lg dark:text-white">Last Month</div>
            <div class="font-semibold text-5xl tracking-tight dark:text-white">${{ totals.monthly.toFixed(2) }}</div>
            <div class="font-normal dark:text-gray-400">Gross volume</div>
          </div>
        </div>
        <div class="mt-10 rounded-lg shadow-md p-6">
          <h1 class="mb-10 text-3xl font-serif dark:text-white">Revenue Overview</h1>
          <div class="">
            <ChartComponent/>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import axios from 'axios';
  import ChartComponent from '@/components/ChartComponent.vue';
  
  const totals = ref({
    daily: 0,
    weekly: 0,
    monthly: 0
  });
  
  
  onMounted(async () => {
    try {
      // Fetch revenue totals
      const response = await axios.get('revenue-overview/');
      const data = response.data;
  
      totals.value = {
        daily: parseFloat(data.daily_fee),
        weekly: parseFloat(data.weekly_fee),
        monthly: parseFloat(data.monthly_fee)
      };

    } catch (error) {
      console.error('Error fetching data:', error);
    }
  });
  </script>
  
  <style scoped>
  .relative {
    width: 100%;
    height: 100%; /* Make sure the container takes the full available height */
  }
  
  canvas {
    width: 100% !important; /* Make sure the canvas scales with the container */
    height: auto !important; /* Maintain aspect ratio */
  }
  
  @media (min-width: 1024px) {
    .relative {
      height: 500px;
    }
  }
  </style>
  