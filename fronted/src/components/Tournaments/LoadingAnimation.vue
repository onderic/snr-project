<template>
  <div class="fixed inset-0 flex items-center justify-center bg-gray-800 dark:bg-gray-900 bg-opacity-500 dark:bg-opacity-75">
    <div class="absolute inset-0 bg-white dark:bg-gray-800 bg-opacity-75 dark:bg-opacity-75 flex items-center justify-center shadow-2xl">
      <div class="flex flex-col items-center justify-center w-full h-full px-4 py-8 bg-gray-300 dark:bg-gray-900">
        <div class="flex items-center justify-center">
          <p class="text-dark dark:text-gray-200 text-lg mb-28 font-semibold font-serif">
            {{ message }}
          </p>
        </div>
        <div class="relative mb-4">
          <span class="loader"></span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  message: {
    type: String,
    default: 'Loading, please wait...'
  }
});
</script>

<style scoped>
.loader {
  width: 48px;
  height: 48px;
  position: relative;
}
.loader::before , .loader::after {
  content: '';
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  width: 48em;
  height: 48em;
  background-image:
    radial-gradient(circle 10px, #FFF 100%, transparent 0),
    radial-gradient(circle 10px, #FFF 100%, transparent 0),
    radial-gradient(circle 10px, #FFF 100%, transparent 0),
    radial-gradient(circle 10px, #FFF 100%, transparent 0),
    radial-gradient(circle 10px, #FFF 100%, transparent 0),
    radial-gradient(circle 10px, #FFF 100%, transparent 0),
    radial-gradient(circle 10px, #FFF 100%, transparent 0),
    radial-gradient(circle 10px, #FFF 100%, transparent 0);
  background-position: 0em -18em, 0em 18em, 18em 0em, -18em 0em,
                       13em -13em, -13em -13em, 13em 13em, -13em 13em;
  background-repeat: no-repeat;
  font-size: 0.5px;
  border-radius: 50%;
  animation: blast 1s ease-in infinite;
}
.loader::after {
  font-size: 1px;
  background: #fff;
  animation: bounce 1s ease-in infinite;
}

@keyframes bounce {
  0%, 100% { font-size: 0.75px }
  50% { font-size: 1.5px }
}
@keyframes blast {
  0%, 40% {
    font-size: 0.5px;
  }
  70% {
    opacity: 1;
    font-size: 4px;
  }
  100% {
    font-size: 6px;
    opacity: 0;
  }
}
</style>
