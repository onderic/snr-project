<template>
    <div>
      <iframe
        width="500"
        height="450"
        frameborder="0"
        style="border:0"
        :src="mapUrl"
        allowfullscreen
      ></iframe>
    </div>
  </template>
  
  <script setup>
  import config from '../../../config'; 

  const apiKey = config.Googl_API_KEY;
  const latitude = 37.7749;
  const longitude = -122.4194;
  
  import { computed } from 'vue';
  
  const mapUrl = computed(() => {
    return `https://www.google.com/maps/embed/v1/place?key=${apiKey}&q=${latitude},${longitude}`;
  });
  </script>
  