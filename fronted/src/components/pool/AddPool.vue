<template>
    <div class="text-white mt-10">
      <h1>Adding Pool...</h1>
      <p v-if="loadingWithDelay">Please wait, adding pool...</p>
      <p v-else>Pool added successfully!</p>
      <div v-if="data">
        <h2 class="text-white">Fetched Data:</h2>
        <pre  class="text-white">{{ data }}</pre>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import { useLoading } from '@/composables/loading'
  import { refMinDelay } from '@/composables/refMinDelay'
  
  const data = ref(null)
  const loading = useLoading()
  const loadingWithDelay = refMinDelay(loading)


  const fetchData = async () => {
    loading.value = true
    try {
      const response = await fetch('https://jsonplaceholder.typicode.com/posts/1')
      data.value = await response.json()
    } finally {
      loading.value = false
    }
  }
  
  onMounted(() => {
    fetchData()
  })
  </script>
  