import { ref, onMounted, onUnmounted } from 'vue';

const usePolling = (method, timeInterval = 10000) => {
  const interval = ref(null);
  const isPolling = ref(false);

  const clear = () => {
    if (interval.value !== null) {
      clearInterval(interval.value);
      interval.value = null;
      isPolling.value = false;
    }
  };

  const fetchData = () => {
    method();
    if (isPolling.value) {
      // Start interval
      interval.value = setInterval(() => {
        method();
      }, timeInterval);
    }
  };

  const start = () => {
    // Clear any existing polling calls
    clear();
    // Set polling flag to true
    isPolling.value = true;
    // Fetch data
    fetchData();
  };

  onMounted(() => {
    if (isPolling.value) {
      fetchData();
    }
  });

  onUnmounted(() => {
    clear();
  });

  return {
    start,
    clear,
  };
};

export default usePolling;
