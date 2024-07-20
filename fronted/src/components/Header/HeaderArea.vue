<template >
  <div class="mb-10">
    <div
      class="z-[100] h-[--m-top] fixed top-0 left-0 w-full flex items-center bg-white dark:bg-slate-800 sky-50 backdrop-blur-xl border-b border-slate-200 dark:bg-dark2 dark:border-slate-800"
    >
      <div class="flex items-center w-full xl:px-6 px-2 max-lg:gap-10 p-2">
        <div class="2xl:w-[--w-side] lg:w-[--w-side-sm]">
          <!-- left -->
          <div class="flex items-center gap-1">
            <!-- icon menu -->
            <button
              type="button"
              class="inline-flex items-center p-2 mt-2 ms-3 text-sm text-gray-500 rounded-lg sm:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
            >
            <v-icon name="co-home" />
            </button>
            <div id="logo">
              <a href="feed.html">
                <img src="" alt="logohere" class="w-28 md:block hidden dark:!hidden" />
                <img src="" alt="logohere" class="dark:md:block hidden" />
                <img src="" class="hidden max-md:block w-20 dark:!hidden" alt="logohere" />
                <img src="" class="hidden dark:max-md:block w-20" alt="logohere" />
              </a>
            </div>
          </div>
        </div>
        <div class="flex-1 relative">
          <div class="max-w-[1220px] mx-auto flex items-center py-6">
            <!-- search -->
            <!-- <SearchBar /> -->

            <!-- <div
              id="search--box"
              class="xl:w-[680px] sm:w-96 sm:relative rounded-xl overflow-hidden z-20 bg-gray-100 dark:bg-slate-900 max-md:hidden w-screen left-0 max-sm:fixed max-sm:top-2 dark:!bg-white/5"
            >
              <ion-icon name="search" class="absolute left-4 top-1/2 -translate-y-1/2"></ion-icon>
              <input
                type="text"
                placeholder="Search Friends, videos .."
                class="w-full !pl-10 !font-normal !bg-transparent h-12 !text-sm"
              />
            </div> -->

            <!-- header icons -->
            <div
              class="flex items-center sm:gap-4 gap-2 absolute right-5 top-1/2 -translate-y-1/2 text-black"
            >
              <!-- theme -->
              <DarkModeSwitcher/>
              <!-- <button
                type="button"
                class="sm:p-2 p-1 rounded-full relative sm:bg-gray-100 dark:bg-slate-900 dark:text-white"
              >
              <v-icon name="md-darkmode" scale="1.5" />
              <v-icon name="bi-sun-fill" scale="1.5" />
              
              </button> -->

              <!-- notification -->
              <DropdownNotification/>

              <!-- profile -->
              <DropdownUser/>
             
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>

import DarkModeSwitcher from '@/components/Header/DarkModeSwitcher.vue'
// import DropdownMessage from '@/components/Header/DropdownMessage.vue'
import DropdownNotification from '@/components/Header/DropdownNotification.vue'
import DropdownUser from '@/components/Header/DropdownUser.vue'
import SearchBar from '@/components/Header/SearchBar.vue'

import { onMounted } from 'vue'
import { initFlowbite } from 'flowbite'

onMounted(() => {
    initFlowbite();
})

</script>

<style lang=""></style>
