<template>
   <div>
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
                        <a href="/" class="duration-300 font-medium ease-linear hover:text-blue-600 py-3">
                            Home
                        </a>
                    </li>
                    <li>
                     <router-link to="/guide">
                      <a href="#" class="duration-300 font-medium ease-linear hover:text-blue-600 py-3">
                            User Guide
                        </a>
                     </router-link>
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

    <div class="bg-gray-100 min-h-screen p-6 mt-20">
      <div class="container mx-auto  bg-white shadow-md rounded-lg overflow-hidden">
        <!-- Header -->
        <header class="bg-gray-200 text-dark py-4 px-6">
          <h1 class="text-3xl text-dar font-semibold">User Guide</h1>
        </header>
  
        <!-- Main Content -->
        <main class="p-6">
          <section class="mb-6">
            <h2 class="text-2xl font-semibold mb-4">Introduction</h2>
            <p class="text-gray-700">
              Welcome to the user guide. This guide will help you navigate and make the most out of our application.
            </p>
          </section>
  
          <!-- Table of Contents -->
          <section class="mb-6">
            <h2 class="text-2xl font-semibold mb-4">Table of Contents</h2>
            <ul class="list-disc pl-5 text-gray-700">
              <li><a href="#getting-started" class="text-blue-500 hover:underline">Getting Started</a></li>
              <li><a href="#features" class="text-blue-500 hover:underline">Features</a></li>
              <li><a href="#troubleshooting" class="text-blue-500 hover:underline">Troubleshooting</a></li>
            </ul>
          </section>
  
          <!-- Sections -->
          <section id="getting-started" class="mb-6">
            <h2 class="text-2xl font-semibold mb-4">Getting Started</h2>
            <p class="text-gray-700">
              Here’s how you can get started with our application.
            </p>
            <div class="relative overflow-hidden dark:bg-darker lg:overflow-auto bg-white dark:bg-gray-900">
    <div class="mx-auto max-w-7xl px-8 md:px-12 lg:px-6 xl:px-0 mb-10 mt-10">
      <div class="py-12 text-center">
        <h2 class="text-5xl font-semibold text-gray-800 dark:text-white mb-6 capitalize font-serif">How It Works</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <!-- Step 1 -->
          <div class="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-md">
            <div class="flex justify-center mb-4">
              <svg class="w-12 h-12 text-blue-500" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="user-plus" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 512">
                <path fill="currentColor" d="M224 256A128 128 0 1 0 224 0a128 128 0 1 0 0 256zM288 288H160C71.63 288 0 359.6 0 448c0 17.67 14.33 32 32 32H416c17.67 0 32-14.33 32-32C448 359.6 376.4 288 288 288zM616 224H568V176C568 167.2 560.8 160 552 160S536 167.2 536 176V224H488C479.2 224 472 231.2 472 240S479.2 256 488 256H536V304C536 312.8 543.2 320 552 320S568 312.8 568 304V256H616C624.8 256 632 248.8 632 240S624.8 224 616 224z"></path>
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-gray-800 dark:text-white mb-2">Create Account</h3>
            <p class="text-gray-600 dark:text-gray-300">Sign up using your email address to quickly set up your account and gain access to all the features.</p>
          </div>
          <!-- Step 2 -->
          <div class="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-md">
            <div class="flex justify-center mb-4">
              <svg class="w-12 h-12 text-blue-500" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="upload" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
                <path fill="currentColor" d="M472 344H328c-6.617 0-12 5.383-12 12v136c0 6.617 5.383 12 12 12h144c6.617 0 12-5.383 12-12V356c0-6.617-5.383-12-12-12zM484 0H124C55.59 0 0 55.59 0 124v264c0 68.41 55.59 124 124 124h144v-96H164v-40h104v-48H164v-40h104v-48H164v-40h104v-48H164V64h232v288h-48v48h48v48h48V64h48v264h40V124C512 55.59 456.4 0 388 0zM256 160c-6.617 0-12 5.383-12 12v176c0 6.617 5.383 12 12 12s12-5.383 12-12V172C268 165.4 262.6 160 256 160zM128 172v176c0 6.617 5.383 12 12 12s12-5.383 12-12V172c0-6.617-5.383-12-12-12S128 165.4 128 172z"></path>
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-gray-800 dark:text-white mb-2">Upload Pools</h3>
            <p class="text-gray-600 dark:text-gray-300">Showcase your skills by uploading your pool profiles. It’s easy and helps others see what you have to offer.</p>
          </div>
          <!-- Step 3 -->
          <div class="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-md">
            <div class="flex justify-center mb-4">
              <svg class="w-12 h-12 text-blue-500" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="search" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
                <path fill="currentColor" d="M505 442.7L405.3 343C418.9 317.9 426.3 290 426.3 260.5C426.3 117.3 334.3 25.3 191.1 25.3S-44 117.3-44 260.5C-44 403.7 47.9 495.7 191.1 495.7C220.6 495.7 248.5 488.3 273.6 474.7L373.3 574.4C377.6 578.7 384.5 578.7 388.9 574.4L504.4 459C508.8 454.7 508.8 447.8 505 442.7zM191.1 426.3C105.4 426.3 38.3 359.2 38.3 273.5C38.3 187.8 105.4 120.7 191.1 120.7C276.8 120.7 343.9 187.8 343.9 273.5C343.9 359.2 276.8 426.3 191.1 426.3z"></path>
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-gray-800 dark:text-white mb-2">Find Tournaments</h3>
            <p class="text-gray-600 dark:text-gray-300">Use our search tool to find and apply for tournaments that align with your qualifications and interests.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
            <!-- Add more content as needed -->
          </section>
  
          <section id="features" class="mb-6">
  <h2 class="text-2xl font-semibold mb-4">Features</h2>
  <p class="text-gray-700 mb-4">
    Learn about the features available in the application.
  </p>
  
  <div class="space-y-6">
    <div class="bg-gray-100 p-4 rounded-lg shadow-md">
      <h3 class="text-xl font-semibold mb-2">Locate Pool Areas</h3>
      <p class="text-gray-700">
        Easily find pool areas near you with our intuitive location feature. Whether you're looking for a local pool center to practice or a venue for a tournament, our app helps you discover nearby pool areas on an interactive map.
      </p>
      <ul class="list-disc pl-5 text-gray-700 mt-2">
        <li>View pool areas on a detailed map.</li>
        <li>Filter results by distance, amenities, and ratings.</li>
        <li>Get directions and contact information for each pool area.</li>
      </ul>
    </div>
    
    <div class="bg-gray-100 p-4 rounded-lg shadow-md">
      <h3 class="text-xl font-semibold mb-2">Tournament Enrollment</h3>
      <p class="text-gray-700">
        Sign up for exciting pool tournaments directly through the app. Stay updated on upcoming events, register for tournaments, and track your progress and results in one convenient place.
      </p>
      <ul class="list-disc pl-5 text-gray-700 mt-2">
        <li>Browse a list of upcoming tournaments.</li>
        <li>Register and pay for tournaments seamlessly.</li>
        <li>View tournament details, schedules, and results.</li>
      </ul>
    </div>
    
    <div class="bg-gray-100 p-4 rounded-lg shadow-md">
      <h3 class="text-xl font-semibold mb-2">Secure Payments</h3>
      <p class="text-gray-700">
        Our system ensures secure and straightforward payment processing for tournament entries and other services. Enjoy a hassle-free experience with reliable payment options and instant confirmation of transactions.
      </p>
      <ul class="list-disc pl-5 text-gray-700 mt-2">
        <li>Make payments using various secure methods.</li>
        <li>Receive instant payment confirmations.</li>
        <li>Track your payment history and receipts.</li>
      </ul>
    </div>
  </div>
