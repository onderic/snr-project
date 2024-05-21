<template>
  <main class="max-w-[1165px] mx-auto lg:mr-44">
    <div class="lg:flex gap-16">
      <div class="flex-1 max-w-[1080px] mx-auto">
        <h3 class="dark:text-white font-bold capitalize mb-4 text-xl">
          COMPETE. SCORE. WIN. REPEAT.
        </h3>
        <div class="flex mb-6">
          <div class="card flex justify-center gap-4">
            <Button label="Home" severity="info" icon="pi pi-home" @click="updateTournaments('Feed')" />
            <Button label="Location" severity="info" icon="pi pi-map-marker" @click="updateTournaments('Discover')" />
            <Button label="Create" severity="info" icon="pi pi-folder-plus" @click="updateTournaments('Create')" />
          </div>
        </div>
        <!-- Dynamically show component info based on the button calls. Tournaments should be the default component -->
        <component :is="currentComponent" />
      </div>
      <div class="2xl:w-[380px] lg:w-[430px] w-full">
        <div
          class="lg:space-y-6 space-y-4 lg:pb-8 max-lg:grid sm:grid-cols-2 max-lg:gap-6"
          uk-sticky="media: 1024; end: #js-oversized; offset: 80"
        >
          <LatestTournaments />
          <UpcomingTournaments />
        </div>
      </div>
    </div>
  </main>
</template>

<script setup>
  import Create from '@/components/dahsboard/Create.vue';
  import Discover from '@/components/dahsboard/Discover.vue';
  import Feed from '@/components/dahsboard/Feed.vue';
  import LatestTournaments from '@/components/dahsboard/LatestTournaments..vue';
  import Tournaments from '@/components/dahsboard/Tournaments.vue';
  import UpcomingTournaments from '@/components/dahsboard/UpcomingTournaments.vue';
  import { ref } from 'vue';
  import Button from 'primevue/button';

const componentsMap = {
  Feed,
  Discover,
  Create,
};

const currentComponent = ref(Tournaments);

const updateTournaments = (componentName) => {
  currentComponent.value = componentsMap[componentName];
};
</script>
