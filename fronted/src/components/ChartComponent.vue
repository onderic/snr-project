<template>
    <div class="relative">
      <canvas id="myChart"></canvas>
    </div>
  </template>
  
  <script setup>
  import { onMounted, ref } from 'vue';
  import Chart from 'chart.js/auto';
  import axios from 'axios';
  
  const chartData = ref({
    labels: [],
    data: []
  });
  
  onMounted(async () => {
    try {
      const response = await axios.get('revenue-overview-graph/');
      chartData.value = response.data;
  
      const ctx = document.getElementById('myChart').getContext('2d');
  
      new Chart(ctx, {
        type: 'bar',
        data: {
          labels: ["Monday","Tuesday","Wendsday", "Thursday", "Friday"],
          datasets: [{
            label: 'Total Revenue (KES)',
            data: ['255','900','300','500', '800'],
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
          }]
        },
        options: {
          responsive: true, 
          maintainAspectRatio: false,
          scales: {
            x: {
              title: {
                display: true,
                text: 'Days of the Week'
              }
            },
            y: {
              beginAtZero: true,
              title: {
                display: true,
                text: 'Revenue (KES)'
              },
              ticks: {
                callback: function(value) {
                  return 'KES ' + value;
                }
              }
            }
          }
        }
      });
    } catch (error) {
      console.error('Error fetching chart data:', error);
    }
  });
  </script>
  
  <style scoped>
  .relative {
    width: 100%;
    height: 100%;
  }
  
  canvas {
    width: 100% !important; 
    height: auto !important; 
  }
  
  @media (min-width: 1024px) {
    .relative {
      height: 500px;
    }
  }
  </style>
  