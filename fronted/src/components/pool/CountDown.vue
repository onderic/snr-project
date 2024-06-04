<template>
   <div>
        <div class="flex gap-3 text-4xl font-semibold text-primary dark:text-white max-lg:justify-center uk-countdown">
            <div class="bg-primary-soft/40 flex flex-col items-center justify-center rounded-lg w-16 h-16 lg:border-4 border-white md:shadow dark:border-slate-700">
                <span class="uk-countdown-days"><span>{{ days }}</span></span> 
                <span class="inline-block text-xs">Days</span>
            </div>
            <div class="bg-primary-soft/40 flex flex-col items-center justify-center rounded-lg w-16 h-16 lg:border-4 border-white md:shadow dark:border-slate-700">
                <div class="uk-countdown-hours"><span>{{ hours }}</span></div> 
                <span class="inline-block text-xs">Hours</span>
            </div>
            <div class="bg-primary-soft/40 flex flex-col items-center justify-center rounded-lg w-16 h-16 lg:border-4 border-white md:shadow dark:border-slate-700">
                <div class="uk-countdown-minutes"><span>{{ minutes }}</span></div> 
                <span class="inline-block text-xs">min </span>
            </div>
            <div class="bg-primary-soft/40 flex flex-col items-center justify-center rounded-lg w-16 h-16 lg:border-4 border-white md:shadow dark:border-slate-700">
                <div class="uk-countdown-seconds"><span>{{ seconds }}</span></div> 
                <span class="inline-block text-xs">sec </span>
            </div>
        </div>
    </div>

</template>

<script setup>
import { ref, watchEffect } from 'vue';

const eventStartTime = '2024-06-10T09:00:00'; 
const eventEndTime = '2024-06-10T18:00:00'; 

const days = ref('');
const hours = ref('');
const minutes = ref('');
const seconds = ref('');

function calculateRemainingTime() {
    const startTime = new Date(eventStartTime).getTime();
    const endTime = new Date(eventEndTime).getTime();
    const now = new Date().getTime();

    let timeRemaining;
    if (now < startTime) {
        timeRemaining = startTime - now;
    } else if (now < endTime) {
        timeRemaining = endTime - now;
    } else {
        timeRemaining = 0;
    }

    days.value = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
    hours.value = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    minutes.value = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
    seconds.value = Math.floor((timeRemaining % (1000 * 60)) / 1000);
}

calculateRemainingTime();

// Update countdown every second
const interval = setInterval(calculateRemainingTime, 1000);

// Clean up interval when component is unmounted
watchEffect(() => {
    return () => clearInterval(interval);
});
</script>

<style scoped>
/* Add any custom styles here */
</style>
<style>

</style>