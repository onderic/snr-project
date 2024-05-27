<template>
    <div class="flex-col space-y-6 bg-slate-600 p-5 rounded-md">
      <h1 class="font-semibold text-2xl capitalize dark:text-white ">Discover pool spaces around you</h1>
  <div class=" dark:bg-slate-800 rounded-xl shadow-sm text-sm font-medium   dark:text-white w-full">
    <!-- Post heading -->
    <div class="flex gap-3 sm:p-4 p-2.5 text-sm font-medium">
      <a href="timeline.html">
        <img src="" alt="" class="w-9 h-9 rounded-full">
      </a>
      <div class="flex-1">
        <a href="timeline.html">
          <h4 class="text-black dark:text-white"> Monroe Parker </h4>
        </a>
        <div class="text-xs text-gray-500 dark:text-white/80"> 2 hours ago</div>
      </div>
      <div class="-mr-1">
        <button type="button" class="button-icon w-8 h-8" aria-haspopup="true" aria-expanded="false">
          <ion-icon class="text-xl md hydrated " name="ellipsis-horizontal" role="img" aria-label="ellipsis horizontal">...</ion-icon>
        </button>
      
      </div>
    </div>

    <!-- Post image -->
    <a href="#preview_modal" >
        <div class="sm:rounded-lg w-full h-full object-cover p-4">
          <GoogleMap/>
      </div>
    </a>


    <!-- Buttons at far ends -->
    <div class="flex justify-between p-4">
      <button class="btn-primary"></button>
      <button class="btn-secondary">More..</button>
    </div>
  </div>
  <div class=" dark:bg-slate-800 rounded-xl shadow-sm text-sm font-medium   dark:text-white w-full">
    <!-- Post heading -->
    <div class="flex gap-3 sm:p-4 p-2.5 text-sm font-medium">
      <a href="timeline.html">
        <img src="" alt="" class="w-9 h-9 rounded-full">
      </a>
      <div class="flex-1">
        <a href="timeline.html">
          <h4 class="text-black dark:text-white"> Monroe Parker </h4>
        </a>
        <div class="text-xs text-gray-500 dark:text-white/80"> 2 hours ago</div>
      </div>
      <div class="-mr-1">
        <button type="button" class="button-icon w-8 h-8" aria-haspopup="true" aria-expanded="false">
          <ion-icon class="text-xl md hydrated " name="ellipsis-horizontal" role="img" aria-label="ellipsis horizontal">...</ion-icon>
        </button>
      
      </div>
    </div>

    <!-- Post image -->
    <a href="#preview_modal" >
        <div class="sm:rounded-lg w-full h-full object-cover p-4">
          <GoogleMap/>
      </div>
    </a>


    <!-- Buttons at far ends -->
    <div class="flex justify-between p-4">
      <button class="btn-primary"></button>
      <button class="btn-secondary">More..</button>
    </div>
  </div>
  <div class=" dark:bg-slate-800 rounded-xl shadow-sm text-sm font-medium   dark:text-white w-full">
    <!-- Post heading -->
    <div class="flex gap-3 sm:p-4 p-2.5 text-sm font-medium">
      <a href="timeline.html">
        <img src="" alt="" class="w-9 h-9 rounded-full">
      </a>
      <div class="flex-1">
        <a href="timeline.html">
          <h4 class="text-black dark:text-white"> Monroe Parker </h4>
        </a>
        <div class="text-xs text-gray-500 dark:text-white/80"> 2 hours ago</div>
      </div>
      <div class="-mr-1">
        <button type="button" class="button-icon w-8 h-8" aria-haspopup="true" aria-expanded="false">
          <ion-icon class="text-xl md hydrated " name="ellipsis-horizontal" role="img" aria-label="ellipsis horizontal">...</ion-icon>
        </button>
      
      </div>
    </div>

    <!-- Post image -->
    <a href="#preview_modal" >
        <div class="sm:rounded-lg w-full h-full object-cover p-4">
          <GoogleMap/>
      </div>
    </a>


    <!-- Buttons at far ends -->
    <div class="flex justify-between p-4">
      <button class="btn-primary"></button>
      <button class="btn-secondary">More..</button>
    </div>
  </div>  
</div>
</template>


<script setup>
import GoogleMap from "@/components/dahsboard/show_map.vue"

</script>

<style scoped>
/* Tailwind CSS classes are used directly, so no additional styling is needed here */
</style>
