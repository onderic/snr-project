<template>
  <div class="flex flex-row">
    <div class="lg:flex gap-16">
      <div class="flex-1 max-w-[1280px] mx-auto">
        <h3 class="dark:text-white font-bold capitalize mb-4 text-xl">
          COMPETE. SCORE. WIN. REPEAT.
        </h3>
        <div class="flex mb-6">
          <div class="card flex justify-center gap-4">
            <Button label="Tournaments" severity="info"  icon="pi pi-home" @click="updateTournaments('Feed')" />
            <Button label="Discover" severity="info" icon="pi pi-map-marker" @click="updateTournaments('Discover')" />
            <div>
              <Toast position="bottom-right" group="br" />
              <ConfirmDialog group="positioned"></ConfirmDialog>
              <div>
                <Button @click="confirmPosition('right')" label="Create" severity="info" icon="pi pi-folder-plus"></Button>
              </div>
            </div>
          </div>
        </div>
        <div class="scrollable-container">
          <component :is="currentComponent" />
        </div>
      </div>
    </div>
    <div class="absolute right-32 mt-16 max-w-[1080px] mx-auto">
      <div class="lg:space-y-6 space-y-4 lg:pb-8 max-lg:grid sm:grid-cols-2 max-lg:gap-6">
        <LatestTournaments />
        <UpcomingTournaments />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import Create from '@/components/dahsboard/Create.vue';
import Discover from '@/components/dahsboard/dash_discover.vue';
import Feed from '@/components/dahsboard/dash_feed.vue';
import LatestTournaments from '@/components/dahsboard/LatestTournaments..vue';
import Tournaments from '@/components/dahsboard/dash_tournaments.vue';
import UpcomingTournaments from '@/components/dahsboard/UpcomingTournaments.vue';
import Button from 'primevue/button';
import { useConfirm } from "primevue/useconfirm";
import { useToast } from "primevue/usetoast";
import ConfirmDialog from 'primevue/confirmdialog';

const componentsMap = {
  Feed,
  Discover,
  Create,
};

const confirm = useConfirm();
const toast = useToast();
const router = useRouter();

const confirmPosition = (position) => {
    confirm.require({
        group: 'positioned',
        message: 'This section allows pool table owners to register the location of their pool area, making it easier for players to find. Are you sure you want to proceed?',
        header: 'Confirmation',
        icon: 'pi pi-info-circle',
        position: position,
        rejectProps: {
            label: 'Cancel',
            severity: 'info',
            text: true
        },
        acceptProps: {
            label: 'Save',
            text: true
        },
        accept: () => {
          toast.add({ severity: 'info', summary: 'Success Message', detail: 'Message Content', group: 'br', life: 3000 });
          router.push('/add-pool')
        },
        reject: () => {
            toast.add({ severity: 'error', summary: 'Rejected', detail: 'Process incomplete', group: 'br', life: 3000 });
        }
    });
};

const currentComponent = ref(Tournaments);

const updateTournaments = (componentName) => {
  currentComponent.value = componentsMap[componentName];
};
</script>

<style scoped>
.scrollable-container {
  max-height: 1000px;
  overflow-y: auto;
}
</style>
