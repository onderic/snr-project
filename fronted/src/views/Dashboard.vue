<template>
  <div class="max-w-[680px] mx-auto">
    <!-- feed story -->
    <div class="md:max-w-[580px] mx-auto flex-1 xl:space-y-6 space-y-3 mt-28">
      <div class="flex flex-row">
        <div class="lg:flex gap-16">
          <div class="flex-1 max-w-[1280px] mx-auto">
            <h3 class="dark:text-white font-bold capitalize mb-4 text-xl">
              COMPETE. SCORE. WIN. REPEAT.
            </h3>
            <div class="flex mb-6">
              <div class="card flex justify-center gap-4">
                <button class="btn" @click="updateComponent('Discover')">
                  <v-icon name="co-home" /> Discover
                </button>
                <button class="btn" @click="updateComponent('Tournaments')">
                  <v-icon name="io-locate-outline" animation="spin" scale="" />
                  Tournaments
                </button>
                <div>
                  <Toast position="bottom-right" group="br" />
                  <ConfirmDialog group="positioned"></ConfirmDialog>
                  <div>
                    <router-link to="/add-pool/location">
                      <button class="btn p-2">
                        <v-icon name="io-create-outline" />
                        Create
                      </button>
                    </router-link>
                  </div>
                </div>
              </div>
            </div>
            <div class="scrollable-container">
              <component :is="currentComponent" />
            </div>
          </div>
        </div>
        <div class="absolute right-32 mt-16 max-w-[1080px] mx-auto hidden lg:block">
          <div class="lg:space-y-6 space-y-4 lg:pb-8 max-lg:grid sm:grid-cols-2 max-lg:gap-6">
            <LatestTournaments />
            <UpcomingTournaments />
          </div>
        </div>
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
