<template>
    <div >


    <header class="absolute inset-x-0 top-0 z-50 py-6">
    <div class="mx-auto lg:max-w-7xl w-full px-5 sm:px-10 md:px-12 lg:px-5">
        <nav class="w-full flex justify-between gap-6 relative">
            <!-- logo -->
            <div class="min-w-max inline-flex relative">
                <a href="/" class="relative flex items-center gap-3">
                    <div class="relative w-7 h-7 overflow-hidden flex rounded-xl">
                      <img src="@/assets/ball.jpeg" alt="">
                    </div>
                    <div class="inline-flex text-lg font-semibold text-gray-900">
                        CueScore
                    </div>
                </a>
            </div>

            <div data-nav-overlay aria-hidden="true"
                class="fixed hidden inset-0 lg:!hidden bg-gray-800/60 bg-opacity-50 backdrop-filter backdrop-blur-xl">
            </div>
            <div data-navbar
                class="flex invisible opacity-0  translate-y-10 overflow-hidden lg:visible lg:opacity-100  lg:-translate-y-0 lg:scale-y-100 duration-300 ease-linear flex-col gap-y-6 gap-x-4 lg:flex-row w-full lg:justify-between lg:items-center absolute lg:relative top-full lg:top-0 bg-white lg:!bg-transparent border-x border-x-gray-100 lg:border-x-0">
                <ul
                    class="border-t border-gray-100  lg:border-t-0 px-6 lg:px-0 pt-6 lg:pt-0 flex flex-col lg:flex-row gap-y-4 gap-x-3 text-lg text-gray-700 w-full lg:justify-center lg:items-center">
                    <li>
                        <a href="#" class="duration-300 font-medium ease-linear hover:text-blue-600 py-3">
                            Home
                        </a>
                    </li>
                    <li>
                        <a href="#" class="duration-300 font-medium ease-linear hover:text-blue-600 py-3">
                            Services
                        </a>
                    </li>
                    <li>
                        <a href="#" class="duration-300 font-medium ease-linear hover:text-blue-600 py-3">
                            About us
                        </a>
                    </li>
                    <li>
                      <div>
                  <button
                  @click="toggleDarkMode"
                  class="sm:p-2 p-1 rounded-full relative sm:bg-gray-100 dark:bg-slate-900 dark:text-white"
                >
                  <template v-if="!isDark">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M12 3.25a8.75 8.75 0 0 1 8.75 8.75 8.75 8.75 0 0 1-8.75 8.75 8.75 8.75 0 0 1-8.75-8.75 8.75 8.75 0 0 1 8.75-8.75zm0-2.5a11.25 11.25 0 0 0-11.25 11.25 11.25 11.25 0 0 0 11.25 11.25 11.25 11.25 0 0 0 11.25-11.25 11.25 11.25 0 0 0-11.25-11.25z"></path>
                    </svg>
                  </template>
                  <template v-else>
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M12 3.25a8.75 8.75 0 0 1 8.75 8.75 8.75 8.75 0 0 1-8.75 8.75 8.75 8.75 0 0 1-8.75-8.75 8.75 8.75 0 0 1 8.75-8.75zm0-2.5a11.25 11.25 0 0 0-11.25 11.25 11.25 11.25 0 0 0 11.25 11.25 11.25 11.25 0 0 0 11.25-11.25 11.25 11.25 0 0 0-11.25-11.25z"></path>
                      <path d="M12 5.75a6.25 6.25 0 1 1 0 12.5 6.25 6.25 0 0 1 0-12.5zm0-2.5a8.75 8.75 0 0 0-8.75 8.75 8.75 8.75 0 0 0 8.75 8.75 8.75 8.75 0 0 0 8.75-8.75 8.75 8.75 0 0 0-8.75-8.75z"></path>
                    </svg>
                  </template>
                  <span class="sr-only">Switch to light / dark version</span>
          </button>
  
                
            </div>
                    </li>
                </ul>

                <div
                    class="lg:min-w-max flex items-center sm:w-max w-full pb-6 lg:pb-0 border-b border-gray-100   lg:border-0 px-6 lg:px-0">
                    <router-link to="/dashboard"
                        class="flex justify-center items-center w-full sm:w-max px-6 h-12 rounded-full outline-none relative overflow-hidden border duration-300 ease-linear
                    after:absolute after:inset-x-0 after:aspect-square after:scale-0 after:opacity-70 after:origin-center after:duration-300 after:ease-linear after:rounded-full after:top-0 after:left-0 after:bg-[#172554] hover:after:opacity-100 hover:after:scale-[2.5] bg-blue-600 border-transparent hover:border-[#172554]">
                        <span class="relative z-10 text-white">
                            Get Started
                        </span>
                 
                  </router-link>
                </div>
            </div>


            <div class="min-w-max flex items-center gap-x-3">

                <button data-toggle-navbar data-is-open="false"
                    class="lg:hidden lg:invisible outline-none w-7 h-auto flex flex-col relative">
                    <span id="line-1"
                        class="w-6 h-0.5 rounded-full bg-gray-700 transition-all duration-300 ease-linear"></span>
                    <span id="line-2"
                        class="w-6 origin-center  mt-1 h-0.5 rounded-ful bg-gray-700 transition-all duration-300 ease-linear"></span>
                    <span id="line-3"
                        class="w-6 mt-1 h-0.5 rounded-ful bg-gray-700 transition-all duration-300 ease-linear"></span>
                    <span class="sr-only">togglenav</span>
                </button>
            </div>
        </nav>
    </div>
</header>

<!-- hero section -->
<section class="relative py-32 lg:py-36 bg-white dark:bg-gray-900">
    <div
        class="mx-auto lg:max-w-7xl w-full px-5 sm:px-10 md:px-12 lg:px-5 flex flex-col lg:flex-row gap-10 lg:gap-12">
        <div class="absolute w-full lg:w-1/2 inset-y-0 lg:right-0 hidden lg:block">
            <span
                class="absolute -left-6 md:left-4 top-24 lg:top-28 w-24 h-24 rotate-90 skew-x-12 rounded-3xl bg-green-400 blur-xl opacity-60 lg:opacity-95 lg:block hidden dark:bg-green-600 dark:opacity-70"></span>
            <span class="absolute right-4 bottom-12 w-24 h-24 rounded-3xl bg-blue-600 blur-xl opacity-80 dark:bg-blue-700 dark:opacity-90"></span>
        </div>
        <span
            class="w-4/12 lg:w-2/12 aspect-square bg-gradient-to-tr from-blue-600 to-green-400 absolute -top-5 lg:left-0 rounded-full skew-y-12 blur-2xl opacity-40 skew-x-12 rotate-90 dark:from-blue-700 dark:to-green-700 dark:opacity-50"></span>
        <div class="relative flex flex-col items-center text-center lg:text-left lg:py-7 xl:py-8 
            lg:items-start lg:max-w-none max-w-3xl mx-auto lg:mx-0 lg:flex-1 lg:w-1/2">
            <h1 class="text-3xl leading-tight sm:text-4xl md:text-5xl xl:text-6xl
                font-bold text-gray-900 dark:text-gray-100">
                Discover and Connect with <span
                    class="text-transparent bg-clip-text bg-gradient-to-br from-indigo-600 from-20% via-blue-600 via-30% to-green-600 dark:from-indigo-400 dark:via-blue-400 dark:to-green-400">Local Pool
                    Centers</span> and Tournaments.
            </h1>
            <p class="mt-8 text-gray-700 dark:text-gray-300">
                Find pool centers near you, join exciting tournaments, and connect with fellow players. 
                For owners, easily upload your pool center details and organize tournaments to reach more players.
            </p>
            <div class="mt-10 w-full flex max-w-md mx-auto lg:mx-0">
                <div class="flex sm:flex-row flex-col gap-5 w-full">
                    <router-link to="/dashboard">
                        <button class="flex text-white justify-center items-center w-max min-w-max sm:w-max px-6 h-12 rounded-full outline-none relative overflow-hidden border duration-300 ease-linear
                                        after:absolute after:inset-x-0 after:aspect-square after:scale-0 after:opacity-70 after:origin-center after:duration-300 after:ease-linear after:rounded-full after:top-0 after:left-0 after:bg-[#172554] hover:after:opacity-100 hover:after:scale-[2.5] bg-blue-600 border-transparent hover:border-[#172554] dark:bg-blue-700 dark:hover:bg-blue-800 dark:after:bg-[#1a1a1a]">
                            <span class="hidden sm:flex relative z-[5]">
                                Discover Now
                            </span>
                        </button>
                    </router-link>
                </div>
            </div>
        </div>

        <div class="flex flex-1 lg:w-1/2 lg:h-auto relative lg:max-w-none lg:mx-0 mx-auto max-w-3xl">
            <img src="@/assets/p.jpg" alt="Hero image" width="2350" height="2359"
                class="lg:absolute lg:w-full lg:h-full rounded-3xl object-cover lg:max-h-none max-h-96">
        </div>
    </div>
</section>


    <div class="relative overflow-hidden dark:bg-darker lg:overflow-auto">
      <header
       
      >

        <div class="absolute inset-0 bg-black opacity-50"></div>
        <div class="relative flex items-center justify-center h-full text-center text-white p-6">
            <div>
                <h1 class="text-4xl md:text-6xl font-bold mb-4">Welcome to Our Service</h1>
                <p class="text-lg mb-8">Discover what we can do for you.</p>
                <a href="#discover" class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-6 rounded-lg transition duration-300">Discover</a>
            </div>
        </div>
    </header>
    </div>
  
  
  
    <div class="relative overflow-hidden dark:bg-darker lg:overflow-auto bg-white dark:bg-gray-900">
    <div class="mx-auto max-w-7xl px-8 md:px-12 lg:px-6 xl:px-0 mb-10 mt-10">
      <div class="py-12 text-center">
        <h2 class="text-5xl font-semibold text-gray-800 dark:text-white mb-6 capitalize font-serif">How it works</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <!-- Step 1 -->
          <div class="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-md">
            <div class="flex justify-center mb-4">
              <svg class="w-12 h-12 text-blue-500" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="user-plus" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 512">
                <path fill="currentColor" d="M224 256A128 128 0 1 0 224 0a128 128 0 1 0 0 256zM288 288H160C71.63 288 0 359.6 0 448c0 17.67 14.33 32 32 32H416c17.67 0 32-14.33 32-32C448 359.6 376.4 288 288 288zM616 224H568V176C568 167.2 560.8 160 552 160S536 167.2 536 176V224H488C479.2 224 472 231.2 472 240S479.2 256 488 256H536V304C536 312.8 543.2 320 552 320S568 312.8 568 304V256H616C624.8 256 632 248.8 632 240S624.8 224 616 224z"></path>
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-gray-800 dark:text-white mb-2">Create Account</h3>
            <p class="text-gray-600 dark:text-gray-300">Sign up with your email and get started in no time.</p>
          </div>
          <!-- Step 2 -->
          <div class="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-md">
            <div class="flex justify-center mb-4">
              <svg class="w-12 h-12 text-blue-500" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="upload" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
                <path fill="currentColor" d="M472 344H328c-6.617 0-12 5.383-12 12v136c0 6.617 5.383 12 12 12h144c6.617 0 12-5.383 12-12V356c0-6.617-5.383-12-12-12zM484 0H124C55.59 0 0 55.59 0 124v264c0 68.41 55.59 124 124 124h144v-96H164v-40h104v-48H164v-40h104v-48H164v-40h104v-48H164V64h232v288h-48v48h48v48h48V64h48v264h40V124C512 55.59 456.4 0 388 0zM256 160c-6.617 0-12 5.383-12 12v176c0 6.617 5.383 12 12 12s12-5.383 12-12V172C268 165.4 262.6 160 256 160zM128 172v176c0 6.617 5.383 12 12 12s12-5.383 12-12V172c0-6.617-5.383-12-12-12S128 165.4 128 172z"></path>
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-gray-800 dark:text-white mb-2">Upload Resume</h3>
            <p class="text-gray-600 dark:text-gray-300">Easily upload your resume to showcase your skills and experience.</p>
          </div>
          <!-- Step 3 -->
          <div class="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-md">
            <div class="flex justify-center mb-4">
              <svg class="w-12 h-12 text-blue-500" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="search" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
                <path fill="currentColor" d="M505 442.7L405.3 343C418.9 317.9 426.3 290 426.3 260.5C426.3 117.3 334.3 25.3 191.1 25.3S-44 117.3-44 260.5C-44 403.7 47.9 495.7 191.1 495.7C220.6 495.7 248.5 488.3 273.6 474.7L373.3 574.4C377.6 578.7 384.5 578.7 388.9 574.4L504.4 459C508.8 454.7 508.8 447.8 505 442.7zM191.1 426.3C105.4 426.3 38.3 359.2 38.3 273.5C38.3 187.8 105.4 120.7 191.1 120.7C276.8 120.7 343.9 187.8 343.9 273.5C343.9 359.2 276.8 426.3 191.1 426.3z"></path>
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-gray-800 dark:text-white mb-2">Find Job</h3>
            <p class="text-gray-600 dark:text-gray-300">Search for jobs that match your qualifications and apply directly.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
  
  
  
    <div class="relative overflow-hidden dark:bg-darker lg:overflow-auto mb-10">
    <div class="mx-auto max-w-7xl px-8 md:px-12 lg:px-6 xl:px-0">
     
      <div class="py-12 ">
          <h2 class="text-5xl text-center font-semibold text-gray-800 dark:text-white mb-6 capitalize font-serif">What they say about us</h2>
        
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mt-10 mb-10">
          
          <!-- Testimonial Card 1 -->
          <div class="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-md ">
            <div class="flex justify-start mb-8">
              <div class="flex space-x-3">
                <svg class="w-5 h-5 text-yellow-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12 .587l3.668 7.568L24 9.75l-6 6.175 1.46 8.573L12 18.897l-7.46 5.601L6 15.925 0 9.75l8.332-1.595z"/></svg>
                <svg class="w-5 h-5 text-yellow-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12 .587l3.668 7.568L24 9.75l-6 6.175 1.46 8.573L12 18.897l-7.46 5.601L6 15.925 0 9.75l8.332-1.595z"/></svg>
                <svg class="w-5 h-5 text-yellow-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12 .587l3.668 7.568L24 9.75l-6 6.175 1.46 8.573L12 18.897l-7.46 5.601L6 15.925 0 9.75l8.332-1.595z"/></svg>
                <svg class="w-5 h-5 text-yellow-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12 .587l3.668 7.568L24 9.75l-6 6.175 1.46 8.573L12 18.897l-7.46 5.601L6 15.925 0 9.75l8.332-1.595z"/></svg>
                <svg class="w-5 h-5 text-yellow-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12 .587l3.668 7.568L24 9.75l-6 6.175 1.46 8.573L12 18.897l-7.46 5.601L6 15.925 0 9.75l8.332-1.595z"/></svg>
              </div>
            </div>
            <p  class="text-lg text-gray-600 dark:text-gray-300 mb-8">Working with this company has been an absolute pleasure. Their professionalism and dedication to excellence are evident in every interaction.</p>
            <div class="flex items-center justify-start">
              <img class="w-10 h-10 rounded-full mr-4" src="@/assets/ball.jpeg" alt="User 1">
              <div class="text-left">
                <p class="text-gray-800 dark:text-white font-semibold">John Doe</p>
                <p class="text-gray-600 dark:text-gray-300 text-sm">House Manager</p>
              </div>
            </div>
          </div>
  
          <div class="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-md ">
            <div class="flex justify-start mb-8">
              <div class="flex space-x-3">
                <svg class="w-5 h-5 text-yellow-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12 .587l3.668 7.568L24 9.75l-6 6.175 1.46 8.573L12 18.897l-7.46 5.601L6 15.925 0 9.75l8.332-1.595z"/></svg>
                <svg class="w-5 h-5 text-yellow-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12 .587l3.668 7.568L24 9.75l-6 6.175 1.46 8.573L12 18.897l-7.46 5.601L6 15.925 0 9.75l8.332-1.595z"/></svg>
                <svg class="w-5 h-5 text-yellow-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12 .587l3.668 7.568L24 9.75l-6 6.175 1.46 8.573L12 18.897l-7.46 5.601L6 15.925 0 9.75l8.332-1.595z"/></svg>
                <svg class="w-5 h-5 text-yellow-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12 .587l3.668 7.568L24 9.75l-6 6.175 1.46 8.573L12 18.897l-7.46 5.601L6 15.925 0 9.75l8.332-1.595z"/></svg>
                <svg class="w-5 h-5 text-yellow-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12 .587l3.668 7.568L24 9.75l-6 6.175 1.46 8.573L12 18.897l-7.46 5.601L6 15.925 0 9.75l8.332-1.595z"/></svg>
              </div>
            </div>
            <p  class="text-lg text-gray-600 dark:text-gray-300 mb-8">Working with this company has been an absolute pleasure. Their professionalism and dedication to excellence are evident in every interaction.</p>
            <div class="flex items-center justify-start">
              <img class="w-10 h-10 rounded-full mr-4" src="@/assets/ball.jpeg" alt="User 1">
              <div class="text-left">
                <p class="text-gray-800 dark:text-white font-semibold">John Makau</p>
                <p class="text-gray-600 dark:text-gray-300 text-sm">Store Keeper</p>
              </div>
            </div>
          </div>
  
          <div class="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-md ">
            <div class="flex justify-start mb-8">
              <div class="flex space-x-3">
                <svg class="w-5 h-5 text-yellow-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12 .587l3.668 7.568L24 9.75l-6 6.175 1.46 8.573L12 18.897l-7.46 5.601L6 15.925 0 9.75l8.332-1.595z"/></svg>
                <svg class="w-5 h-5 text-yellow-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12 .587l3.668 7.568L24 9.75l-6 6.175 1.46 8.573L12 18.897l-7.46 5.601L6 15.925 0 9.75l8.332-1.595z"/></svg>
                <svg class="w-5 h-5 text-yellow-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12 .587l3.668 7.568L24 9.75l-6 6.175 1.46 8.573L12 18.897l-7.46 5.601L6 15.925 0 9.75l8.332-1.595z"/></svg>
                <svg class="w-5 h-5 text-yellow-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12 .587l3.668 7.568L24 9.75l-6 6.175 1.46 8.573L12 18.897l-7.46 5.601L6 15.925 0 9.75l8.332-1.595z"/></svg>
                <svg class="w-5 h-5 text-yellow-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12 .587l3.668 7.568L24 9.75l-6 6.175 1.46 8.573L12 18.897l-7.46 5.601L6 15.925 0 9.75l8.332-1.595z"/></svg>
              </div>
            </div>
            <p  class="text-lg text-gray-600 dark:text-gray-300 mb-8">Working with this company has been an absolute pleasure. Their professionalism and dedication to excellence are evident in every interaction.</p>
            <div class="flex items-center justify-start">
              <img class="w-10 h-10 rounded-full mr-4" src="@/assets/ball.jpeg" alt="User 1">
              <div class="text-left">
                <p class="text-gray-800 dark:text-white font-semibold">Onderi Doe</p>
                <p class="text-gray-600 dark:text-gray-300 text-sm">Cleaner</p>
              </div>
            </div>
          </div>
          
         
  
        </div>
      </div>
    </div>
  </div>
  
  
  
  
  <footer class="bg-white dark:bg-gray-900">
      <div class="mx-auto w-full max-w-screen-xl">
        <div class="grid grid-cols-2 gap-8 px-4 py-6 lg:py-8 md:grid-cols-4">
          <div>
              <h2 class="mb-6 text-sm font-semibold text-gray-900 uppercase dark:text-white">Company</h2>
              <ul class="text-gray-500 dark:text-gray-400 font-medium">
                  <li class="mb-4">
                      <a href="#" class=" hover:underline">About</a>
                  </li>
                  <li class="mb-4">
                      <a href="#" class="hover:underline">Careers</a>
                  </li>
                  <li class="mb-4">
                      <a href="#" class="hover:underline">Brand Center</a>
                  </li>
                  <li class="mb-4">
                      <a href="#" class="hover:underline">Blog</a>
                  </li>
              </ul>
          </div>
          <div>
              <h2 class="mb-6 text-sm font-semibold text-gray-900 uppercase dark:text-white">Help center</h2>
              <ul class="text-gray-500 dark:text-gray-400 font-medium">
                  <li class="mb-4">
                      <a href="#" class="hover:underline">Discord Server</a>
                  </li>
                  <li class="mb-4">
                      <a href="#" class="hover:underline">Twitter</a>
                  </li>
                  <li class="mb-4">
                      <a href="#" class="hover:underline">Facebook</a>
                  </li>
                  <li class="mb-4">
                      <a href="#" class="hover:underline">Contact Us</a>
                  </li>
              </ul>
          </div>
          <div>
              <h2 class="mb-6 text-sm font-semibold text-gray-900 uppercase dark:text-white">Legal</h2>
              <ul class="text-gray-500 dark:text-gray-400 font-medium">
                  <li class="mb-4">
                      <a href="#" class="hover:underline">Privacy Policy</a>
                  </li>
                  <li class="mb-4">
                      <a href="#" class="hover:underline">Licensing</a>
                  </li>
                  <li class="mb-4">
                      <a href="#" class="hover:underline">Terms &amp; Conditions</a>
                  </li>
              </ul>
          </div>
          <div>
              <h2 class="mb-6 text-sm font-semibold text-gray-900 uppercase dark:text-white">Download</h2>
              <ul class="text-gray-500 dark:text-gray-400 font-medium">
                  <li class="mb-4">
                      <a href="#" class="hover:underline">Discord Server</a>
                  </li>
                  <li class="mb-4">
                      <a href="#" class="hover:underline">Twitter</a>
                  </li>
                  <li class="mb-4">
                      <a href="#" class="hover:underline">Facebook</a>
                  </li>
                  <li class="mb-4">
                      <a href="#" class="hover:underline">Contact Us</a>
                  </li>
              </ul>
          </div>
      </div>
      <div class="px-4 py-6 bg-gray-100 dark:bg-gray-700 md:flex md:items-center md:justify-between">
          <span class="text-sm text-gray-500 dark:text-gray-300 sm:text-center">© 2024 <a href="/">RoyalPrinceAgencyLtd™</a>. All Rights Reserved.
          </span>
          <div class="flex mt-4 sm:justify-center md:mt-0 space-x-5 rtl:space-x-reverse">
              <a href="#" class="text-gray-400 hover:text-gray-900 dark:hover:text-white">
                    <svg class="w-4 h-4" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 8 19">
                          <path fill-rule="evenodd" d="M6.135 3H8V0H6.135a4.147 4.147 0 0 0-4.142 4.142V6H0v3h2v9.938h3V9h2.021l.592-3H5V3.591A.6.6 0 0 1 5.592 3h.543Z" clip-rule="evenodd"/>
                      </svg>
                    <span class="sr-only">Facebook page</span>
                </a>
                <a href="#" class="text-gray-400 hover:text-gray-900 dark:hover:text-white">
                    <svg class="w-4 h-4" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 21 16">
                          <path d="M16.942 1.556a16.3 16.3 0 0 0-4.126-1.3 12.04 12.04 0 0 0-.529 1.1 15.175 15.175 0 0 0-4.573 0 11.585 11.585 0 0 0-.535-1.1 16.274 16.274 0 0 0-4.129 1.3A17.392 17.392 0 0 0 .182 13.218a15.785 15.785 0 0 0 4.963 2.521c.41-.564.773-1.16 1.084-1.785a10.63 10.63 0 0 1-1.706-.83c.143-.106.283-.217.418-.33a11.664 11.664 0 0 0 10.118 0c.137.113.277.224.418.33-.544.328-1.116.606-1.71.832a12.52 12.52 0 0 0 1.084 1.785 16.46 16.46 0 0 0 5.064-2.595 17.286 17.286 0 0 0-2.973-11.59ZM6.678 10.813a1.941 1.941 0 0 1-1.8-2.045 1.93 1.93 0 0 1 1.8-2.047 1.919 1.919 0 0 1 1.8 2.047 1.93 1.93 0 0 1-1.8 2.045Zm6.644 0a1.94 1.94 0 0 1-1.8-2.045 1.93 1.93 0 0 1 1.8-2.047 1.918 1.918 0 0 1 1.8 2.047 1.93 1.93 0 0 1-1.8 2.045Z"/>
                      </svg>
                    <span class="sr-only">Discord community</span>
                </a>
                <a href="#" class="text-gray-400 hover:text-gray-900 dark:hover:text-white">
                    <svg class="w-4 h-4" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 17">
                      <path fill-rule="evenodd" d="M20 1.892a8.178 8.178 0 0 1-2.355.635 4.074 4.074 0 0 0 1.8-2.235 8.344 8.344 0 0 1-2.605.98A4.13 4.13 0 0 0 13.85 0a4.068 4.068 0 0 0-4.1 4.038 4 4 0 0 0 .105.919A11.705 11.705 0 0 1 1.4.734a4.006 4.006 0 0 0 1.268 5.392 4.165 4.165 0 0 1-1.859-.5v.05A4.057 4.057 0 0 0 4.1 9.635a4.19 4.19 0 0 1-1.856.07 4.108 4.108 0 0 0 3.831 2.807A8.36 8.36 0 0 1 0 14.184 11.732 11.732 0 0 0 6.291 16 11.502 11.502 0 0 0 17.964 4.5c0-.177 0-.35-.012-.523A8.143 8.143 0 0 0 20 1.892Z" clip-rule="evenodd"/>
                  </svg>
                    <span class="sr-only">Twitter page</span>
                </a>
                <a href="#" class="text-gray-400 hover:text-gray-900 dark:hover:text-white">
                    <svg class="w-4 h-4" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                          <path fill-rule="evenodd" d="M10 .333A9.911 9.911 0 0 0 6.866 19.65c.5.092.678-.215.678-.477 0-.237-.01-1.017-.014-1.845-2.757.6-3.338-1.169-3.338-1.169a2.627 2.627 0 0 0-1.1-1.451c-.9-.615.07-.6.07-.6a2.084 2.084 0 0 1 1.518 1.021 2.11 2.11 0 0 0 2.884.823c.044-.503.268-.973.63-1.325-2.2-.25-4.516-1.1-4.516-4.9A3.832 3.832 0 0 1 4.7 7.068a3.56 3.56 0 0 1 .095-2.623s.832-.266 2.726 1.016a9.409 9.409 0 0 1 4.962 0c1.89-1.282 2.717-1.016 2.717-1.016.366.83.402 1.768.1 2.623a3.827 3.827 0 0 1 1.02 2.659c0 3.807-2.319 4.644-4.525 4.889a2.366 2.366 0 0 1 .673 1.834c0 1.326-.012 2.394-.012 2.72 0 .263.18.572.681.475A9.911 9.911 0 0 0 10 .333Z" clip-rule="evenodd"/>
                    </svg>
                    <span class="sr-only">GitHub account</span>
                </a>
                <a href="#" class="text-gray-400 hover:text-gray-900 dark:hover:text-white">
                    <svg class="w-4 h-4" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                      <path fill-rule="evenodd" d="M10 0a10 10 0 1 0 10 10A10.009 10.009 0 0 0 10 0Zm6.613 4.614a8.523 8.523 0 0 1 1.93 5.32 20.094 20.094 0 0 0-5.949-.274c-.059-.149-.122-.292-.184-.441a23.879 23.879 0 0 0-.566-1.239 11.41 11.41 0 0 0 4.769-3.366ZM8 1.707a8.821 8.821 0 0 1 2-.238 8.5 8.5 0 0 1 5.664 2.152 9.608 9.608 0 0 1-4.476 3.087A45.758 45.758 0 0 0 8 1.707ZM1.642 8.262a8.57 8.57 0 0 1 4.73-5.981A53.998 53.998 0 0 1 9.54 7.222a32.078 32.078 0 0 1-7.9 1.04h.002Zm2.01 7.46a8.51 8.51 0 0 1-2.2-5.707v-.262a31.64 31.64 0 0 0 8.777-1.219c.243.477.477.964.692 1.449-.114.032-.227.067-.336.1a13.569 13.569 0 0 0-6.942 5.636l.009.003ZM10 18.556a8.508 8.508 0 0 1-5.243-1.8 11.717 11.717 0 0 1 6.7-5.332.509.509 0 0 1 .055-.02 35.65 35.65 0 0 1 1.819 6.476 8.476 8.476 0 0 1-3.331.676Zm4.772-1.462A37.232 37.232 0 0 0 13.113 11a12.513 12.513 0 0 1 5.321.364 8.56 8.56 0 0 1-3.66 5.73h-.002Z" clip-rule="evenodd"/>
                  </svg>
                    <span class="sr-only">Dribbble account</span>
                </a>
          </div>
        </div>
      </div>
  </footer>
  
    
    
    
    </div>
    </template>
    
    <script setup>
    import { useDark, useToggle } from '@vueuse/core'
    import { onMounted } from 'vue'
    import { 
        initAccordions, 
        initCarousels, 
        initCollapses, 
        initDials, 
        initDismisses, 
        initDrawers, 
        initDropdowns, 
        initModals, 
        initPopovers, 
        initTabs, 
        initTooltips } from 'flowbite'
    
    // initialize components based on data attribute selectors
    onMounted(() => {
        initAccordions();
        initCarousels();
        initCollapses();
        initDials();
        initDismisses();
        initDrawers();
        initDropdowns();
        initModals();
        initPopovers();
        initTabs();
        initTooltips();
    })
  
    
  
    const isDark = useDark()
    const toggleDark = useToggle(isDark)
  
    const toggleDarkMode = () => {
      toggleDark()
    }
    </script>
    
  
  <style scoped>
     .bg-cover {
            background-size: cover;
        }
  </style>  