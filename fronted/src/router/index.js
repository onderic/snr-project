import { createRouter, createWebHistory } from 'vue-router';
import User from '@/layouts/User.vue';
import Dash from '@/layouts/Dashboard.vue';
import Dashboard from '@/views/Dashboard.vue';
import Enroll from '@/views/Enrollment.vue';
import AddPool from "@/views/owner/pool/AddPoool.vue";
import Manage from "@/views/owner/events/ManageEvents.vue";
import ManagePool from "@/views/owner/pool/ManagePool.vue";
import EventDetail from "@/views/owner/events/EventDetail.vue";
import Login from '@/views/auth/login.vue';
import AdminPool from '@/views/Admin/Pools.vue';
import Owners from '@/views/Admin/Owners.vue';
import Events from '@/views/Admin/Events.vue';
import Register from '@/views/auth/register.vue';

import AdminDashboard from '@/views/Admin/Dashboard.vue';
import OwenrDashboard from '@/views/owner/Dashboard.vue';
import Home from '@/views/index.vue';
import Guide from '@/views/guide.vue';

import { useUserStore } from '@/stores/user'; 

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "",
      name: "/",
      component: Home
    },
    {
      path: "/guide",
      name: "guide",
      component: Guide
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
    {
      redirect: '/dashboard',
      component: User,
      meta: { requiresAuth: true },
      children: [
        {
          path: '/dashboard',
          name: 'dashboard',
          component: Dashboard,
          beforeEnter: (to, from, next) => {
            to.meta.currentComponent = 'Discover';
            next();
          },
        },
        {
          path: '/add-pool/location',
          name: 'addpool',
          component: AddPool
        },
        {
          path: "/manage-events",
          name: "manage-events",
          component: Manage
        },
        {
          path: '/event-detail/:id',
          name: "event-detail",
          component: EventDetail
        },
        {
          path: "/manage-pool",
          name: "manage-pool",
          component: ManagePool
        },
        {
          path: "/enrollment-list",
          name: "enrollment",
          component: Enroll
        },
        {
          path: "/owner-dashboard",
          name: "owenerDashboard",
          component: OwenrDashboard
        },


        // admin
        {
          path: "/admin-manage-pool",
          name: "adminPool",
          component: AdminPool
        },
        {
          path: "/admin-owners",
          name: "owners",
          component: Owners
        },
        {
          path: "/admin-manage-events",
          name: "events",
          component: Events
        },
        {
          path: "/admin-dashboard",
          name: "adminDashboard",
          component: AdminDashboard
        },
      ]
    },
  
  ]
});

router.beforeEach((to, from, next) => {
  const userStore = useUserStore();
  if (to.meta.requiresAuth) {
    const token = localStorage.getItem('user.access');
    if (!token) {
      next({ name: 'login', query: { to: to.path } });
    } else {
      if (!userStore.user.isAuthenticated) {
        userStore.initStore();
      }
      next();
    }
  } else {
    next();
  }
});

export default router;
