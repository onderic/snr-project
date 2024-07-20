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
          <div class="relative">
           <ChartComponent/>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import axios from 'axios';
  import { Bar } from 'vue-chartjs';
  import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js';
  import ChartComponent from '@/components/ChartComponent.vue'
  
  ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale);
  
  const totals = ref({
    daily: 0,
    weekly: 0,
    monthly: 0
  });
  
  const chartData = ref({
    labels: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    datasets: [
      {
        label: 'Daily Revenue',
        data: [], // Revenue amounts should be here
        backgroundColor: '#4A90E2',
        borderColor: '#2C3E50',
        borderWidth: 1
      }
    ]
  });
  
  const chartOptions = ref({
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        labels: {
          color: 'gray'
        }
      }
    },
    scales: {
      x: {
        type: 'category',
        title: {
          display: true,
          text: 'Days'
        },
        ticks: {
          color: 'gray'
        },
        grid: {
          color: 'rgba(128, 128, 128, 0.2)'
        }
      },
      y: {
        title: {
          display: true,
          text: 'Revenue'
        },
        ticks: {
          color: 'gray'
        },
        grid: {
          color: 'rgba(128, 128, 128, 0.2)'
        }
      }
    }
  });
  
  onMounted(async () => {
    const darkModeMediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
    updateChartColors(darkModeMediaQuery.matches);
    darkModeMediaQuery.addEventListener('change', e => updateChartColors(e.matches));
  
    try {
      const response = await axios.get('/revenue-overview/');
      const data = response.data;
  
      totals.value = {
        daily: parseFloat(data.daily_fee),
        weekly: parseFloat(data.weekly_fee),
        monthly: parseFloat(data.monthly_fee)
      };
  
      // Manual days mapping
      const days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"];
      const dailyFees = data.daily_fees;
      const revenues = days.map(day => parseFloat(dailyFees[day]) || 0);
  
      chartData.value.labels = days;
      chartData.value.datasets[0].data = revenues;
  
      console.log('Chart Data:', chartData.value); // Debugging line to check chart data
    } catch (error) {
      console.error('Error fetching revenue data:', error);
    }
  });
  
  function updateChartColors(isDarkMode) {
    chartOptions.value.plugins.legend.labels.color = isDarkMode ? 'gray' : 'black';
    chartOptions.value.scales.x.ticks.color = isDarkMode ? 'gray' : 'black';
    chartOptions.value.scales.y.ticks.color = isDarkMode ? 'gray' : 'black';
    chartOptions.value.scales.x.grid.color = isDarkMode ? 'rgba(128, 128, 128, 0.2)' : '#ddd';
    chartOptions.value.scales.y.grid.color = isDarkMode ? 'rgba(128, 128, 128, 0.2)' : '#ddd';
  }
  </script>
  