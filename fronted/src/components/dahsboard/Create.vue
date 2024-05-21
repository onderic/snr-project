<template>
  <div>
    <h1 class="text-lg text-white">Create here</h1>
  </div>
   
</template>

<script setup>


const emit = defineEmits(['update-tournaments']);

const updateTournaments = () => {
  emit('update-tournaments');
};

</script>

<style>

</style>