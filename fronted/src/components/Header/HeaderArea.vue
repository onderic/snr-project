<template lang="">
  <div>
    <div
      class="z-[100] h-[--m-top] fixed top-0 left-0 w-full flex items-center bg-white dark:bg-slate-800 sky-50 backdrop-blur-xl border-b border-slate-200 dark:bg-dark2 dark:border-slate-800"
    >
      <div class="flex items-center w-full xl:px-6 px-2 max-lg:gap-10 p-2">
        <div class="2xl:w-[--w-side] lg:w-[--w-side-sm]">
          <!-- left -->
          <div class="flex items-center gap-1">
            <!-- icon menu -->
            <button
              @click="toggleSidebar"
              type="button"
              class="inline-flex items-center p-2 mt-2 ms-3 text-sm text-gray-500 rounded-lg sm:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
            >
              <svg
                class="w-6 h-6"
                aria-hidden="true"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  clip-rule="evenodd"
                  fill-rule="evenodd"
                  d="M2 4.75A.75.75 0 012.75 4h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 4.75zm0 10.5a.75.75 0 01.75-.75h7.5a.75.75 0 010 1.5h-7.5a.75.75 0 01-.75-.75zM2 10a.75.75 0 01.75-.75h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 10z"
                ></path>
              </svg>
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
          <div class="max-w-[1220px] mx-auto flex items-center">
            <!-- search -->
            <div
              id="search--box"
              class="xl:w-[680px] sm:w-96 sm:relative rounded-xl overflow-hidden z-20 bg-gray-100 dark:bg-slate-900 max-md:hidden w-screen left-0 max-sm:fixed max-sm:top-2 dark:!bg-white/5"
            >
              <ion-icon name="search" class="absolute left-4 top-1/2 -translate-y-1/2"></ion-icon>
              <input
                type="text"
                placeholder="Search Friends, videos .."
                class="w-full !pl-10 !font-normal !bg-transparent h-12 !text-sm"
              />
            </div>

            <!-- header icons -->
            <div
              class="flex items-center sm:gap-4 gap-2 absolute right-5 top-1/2 -translate-y-1/2 text-black"
            >
              <!-- create -->
              <button
                type="button"
                class="sm:p-2 p-1 rounded-full relative sm:bg-gray-100 dark:bg-slate-900 dark:text-white"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
                  class="w-5 h-5 max-sm:hidden"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M12 4.5v15m7.5-7.5h-15"
                  ></path>
                </svg>
                <ion-icon name="add-circle-outline" class="sm:hidden text-2xl"></ion-icon>
              </button>

              <!-- notification -->
              <button
                type="button"
                class="sm:p-2 p-1 rounded-full relative sm:bg-gray-100 dark:bg-slate-900 dark:text-white"
                uk-tooltip="title: Notification; pos: bottom; offset:6"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 24 24"
                  fill="currentColor"
                  class="w-6 h-6 max-sm:hidden"
                >
                  <path
                    d="M5.85 3.5a.75.75 0 00-1.117-1 9.719 9.719 0 00-2.348 4.876.75.75 0 001.479.248A8.219 8.219 0 015.85 3.5zM19.267 2.5a.75.75 0 10-1.118 1 8.22 8.22 0 011.987 4.124.75.75 0 001.48-.248A9.72 9.72 0 0019.266 2.5z"
                  />
                  <path
                    fill-rule="evenodd"
                    d="M12 2.25A6.75 6.75 0 005.25 9v.75a8.217 8.217 0 01-2.119 5.52.75.75 0 00.298 1.206c1.544.57 3.16.99 4.831 1.243a3.75 3.75 0 107.48 0 24.583 24.583 0 004.83-1.244.75.75 0 00.298-1.205 8.217 8.217 0 01-2.118-5.52V9A6.75 6.75 0 0012 2.25zM9.75 18c0-.034 0-.067.002-.1a25.05 25.05 0 004.496 0l.002.1a2.25 2.25 0 11-4.5 0z"
                    clip-rule="evenodd"
                  />
                </svg>
                <div
                  class="absolute top-0 right-0 -m-1 bg-red-600 text-white text-xs px-1 rounded-full"
                >
                  6
                </div>
                <ion-icon name="notifications-outline" class="sm:hidden text-2xl"></ion-icon>
              </button>

              <!-- messages -->
              <button
                type="button"
                class="sm:p-2 p-1 rounded-full relative sm:bg-gray-100 dark:bg-slate-900 dark:text-white"
                uk-tooltip="title: Messages; pos: bottom; offset:6"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 24 24"
                  fill="currentColor"
                  class="w-6 h-6 max-sm:hidden"
                >
                  <path
                    fill-rule="evenodd"
                    d="M4.848 2.771A49.144 49.144 0 0112 2.25c2.43 0 4.817.178 7.152.52 1.978.292 3.348 2.024 3.348 3.97v6.02c0 1.946-1.37 3.678-3.348 3.97a48.901 48.901 0 01-3.476.383.39.39 0 00-.297.17l-2.755 4.133a.75.75 0 01-1.248 0l-2.755-4.133a.39.39 0 00-.297-.17 48.9 48.9 0 01-3.476-.384c-1.978-.29-3.348-2.024-3.348-3.97V6.741c0-1.946 1.37-3.68 3.348-3.97zM6.75 8.25a.75.75 0 01.75-.75h9a.75.75 0 010 1.5h-9a.75.75 0 01-.75-.75zm.75 2.25a.75.75 0 000 1.5H12a.75.75 0 000-1.5H7.5z"
                    clip-rule="evenodd"
                  ></path>
                </svg>
                <ion-icon name="chatbox-ellipses-outline" class="sm:hidden text-2xl"></ion-icon>
              </button>

              <!-- profile -->
              <div
                class="rounded-full relative bg-gray-100 dark:bg-slate-900 cursor-pointer shrink-0"
              >
                <img src="" alt="" class="sm:w-9 sm:h-9 w-7 h-7 rounded-full shadow shrink-0" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>

import DarkModeSwitcher from './DarkModeSwitcher.vue'
import DropdownMessage from './DropdownMessage.vue'
import DropdownNotification from './DropdownNotification.vue'
import DropdownUser from './DropdownUser.vue'

export default {
  components: {
    DarkModeSwitcher,
    DropdownMessage,
    DropdownNotification,
    DropdownUser
  },
  // setup() {
  //   const { emit } = getCurrentInstance()

  //   const toggleSidebar = () => {
  //     emit('toggle-sidebar')
  //   }
  //   return {
  //     toggleSidebar
  //   }
  // }
}
</script>
<style lang=""></style>
