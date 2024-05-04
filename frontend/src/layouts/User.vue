<template>
  <div>
    <!-- Show loader if loading is true -->
    <div v-if="loading" class="flex justify-center items-center h-screen">
      <div class="rounded-full h-20 w-20 bg-violet-800 animate-ping"></div>
    </div>
    <!-- Show layouts and router view if loading is false -->
    <div v-else>
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
          <main>
            <div class="mx-auto max-w-screen p-4 md:p-6 2xl:p-10 mt-20">
              <!-- <slot></slot> -->
              <router-view />
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
import Sidebar from '@/components/Sidebar/Sidebar.vue'
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
