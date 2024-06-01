<template>
  <div>
    <!-- Progress Bar at the very top -->
    <ProgressBar :loading="loadingWithDelay" />

    <div class="flex h-screen overflow-hidden">
      <!-- Sidebar -->
      <Sidebar />

      <!-- Content Area -->
      <div class="relative flex flex-1 flex-col overflow-y-auto overflow-x-hidden">
        <!-- Header -->
        <HeaderArea/>

        <!-- Main Content -->
        <main class="2xl:ml-[--w-side] xl:ml-[--w-side-sm] p-2.5 h-[calc(100vh-var(--m-top))] mt-[--m-top]">
          <div class="lg:flex 2xl:gap-16 gap-12 max-w-[1065px] mx-auto">
            <router-view />
          </div>
        </main>
      </div>
    </div>
  </div>
</template>

<script setup>

import Sidebar from '@/components/Sidebar/SideBar.vue'
import HeaderArea from '@/components/Header/HeaderArea.vue'
import ProgressBar from '@/components/ProgressBar.vue'
import { refMinDelay } from '@/composables/refMinDelay'
import { provideLoading } from '@/composables/loading'


const loading = provideLoading()
const loadingWithDelay = refMinDelay(loading, 3000)

</script>
