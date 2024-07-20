<template>
  <div class="2xl:max-w-[1220px] max-w-[1065px] mx-auto lg:mt-20 mt-4">
      <div class="p-4 bg-white block sm:flex items-center justify-between border-b border-gray-200 mt-20 dark:bg-gray-800 dark:border-gray-700">
        <div class="w-full mb-1">
          <div class="mb-4">
            <h1 class="text-xl font-semibold text-gray-900 sm:text-2xl dark:text-white">My Pool Spaces</h1>
          </div>
        </div>
      </div>
      <div class="flex flex-col">
        <div class="overflow-x-auto">
          <div class="inline-block min-w-full align-middle">
            <div class="overflow-hidden shadow">
              <table class="min-w-full divide-y divide-gray-200 table-fixed dark:divide-gray-600">
                <thead class="bg-gray-100 dark:bg-gray-700">
                  <tr>
                    <th scope="col" class="p-4 text-xs font-medium text-left text-gray-500 uppercase dark:text-gray-400">Title</th>
                    <th scope="col" class="p-4 text-xs font-medium text-left text-gray-500 uppercase dark:text-gray-400">Email</th>
                    <th scope="col" class="p-4 text-xs font-medium text-left text-gray-500 uppercase dark:text-gray-400">Number</th>
                    <th scope="col" class="p-4 text-xs font-medium text-left text-gray-500 uppercase dark:text-gray-400">Address</th>
                    <th scope="col" class="p-4 text-xs font-medium text-left text-gray-500 uppercase dark:text-gray-400">Status</th>
                    <th scope="col" class="p-4 text-xs font-medium text-left text-gray-500 uppercase dark:text-gray-400">Actions</th>
                  </tr>
                </thead>
                <tbody class="bg-white divide-y divide-gray-200 dark:bg-gray-800 dark:divide-gray-700">
                  <tr v-for="poolSpace in poolSpaces" :key="poolSpace.id" class="hover:bg-gray-100 dark:hover:bg-gray-700">
                    <td class="p-4 text-base font-medium text-gray-900 whitespace-nowrap dark:text-white">{{ poolSpace.title }}</td>
                    <td class="p-4 text-base font-medium text-gray-900 whitespace-nowrap dark:text-white">{{ poolSpace.email }}</td>
                    <td class="p-4 text-base font-medium text-gray-900 whitespace-nowrap dark:text-white">{{ poolSpace.number }}</td>
                    <td class="p-4 text-base font-medium text-gray-900 dark:text-white break-words">{{ poolSpace.address }}</td>
                    <td class="p-4 text-base font-medium text-gray-900 whitespace-nowrap dark:text-white">
                      <div class="flex items-center">
                        <div :class="{'h-2.5 w-2.5 rounded-full mr-2': true, 'bg-green-400': poolSpace.status === 'active', 'bg-red-400': poolSpace.status === 'inactive'}"></div> {{ poolSpace.status }}
                      </div>
                    </td>
                    <td class="p-4 space-x-2 whitespace-nowrap">
                      <button @click="openEditModal(poolSpace)" type="button" class="inline-flex items-center px-3 py-2 text-sm font-medium text-center dark:text-white rounded-lg bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">
                        <svg class="w-4 h-4 mr-2" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                          <path d="M17.414 2.586a2 2 0 00-2.828 0L7 10.172V13h2.828l7.586-7.586a2 2 0 000-2.828z"></path>
                          <path fill-rule="evenodd" d="M2 6a2 2 0 012-2h4a1 1 0 010 2H4v10h10v-4a1 1 0 112 0v4a2 2 0 01-2 2H4a2 2 0 01-2-2V6z" clip-rule="evenodd"></path>
                        </svg>
                        Edit
                      </button>
                      <button @click="deletePoolSpace(poolSpace.id)" type="button" class="inline-flex items-center px-3 py-2 text-sm font-medium text-center text-white bg-red-600 rounded-lg hover:bg-red-800 focus:ring-4 focus:ring-red-300 dark:focus:ring-red-900">
                        <svg class="w-4 h-4 mr-2" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                          <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd"></path>
                        </svg>
                        Delete
                      </button>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
  
      <!-- Edit Modal -->
      <div v-if="isEditModalOpen" class="fixed inset-0 z-50 flex items-center justify-center overflow-auto bg-black bg-opacity-50">
        <div class="bg-white rounded-lg dark:bg-gray-700 w-1/2">
          <div class="p-4 border-b border-gray-200 dark:border-gray-600">
            <h3 class="text-xl font-semibold text-gray-900 dark:text-white">Edit Pool Space</h3>
          </div>
          <div class="p-4">
            <form @submit.prevent="updatePoolSpace">
              <div class="mb-4">
                <label for="title" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Title</label>
                <input v-model="editForm.title" type="text" id="title" class="w-full p-2 border rounded-lg dark:bg-gray-600 dark:text-white" required>
              </div>
              <div class="mb-4">
                <label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Email</label>
                <input v-model="editForm.email" type="email" id="email" class="w-full p-2 border rounded-lg dark:bg-gray-600 dark:text-white" required>
              </div>
              <div class="mb-4">
                <label for="number" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Number</label>
                <input v-model="editForm.number" type="text" id="number" class="w-full p-2 border rounded-lg dark:bg-gray-600 dark:text-white" required>
              </div>
              <div class="mb-4">
                <label for="address" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Address</label>
                <textarea v-model="editForm.address" id="address" class="w-full p-2 border rounded-lg dark:bg-gray-600 dark:text-white" required></textarea>
              </div>
              <div class="mb-4">
                <label for="status" class="block mb-2 text-sm font-medium text-gray-900  dark:text-gray-300">Status</label>
                <input v-model="editForm.status" type="text" id="number" class="w-full p-2 border rounded-lg dark:bg-gray-400 bg-gray-300 dark:text-white" readonly>
              
              </div>
              <div class="flex justify-end space-x-2">
                <button type="button" @click="closeEditModal" class="px-4 py-2 text-sm font-medium text-gray-900 bg-gray-200 rounded-lg dark:bg-gray-600 dark:text-white dark:hover:bg-gray-500">Cancel</button>
                <button type="submit" class="px-4 py-2 text-sm font-medium text-white bg-blue-600 rounded-lg dark:bg-blue-500 dark:hover:bg-blue-700">

                <v-icon v-if="loading" name="gi-spinning-blades" animation="spin"  scale="1"/> 
                  Save
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import axios from 'axios';
  import { ref, onMounted } from 'vue';
  import { useLoading } from '@/composables/loading';
  import { useUserStore } from '@/stores/user';
  import { useToast } from 'vue-toastify';

  const loading = useLoading();
  const poolSpaces = ref([]);
  const userStore = useUserStore();
  const isEditModalOpen = ref(false);
  const toast = useToast();
  const editForm = ref({
    id: null,
    title: '',
    email: '',
    number: '',
    address: '',
    status: '',
    latitude: null,
    longitude: null,
    user: null
  });

  async function getPoolSpaces() {
    try {
      loading.value = true;
      const response = await axios.get('/user-pool-spaces/', { 
        headers: {
          Authorization: `Bearer ${userStore.user.access}`,
        },
      });
      poolSpaces.value = response.data;
      console.log('User PoolSpaces:', response.data);
    } catch (error) {
      console.error('Error fetching user pool spaces:', error.message);
    } finally {
      loading.value = false;
    }
  }

  async function deletePoolSpace(id) {
    if (window.confirm('Are you sure you want to delete this pool space?')) {
      try {
        const response = await axios.delete(`/delete-pool/${id}/`, {
          headers: {
            Authorization: `Bearer ${userStore.user.access}`,
          },
        });
        poolSpaces.value = poolSpaces.value.filter(poolSpace => poolSpace.id !== id);
        toast.success('Pool space deleted successfully');
      } catch (error) {
        console.error('Error deleting pool space:', error.message);
        toast.error('Failed to delete pool space');
      }
    }
  }

  function openEditModal(poolSpace) {
    // Populate editForm with the selected poolSpace data
    editForm.value.id = poolSpace.id;
    editForm.value.title = poolSpace.title;
    editForm.value.email = poolSpace.email;
    editForm.value.number = poolSpace.number;
    editForm.value.address = poolSpace.address;
    editForm.value.status = poolSpace.status;
    editForm.value.latitude = poolSpace.latitude;
    editForm.value.longitude = poolSpace.longitude;
    editForm.value.user = poolSpace.user;
    isEditModalOpen.value = true;
  }

  function closeEditModal() {
    isEditModalOpen.value = false;
  }

  async function updatePoolSpace() {
    try {
      loading.value = true;
      const response = await axios.put(`pool-spaces/${editForm.value.id}/update/`, editForm.value, {
        headers: {
          Authorization: `Bearer ${userStore.user.access}`,
        },
      });
      const updatedPoolSpaceIndex = poolSpaces.value.findIndex(poolSpace => poolSpace.id === editForm.value.id);
      if (updatedPoolSpaceIndex !== -1) {
        poolSpaces.value[updatedPoolSpaceIndex] = response.data;
      }
      closeEditModal();
      toast.success('Pool Space updated successfully');
    } catch (error) {
      console.error('Error updating pool space:', error.message);
    }finally {
      loading.value = false;
    }
  }

  onMounted(() => {
    getPoolSpaces();
  });
</script>
