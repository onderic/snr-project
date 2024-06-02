import { createRouter, createWebHistory } from 'vue-router'

import User from '@/layouts/User.vue'
import Dashboard from '@/views/Dashboard.vue'
import AddPool from "@/views/owner/pool/AddPoool.vue"


// events
import Manage from "@/views/owner/events/ManageEvents.vue"
import ManagePool from "@/views/owner/pool/ManagePool.vue"
import EventDetail from "@/views/owner/events/EventDetail.vue"


import Login from '@/views/auth/login.vue'
import Register from '@/views/auth/register.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '',
      redirect: '/dashboard',
      component: User,
      meta: { requiresAuth: true },
      children: [
        {
          path: '/dashboard',
          name: 'dashboard',
          component: Dashboard
        },
        {
          path: '/add-pool/location',
          name: 'addpool',
          component: AddPool
        },

        // events
        {
          path:"/manage-events",
          name: "manage-events",
          component: Manage

        },
        {
          path:"/event-detail",
          name: "event-detail",
          component: EventDetail

        },

        // pools
        {
          path:"/manage-pool",
          name: "manage-pool",
          component: ManagePool

        },



      
      ]
    },

    {
      path: "/auth/login",
      name: "login",
      component: Login,
    },
    {
      path: "/auth/register",
      name: "register",
      component: Register,
    },
    

    // {
    //   path: "/auth/register",
    //   name: "register",
    //   component: Register,
    // },

    // {
    //   path: "/terms-conditions",
    //   name: "terms",
    //   component: Terms,
    // },
    // {
    //   path: "/auth/login",
    //   name: "login",
    //   component: Login,
    // },
    // {
    //   path: '/auth/invite',
    //   name: 'invite',
    //   component: Referral,
    //   props: route => ({ referralCode: route.query.ref, invest: route.query.invest })
    // },
  ]
})

// router.beforeEach((to, from, next) => {
//   if (to.meta.requiresAuth) {
//     const token = localStorage.getItem('accessToken');
//     if (!token) {
//       next({ name: 'login', query: { to: to.path } });
//     } else {

//       next();
//     }
//   } else {
//     next();
//   }
// });

export default router
