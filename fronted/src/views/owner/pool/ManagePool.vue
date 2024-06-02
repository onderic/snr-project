<template>
    <div class="2xl:max-w-[1220px] max-w-[1065px] mx-auto mt-10">
 <!-- component -->
<div class="sm:px-6 w-full">
            <div class=" mb-5">
                <div class="flex items-center justify-between">
                    <p class="focus:outline-none text-base dark:text-white sm:text-lg md:text-xl lg:text-2xl font-bold leading-normal text-gray-800">My PoolSpace</p>
                    <div class="py-1 px-4 flex items-center text-sm font-medium leading-none text-gray-600 bg-gray-200 hover:bg-gray-300 cursor-pointer rounded">
                        <!-- <p>Sort By:</p>
                        <select aria-label="select" class="focus:text-indigo-600 focus:outline-none bg-transparent ml-1">
                            <option class="text-sm text-indigo-800">Latest</option>
                            <option class="text-sm text-indigo-800">Oldest</option>
                            <option class="text-sm text-indigo-800">Latest</option>
                        </select> -->
                    </div>
                </div>
            </div>
            <div class="bg-white py-4 md:py-7 px-4 md:px-8 xl:px-10">
                <div class="sm:flex items-center justify-between">
                    <div class="flex items-center">
                        <a class="rounded-full focus:outline-none focus:ring-2  focus:bg-indigo-50 focus:ring-indigo-800" href=" javascript:void(0)">
                            <div class="py-2 px-8 bg-indigo-100 text-indigo-700 rounded-full">
                                <p>All</p>
                            </div>
                        </a>
                        <a class="rounded-full focus:outline-none focus:ring-2 focus:bg-indigo-50 focus:ring-indigo-800 ml-4 sm:ml-8" href="javascript:void(0)">
                            <div class="py-2 px-8 text-gray-600 hover:text-indigo-700 hover:bg-indigo-100 rounded-full ">
                                <p>Done</p>
                            </div>
                        </a>
                        <a class="rounded-full focus:outline-none focus:ring-2 focus:bg-indigo-50 focus:ring-indigo-800 ml-4 sm:ml-8" href="javascript:void(0)">
                            <div class="py-2 px-8 text-gray-600 hover:text-indigo-700 hover:bg-indigo-100 rounded-full ">
                                <p>Pending</p>
                            </div>
                        </a>
                    </div>
                    <button class="btn" >Add Event</button>
                   
                </div>
                <div class="mt-7 overflow-x-auto">
                    <table class="w-full whitespace-nowrap">
                        <tbody>
                            <tr tabindex="0" class="focus:outline-none h-16 border border-gray-100 rounded">
                                <td>
                                    <div class="ml-5">
                                        <div class="bg-gray-200 rounded-sm w-5 h-5 flex flex-shrink-0 justify-center items-center relative">
                                            <input placeholder="checkbox" type="checkbox" class="focus:opacity-100 checkbox opacity-0 absolute cursor-pointer w-full h-full" />
                                            <div class="check-icon hidden bg-indigo-700 text-white rounded-sm">
                                                  <v-icon name="px-checkbox-on" />
                                            </div>
                                        </div>
                                    </div>
                                </td>
                                <td class="">
                                    <div class="flex items-center pl-5">
                                        <p class="text-base font-medium leading-none text-gray-700 mr-2">Marketing Keynote Presentation</p>
                                        
                                    </div>
                                </td>
                                <td class="pl-24">
                                    <div class="flex items-center">
                                        
                                        <p class="text-sm leading-none text-gray-600 ml-2">Urgent</p>
                                    </div>
                                </td>
                               
                            </tr>
                            <tr class="h-3"></tr>
                          
                           
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        
</div>
</template>

<script>
export default {

}
</script>

<style>

</style>