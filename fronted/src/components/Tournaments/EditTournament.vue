<template>
    <div>
        <button data-modal-target="crud-modal" data-modal-toggle="crud-modal" class="block text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800" type="button">
   Edit
    </button>
  
     <!-- Main modal -->
<div id="crud-modal" tabindex="-1" aria-hidden="true" class="hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full">
    <div class="relative p-4 w-full max-w-md max-h-full">
        <!-- Modal content -->
        <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
            <!-- Modal header -->
            <div class="flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600">
                <h3 class="text-lg font-semibold text-gray-900 dark:text-white">
                    Create New Product
                </h3>
                <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white" data-modal-toggle="crud-modal">
                    <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>
                    </svg>
                    <span class="sr-only">Close modal</span>
                </button>
            </div>
            <!-- Modal body -->
            <div>
              <div class="grid gap-4 mb-4 sm:grid-cols-2">
                <div>
                  <label for="edit_title" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Title</label>
                  <input type="text" name="edit_title" id="edit_title" v-model="editTitle" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500" placeholder="Event title" required>
                </div>
                <div>
                  <label for="edit_start_time" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Start Date</label>
                  <input type="datetime-local" name="edit_start_time" id="edit_start_time" v-model="editStartTime" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500" placeholder="Event start time" required>
                </div>
                <div>
                  <label for="edit_end_time" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">End Date</label>
                  <input type="datetime-local" name="edit_end_time" id="edit_end_time" v-model="editEndTime" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500" placeholder="Event end time" required>
                </div>
                <div>
                  <label for="edit_enrollment_fee" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Registration fee</label>
                  <input type="number" name="edit_enrollment_fee" id="edit_enrollment_fee" v-model="editEnrollmentFee" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500" placeholder="Event registration fee" required>
                </div>
                <div class="sm:col-span-2">
                  <label for="edit_description" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Description</label>
                  <textarea id="edit_description" v-model="editDescription" rows="4" class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500" placeholder="Write event description here"></textarea>                    
                </div>
              </div>
              <button @click="updateEvent" type="submit" class="btn">
                <v-icon v-if="loading.value" name="gi-spinning-blades" animation="spin" scale="1"/> 
                Update 
              </button>
            </div>
        </div>
    </div>
</div> 
    </div>
  </template>
  
  <script setup>
  import { ref, watch } from 'vue';
  import { useToast } from 'vue-toastify';
  import { useLoading } from '@/composables/loading';
  import axios from 'axios';
  import { onMounted} from 'vue';
  
  const toast = useToast();
  const loading = useLoading();
  
  const props = defineProps({
    selectedEvent: {
      type: Object,
      required: true
    }
  });
  
  const editTitle = ref('');
  const editDescription = ref('');
  const editStartTime = ref('');
  const editEndTime = ref('');
  const editEnrollmentFee = ref('');
  
  watch(props.selectedEvent, (newEvent) => {
    editTitle.value = newEvent.title || '';
    editDescription.value = newEvent.description || '';
    editStartTime.value = newEvent.start_time || '';
    editEndTime.value = newEvent.end_time || '';
    editEnrollmentFee.value = newEvent.enrollment_fee || '';
  });
  
  async function updateEvent() {
    try {
      loading.value = true;
      const updatedEvent = {
        title: editTitle.value,
        description: editDescription.value,
        start_time: editStartTime.value,
        end_time: editEndTime.value,
        enrollment_fee: editEnrollmentFee.value,
      };
      await axios.put(`/tournaments_update/${props.selectedEvent.id}/`, updatedEvent);
      toast.success('Event updated successfully');
      // Emit event to parent to refresh the events list
      emit('event-updated');
    } catch (error) {
      console.error('Error updating event:', error.message);
      toast.error('Failed to update event');
    } finally {
      loading.value = false;
    }
  }

  onMounted(() => {
    initFlowbite();
});
  </script>