// usePolling.js
import { ref, onUnmounted } from 'vue';

export default function usePolling(callback, interval, onLoadingChange) {
  const isPolling = ref(false);
  const isLoading = ref(false);
  let timerId = null;

  const start = () => {
    if (isPolling.value) return;
    isPolling.value = true;
    isLoading.value = true;
    onLoadingChange(isLoading.value);
    timerId = setInterval(() => {
      if (isPolling.value) callback();
    }, interval);
  };

  const stop = () => {
    if (!isPolling.value) return;
    isPolling.value = false;
    isLoading.value = false;
    onLoadingChange(isLoading.value);
    if (timerId) {
      clearInterval(timerId);
      timerId = null;
    }
  };

  onUnmounted(() => {
    stop();
  });

  return { start, stop, isLoading };
}
