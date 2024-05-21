<template>
  <aside
    class="fixed top-16 left-0 z-40 w-64 h-screen transition-transform -translate-x-full sm:translate-x-0"
    :class="{ '-translate-x-full': !showSidebar, 'translate-x-0': showSidebar }"
  >
    <div
      class="p-2 max-xl:bg-slate-700 dark:text-gray-400 shadow-sm 2xl:w-72 sm:w-64 w-[80%] h-[calc(100vh-64px)] relative z-30 max-lg:border-r dark:border-slate-700"
    >
      <div class="pr-4">
        <div id="side">
          <ul class="mt-6">
            <li>
              <a
                href="feed.html"
                class="flex items-center space-x-2 py-2 px-4 rounded-lg hover:bg-gray-100 dark:hover:bg-slate-600 font-bold text-sm dark:text-white"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="w-6 h-6"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M15 19l-7-7 7-7"
                  ></path>
                </svg>
                <span>Feed</span>
              </a>
            </li>
            <li>
              <a
                href="messages.html"
                class="flex items-center space-x-2 py-2 px-4 rounded-lg hover:bg-gray-100 dark:hover:bg-slate-600 font-bold text-sm dark:text-white"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="w-6 h-6"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M12 6v6m0 0v6m0-6h6m-6 0H6"
                  ></path>
                </svg>
                <span>Messages</span>
              </a>
            </li>
            <li>
              <a
                href="video.html"
                class="flex items-center space-x-2 py-2 px-4 rounded-lg hover:bg-gray-100 dark:hover:bg-slate-600 font-bold text-sm dark:text-white"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="w-6 h-6"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M6 2l8 5-8 5V2z"
                  ></path>
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                  ></path>
                </svg>
                <span>Video</span>
              </a>
            </li>
            <li class="active">
              <a
                href="event.html"
                class="flex items-center space-x-2 py-2 px-4 rounded-lg bg-blue-500 text-white dark:bg-blue-600 dark:text-white"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="w-6 h-6"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M9 5l7 7-7 7"
                  ></path>
                </svg>
                <span>Event</span>
              </a>
            </li>
            <li>
              <a
                href="pages.html"
                class="flex items-center space-x-2 py-2 px-4 rounded-lg hover:bg-gray-100 dark:hover:bg-slate-600 font-bold text-sm dark:text-white"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="w-6 h-6"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M3 6l5 5L3 16M21 6l-5 5 5 5"
                  ></path>
                </svg>
                <span>Pages</span>
              </a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </aside>
</template>

<script>
import { ref } from 'vue'

import { useRouter } from 'vue-router'


export default {
  props: {
    showSidebar: {
      type: Boolean,
      default: false
    }
  },
  setup() {
    const dropdownOpen = ref({
      dropdwon: false
    })

    const toggleDropdown = (id) => {
      dropdownOpen.value[id] = !dropdownOpen.value[id]
    }

    const router = useRouter()

   

    // const logout = () => {
    //   userStore.logout();
    //   router.push({ name: 'login' });
    //   toast.info('You have logged out');
    // }

    return {
      dropdownOpen,
      toggleDropdown
    }
  }
}
</script>
