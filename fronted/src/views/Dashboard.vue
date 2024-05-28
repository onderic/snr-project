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
            <button  class="btn" @click="updateTournaments('Feed')" >
              <v-icon name="co-home" /> Tournaments
            </button>
            <button class="btn" @click="updateTournaments('Discover')" >
               <v-icon name="io-locate-outline" animation="spin"  scale=""/> 
                Discover 
              </button>
         
            <div>
              <Toast position="bottom-right" group="br" />
              <ConfirmDialog group="positioned"></ConfirmDialog>
              <div >

                <router-link  to="/add-pool/location">
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
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import Create from '@/components/dahsboard/Create.vue';
import Discover from '@/components/dahsboard/dash_discover.vue';
import Feed from '@/components/dahsboard/dash_feed.vue';
import LatestTournaments from '@/components/dahsboard/LatestTournaments..vue';
import Tournaments from '@/components/dahsboard/dash_tournaments.vue';
import UpcomingTournaments from '@/components/dahsboard/UpcomingTournaments.vue';

const componentsMap = {
  Feed,
  Discover,
  Create,
};



const toastId = ref('');
const notify = () => toastId.value = toast('Hello', {
  autoClose: false,
  position: toast.POSITION.BOTTOM_CENTER,
});
const update = () => toast.update(toastId.value, {
  type: toast.TYPE.INFO,
  autoClose: 5000,
});


const router = useRouter();

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
