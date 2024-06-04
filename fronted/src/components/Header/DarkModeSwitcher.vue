<template>
  <div>
    <button
      @click="toggleDarkMode"
      class="sm:p-2 p-1 rounded-full relative sm:bg-gray-100 dark:bg-slate-900 dark:text-white"
    >
      <v-icon
        v-if="!isDark"
        name="md-darkmode"
        scale="1.5"
      />
      <v-icon
        v-else
        name="bi-sun-fill"
        scale="1.5"
      />
      <span class="sr-only">Switch to light / dark version</span>
    </button>
  </div>
</template>

<script setup>
import { useDark, useToggle } from '@vueuse/core'

const isDark = useDark()
const toggleDark = useToggle(isDark)

const toggleDarkMode = () => {
  toggleDark()
}
</script>

<style scoped>
/* Add any custom styles here if needed */
</style>
