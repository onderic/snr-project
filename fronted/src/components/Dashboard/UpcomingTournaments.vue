<template>
         <div class="w-full max-w-md p-4 bg-white border border-gray-200 rounded-lg shadow sm:p-8 dark:bg-gray-800 dark:border-gray-700">
              <div class="flex items-center justify-between mb-4">
                  <h5 class="text-xl font-bold leading-none text-gray-900 dark:text-white">Upcomming Tournaments</h5>
                  <!-- <a href="#" class="text-sm font-medium text-blue-600 hover:underline dark:text-blue-500">
                      View all
                  </a> -->
            </div>
            <div class="flow-root">
                  <ul role="list" class="divide-y divide-gray-200 dark:divide-gray-700">
                      <li class="py-3 sm:py-4">
                          <div class="flex items-center">
                              <div class="flex-shrink-0">
                                  <img class="w-8 h-8 rounded-full" src="@/assets/ball.jpeg" alt="Neil image">
                              </div>
                              <div class="flex-1 min-w-0 ms-4">
                                  <p class="text-sm font-medium text-gray-900 truncate dark:text-white">
                                      Neil Sims
                                  </p>
                                  <p class="text-sm text-gray-500 truncate dark:text-gray-400">
                                      neil@example.com
                                  </p>
                              </div>
                              <div class="inline-flex items-center text-base font-semibold text-gray-900 dark:text-white">
                                  Winner
                              </div>
                          </div>
                      </li>
                      <li class="py-3 sm:py-4">
                          <div class="flex items-center ">
                              <div class="flex-shrink-0">
                                  <img class="w-8 h-8 rounded-full" src="@/assets/ball.jpeg" alt="Bonnie image">
                              </div>
                              <div class="flex-1 min-w-0 ms-4">
                                  <p class="text-sm font-medium text-gray-900 truncate dark:text-white">
                                      Bonnie Green
                                  </p>
                                  <p class="text-sm text-gray-500 truncate dark:text-gray-400">
                                      bonnie@example.com
                                  </p>
                              </div>
                              <div class="inline-flex items-center text-base font-semibold text-gray-900 dark:text-white">
                                  Participant
                              </div>
                          </div>
                      </li>
                      <!-- Add more participants here -->
                  </ul>
            </div>
          </div>
</template>

<script>
export default {

}
</script>

<style>

</style>