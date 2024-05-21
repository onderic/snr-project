<template>
    <div>
    <h1 class="text-lg text-white">Discover here</h1>
  </div>
</template>


<script setup>
import Button from 'primevue/button';


const emit = defineEmits(['update-tournaments']);

const updateTournaments = () => {
  emit('update-tournaments');
};

</script>


<style>

</style>