<template>
   <div>
    <div v-for="n in placeholders" :key="n" class="dark:bg-slate-700 mb-5 rounded-xl shadow-xl text-sm font-medium dark:text-white w-full">
        <div class="flex gap-20 sm:p-4 p-2.5 text-sm font-medium">
          <div class="w-12 h-12 rounded-full bg-gray-300"></div> 
          <div class="flex-1">
            <div class="text-black dark:text-white bg-gray-300 h-4 w-60 mb-1"></div> 
            <div class="text-xs text-gray-500 dark:text-white/80 bg-gray-300 h-2 w-60"></div> 
          </div>
          <div class="-mr-1">
            <button type="button" class="button-icon w-10 h-10 bg-gray-300" aria-haspopup="true" aria-expanded="false"></button> 
          </div>
        </div>
        <div class="sm:rounded-lg w-full h-48 object-cover p-4 bg-gray-300"></div> 
      </div>
   </div>
</template>


<script  setup>
import { ref } from 'vue';
const placeholders = ref(6); 
</script>

<style>

</style>