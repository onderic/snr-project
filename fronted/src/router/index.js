import { createRouter, createWebHistory } from 'vue-router'

import User from '@/layouts/user_layout.vue'
import Dashboard from '@/views/user_dashboard.vue'
import AddPool from "@/views/owner/AddPoool.vue"
import Login from '@/views/auth/login.vue'

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
          path: '/add-pool',
          name: 'addpool',
          component: AddPool
        },
        {
          path: "/auth/login",
          name: "login",
          component: Login,
        },
      ]
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
