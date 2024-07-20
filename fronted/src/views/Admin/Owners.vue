<template>
   <div class="2xl:max-w-[1220px] max-w-[1065px] mx-auto lg:mt-20 mt-4">
      <div class="p-4 bg-white block sm:flex items-center justify-between border-b border-gray-200  dark:bg-gray-800 dark:border-gray-700">
        <div class="w-full mb-1">
          <div class="mb-4">
            <h1 class="text-xl font-semibold text-gray-900 sm:text-2xl dark:text-white">All Owners</h1>
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
                    <th scope="col" class="p-4 text-xs font-medium text-left text-gray-500 uppercase dark:text-gray-400">Name</th>
                    <th scope="col" class="p-4 text-xs font-medium text-left text-gray-500 uppercase dark:text-gray-400">Email</th>
                    <th scope="col" class="p-4 text-xs font-medium text-left text-gray-500 uppercase dark:text-gray-400">Phone Number</th>
                    <th scope="col" class="p-4 text-xs font-medium text-left text-gray-500 uppercase dark:text-gray-400">Joined</th>
                    <th scope="col" class="p-4 text-xs font-medium text-left text-gray-500 uppercase dark:text-gray-400">Actions</th>
                  </tr>
                </thead>
                <tbody class="bg-white divide-y divide-gray-200 dark:bg-gray-800 dark:divide-gray-700">
                  <template v-if="loading">
                    <tr v-for="n in 5" :key="n" class="animate-pulse">
                      <td class="p-4 text-base font-medium text-gray-900 whitespace-nowrap dark:text-white">
                        <div class="h-4 bg-gray-200 rounded dark:bg-gray-700 w-48"></div>
                      </td>
                      <td class="p-4 text-base font-medium text-gray-900 whitespace-nowrap dark:text-white">
                        <div class="h-4 bg-gray-200 rounded dark:bg-gray-700 w-48"></div>
                      </td>
                      <td class="p-4 text-base font-medium text-gray-900 whitespace-nowrap dark:text-white">
                        <div class="h-4 bg-gray-200 rounded dark:bg-gray-700 w-48"></div>
                      </td>
                      <td class="p-4 text-base font-medium text-gray-900 whitespace-nowrap dark:text-white">
                        <div class="h-4 bg-gray-200 rounded dark:bg-gray-700 w-48"></div>
                      </td>
                      <td class="p-4 space-x-2 whitespace-nowrap">
                        <div class="h-8 bg-gray-200 rounded dark:bg-gray-700 w-24"></div>
                      </td>
                    </tr>
                  </template>
                  <template v-else>
                    <tr v-for="owner in owners" :key="owner.id" class="hover:bg-gray-100 dark:hover:bg-gray-700">
                      <td class="p-4 text-base font-medium text-gray-900 whitespace-nowrap dark:text-white">{{ owner.name }}</td>
                      <td class="p-4 text-base font-medium text-gray-900 whitespace-nowrap dark:text-white">{{ owner.email }}</td>
                      <td class="p-4 text-base font-medium text-gray-900 whitespace-nowrap dark:text-white">{{ owner.phone_number }}</td>
                      <td class="p-4 text-base font-medium text-gray-900 whitespace-nowrap dark:text-white">{{ owner.date_joined }}</td>
                      <td class="p-4 space-x-2 whitespace-nowrap">
                        <button @click="openEditModal(owner)" type="button" class="inline-flex items-center px-3 py-2 text-sm font-medium text-center dark:text-white rounded-lg bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">
                          <svg class="w-4 h-4 mr-2" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                            <path d="M17.414 2.586a2 2 0 00-2.828 0L7 10.172V13h2.828l7.586-7.586a2 2 0 000-2.828z"></path>
                            <path fill-rule="evenodd" d="M2 6a2 2 0 012-2h4a1 1 0 010 2H4v10h10v-4a1 1 0 112 0v4a2 2 0 01-2 2H4a2 2 0 01-2-2V6z" clip-rule="evenodd"></path>
                          </svg>
                          Edit
                        </button>
                        <button @click="deleteOwner(owner.id)" type="button" class="inline-flex items-center px-3 py-2 text-sm font-medium text-center text-white bg-red-600 rounded-lg hover:bg-red-800 focus:ring-4 focus:ring-red-300 dark:focus:ring-red-900">
                          <svg class="w-4 h-4 mr-2" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                            <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd"></path>
                          </svg>
                          Delete
                        </button>
                      </td>
                    </tr>
                  </template>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import axios from 'axios';
  import { ref, onMounted } from 'vue';
  import { useUserStore } from '@/stores/user';
  import { useToast } from 'vue-toastify';
  
  const loading = ref(false);
  const owners = ref([]);
  const userStore = useUserStore();
  const toast = useToast();
  
  const fetchOwners = async () => {
    try {
      loading.value = true;
      const response = await axios.get('/users/owners/', {
        headers: {
          Authorization: `Bearer ${userStore.user.access}`,
        },
      });
      owners.value = response.data;
    } catch (error) {
      console.error('Error fetching owners:', error);
      toast.error('Failed to fetch owners');
    } finally {
      loading.value = false;
    }
  };
  
  const deleteOwner = async (id) => {
    if (window.confirm('Are you sure you want to delete this owner?')) {
      try {
        await axios.delete(`/api/users/${id}/`, {
          headers: {
            Authorization: `Bearer ${userStore.user.access}`,
          },
        });
        owners.value = owners.value.filter(owner => owner.id !== id);
        toast.success('Owner deleted successfully');
      } catch (error) {
        console.error('Error deleting owner:', error);
        toast.error('Failed to delete owner');
      }
    }
  };
  
  const openEditModal = (owner) => {
    // handle opening the edit modal
  };
  
  onMounted(fetchOwners);
  </script>
  