</section>

  
          <section id="troubleshooting" class="mb-6">
  <h2 class="text-2xl font-semibold mb-4">Troubleshooting</h2>
  <p class="text-gray-700 mb-4">
    Common issues and their solutions.
  </p>
  
  <div class="space-y-4">
    <div class="bg-gray-100 p-4 rounded-lg shadow-md">
      <h3 class="text-xl font-semibold mb-2">Issue 1: Unable to Log In</h3>
      <p class="text-gray-700 mb-2">
        If you are unable to log in, please check the following:
      </p>
      <ul class="list-disc pl-5 text-gray-700">
        <li>Ensure that you are using the correct username and password.</li>
        <li>Try resetting your password using the "Forgot Password" link.</li>
        <li>Check if your account has been deactivated or suspended.</li>
        <li>Verify that your internet connection is stable.</li>
      </ul>
      <p class="text-gray-700 mt-2">
        If the problem persists, please contact support for further assistance.
      </p>
    </div>
    
    <div class="bg-gray-100 p-4 rounded-lg shadow-md">
      <h3 class="text-xl font-semibold mb-2">Issue 2: App Not Loading</h3>
      <p class="text-gray-700 mb-2">
        If the application is not loading, try the following solutions:
      </p>
      <ul class="list-disc pl-5 text-gray-700">
        <li>Clear your browser's cache and cookies.</li>
        <li>Ensure that you are using the latest version of the app.</li>
        <li>Restart your browser or app and try loading it again.</li>
        <li>Check for any known service outages or maintenance updates.</li>
      </ul>
      <p class="text-gray-700 mt-2">
        If the issue continues, please report the problem to our support team.
      </p>
    </div>
    
    <div class="bg-gray-100 p-4 rounded-lg shadow-md">
      <h3 class="text-xl font-semibold mb-2">Issue 3: Features Not Working</h3>
      <p class="text-gray-700 mb-2">
        If certain features are not functioning as expected, consider these steps:
      </p>
      <ul class="list-disc pl-5 text-gray-700">
        <li>Ensure that you have the necessary permissions or subscriptions for the feature.</li>
        <li>Check if there are any updates or patches available for the feature.</li>
        <li>Verify that the feature is enabled in your account settings.</li>
        <li>Try reloading the app or clearing any temporary data.</li>
      </ul>
      <p class="text-gray-700 mt-2">
        For further assistance, contact our customer support team.
      </p>
    </div>
    
    <div class="bg-gray-100 p-4 rounded-lg shadow-md">
      <h3 class="text-xl font-semibold mb-2">Issue 4: Error Messages</h3>
      <p class="text-gray-700 mb-2">
        If you encounter error messages, follow these steps to resolve them:
      </p>
      <ul class="list-disc pl-5 text-gray-700">
        <li>Read the error message carefully for specific instructions.</li>
        <li>Check the application logs for detailed error information.</li>
        <li>Search our help center or knowledge base for the error code or message.</li>
        <li>Restart the app and try the action again.</li>
      </ul>
      <p class="text-gray-700 mt-2">
        If you need additional help, please reach out to our support team with the error details.
      </p>
    </div>
  </div>
</section>

        </main>
  
      
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
  
  <script>
  export default {
    // Add your script logic here if needed
  }
  </script>
  
  <style scoped>
  /* Add additional styling if needed */
  </style>
  