<template>
  <div>
   

    <!-- Show loader if loading is true -->
    <div v-if="loading" class="flex justify-center items-center h-screen">
      
      <div class="rounded-full h-20 w-20 bg-violet-800 animate-ping"></div>
    </div>
    <!-- Show layouts and router view if loading is false -->
    <div v-else>
      <div class="card">
      
    </div>
      <!-- ===== Page Wrapper Start ===== -->
      <div class="flex h-screen overflow-hidden">
        <!-- ===== Sidebar Start ===== -->
        <Sidebar :show-sidebar="showSidebar" />
        <!-- ===== Sidebar End ===== -->

        <!-- ===== Content Area Start ===== -->
        <div class="relative flex flex-1 flex-col overflow-y-auto overflow-x-hidden">
          <!-- ===== Header Start ===== -->
          <HeaderArea @toggle-sidebar="toggleSidebar" />
          <!-- ===== Header End ===== -->

          <!-- ===== Main Content Start ===== -->
              <!-- <slot></slot> -->
              <main class="2xl:ml-[--w-side]  xl:ml-[--w-side-sm] p-2.5 h-[calc(100vh-var(--m-top))] mt-[--m-top]">
                 <!-- timeline -->
                <div class="lg:flex 2xl:gap-16 gap-12 max-w-[1065px] mx-auto"  id="js-oversized">
                  <div class="max-w-[680px] mx-auto">


                  <!-- feed story -->
                  <div class="md:max-w-[580px] mx-auto flex-1 xl:space-y-6 space-y-3 mt-28"></div>
                            
                    <router-view /> 
                  
                    </div>
                    </div>
                </main>
          <!-- ===== Main Content End ===== -->
          <!-- <footer-user /> -->
        </div>
      </div>
      <!-- ===== Page Wrapper End ===== -->
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'

import Sidebar from '@/components/Sidebar/side_bar.vue'
import HeaderArea from '@/components/Header/HeaderArea.vue'
import { useRouter } from 'vue-router'

export default {
  components: {
    HeaderArea,
    Sidebar
  },
  setup() {
    const loading = ref(false)
    const showSidebar = ref(false)

    const toggleSidebar = () => {
      showSidebar.value = !showSidebar.value
    }

    const router = useRouter()
    router.beforeEach((to, from, next) => {
      loading.value = true // Set loading to true before navigating
      if (window.innerWidth < 1024) {
        // Close the sidebar if the window width is smaller than 1024
        showSidebar.value = false
      }
      next()
    })

    router.afterEach((to, from) => {
      if (to.path === from.path) {
        // Close the sidebar if the user clicks on the current route
        showSidebar.value = false
      }
      loading.value = false // Set loading to false after navigation is complete
    })

    return {
      loading,
      showSidebar,
      toggleSidebar
    }
  }
}
</script>
