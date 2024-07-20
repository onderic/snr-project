<template>
  <div class="flex flex-col lg:flex-row gap-12 2xl:gap-16 max-w-[1065px] mx-auto lg:mt-16 mt-4">
    <div class="w-full lg:w-2/3">
      <!-- feed story -->
      <div class="flex-1 xl:space-y-6 space-y-3">
        <h3 class="dark:text-white font-bold capitalize mb-4 text-xl">
          COMPETE. SCORE. WIN. REPEAT.
        </h3>
        <div class="flex mb-6 flex-wrap lg:gap-8 gap-1 justify-center lg:justify-start">
          <button class="text-white bg-gradient-to-br from-purple-600 to-blue-500 hover:bg-gradient-to-bl focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800 font-medium rounded-lg text-sm lg:px-5 px-2 py-2.5 text-center me-2 mb-2" @click="updateComponent('Discover')">
            <v-icon name="co-home" /> Discover
          </button>
          <button class="text-white bg-gradient-to-br from-purple-600 to-blue-500 hover:bg-gradient-to-bl focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800 font-medium rounded-lg text-sm lg:px-5 px-2 py-2.5 text-center me-2 mb-2" @click="updateComponent('Tournaments')">
            <v-icon name="io-locate-outline" animation="spin" scale="" />
            Tournaments
          </button>
          <router-link to="/add-pool/location">
            <button class="text-white bg-gradient-to-br from-purple-600 to-blue-500 hover:bg-gradient-to-bl focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800 font-medium rounded-lg text-sm lg:px-5 px-2 py-2.5 text-center me-2 mb-2 p-2">
              <v-icon name="io-create-outline" />
              Create
            </button>
          </router-link>
        </div>
        <div class="scrollable-container">
          <component :is="currentComponent" />
        </div>
      </div>
    </div>
    <div class="w-full lg:w-1/3 lg:ml-20 mt-10 lg:mt-28">
      <div class="space-y-4 lg:space-y-6">
        <LatestTournaments />
        <UpcomingTournaments />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import Create from '@/components/Dashboard/Create.vue';
import Discover from '@/components/Dashboard/Discover.vue';
import LatestTournaments from '@/components/Dashboard/LatestTournaments.vue';
import Tournaments from '@/components/Dashboard/Tournaments.vue';
import UpcomingTournaments from '@/components/Dashboard/UpcomingTournaments.vue';

const componentsMap = {
  Discover,
  Create,
  Tournaments
};

const currentComponent = ref('Discover');

const updateComponent = (component) => {
  currentComponent.value = componentsMap[component];
};

// Reset currentComponent on route enter
const route = useRoute();
onMounted(() => {
  if (route.name === 'dashboard') {
    currentComponent.value = componentsMap['Discover'];
  }
});
</script>

<style scoped>
.scrollable-container {
  max-height: 1000px;
  overflow-y: auto;
}
</style>
