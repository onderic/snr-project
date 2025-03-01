import { defineStore } from 'pinia';

export const useUserStore = defineStore({
  id: 'user',

  state: () => ({
    user: {
      isAuthenticated: false,
      id: null,
      role: null,
      name: null,
      access: null,
      refresh: null,
    },
  }),

  actions: {
    initStore() {
      if (localStorage.getItem('user.access')) {
        this.user.access = localStorage.getItem('user.access');
        this.user.refresh = localStorage.getItem('user.refresh');
        this.user.id = localStorage.getItem('user.id');
        this.user.role = localStorage.getItem('user.role');
        this.user.name = localStorage.getItem('user.name');
        this.user.isAuthenticated = true;

        // this.refreshToken();
      }
    },

    setToken(data) {
      this.user.access = data.access;
      this.user.refresh = data.refresh;
      this.user.isAuthenticated = true;

      localStorage.setItem('user.access', data.access);
      localStorage.setItem('user.refresh', data.refresh);
    },

    removeToken() {
      this.user.refresh = null;
      this.user.access = null;
      this.user.isAuthenticated = false;
      this.user.id = null;
      this.user.role = null;
      this.user.name = null;

      localStorage.removeItem('user.access');
      localStorage.removeItem('user.refresh');
      localStorage.removeItem('user.id');
      localStorage.removeItem('user.role');
      localStorage.removeItem('user.name');
    },

    setUserInfo(user) {
      this.user.id = user.id;
      this.user.role = user.role;
      this.user.name = user.name;

      localStorage.setItem('user.id', this.user.id);
      localStorage.setItem('user.role', this.user.role);
      localStorage.setItem('user.name', this.user.name);
    },

    updateUserRole(role) {
      this.user.role = role;
      localStorage.setItem('user.role', role);
    },

    // refreshToken() {
    //   axios
    //     .post('/api/v1/refresh/', {
    //       refresh: this.user.refresh,
    //     })
    //     .then(response => {
    //       this.user.access = response.data.access;

    //       localStorage.setItem('user.access', response.data.access);

    //       axios.defaults.headers.common['Authorization'] = 'Bearer ' + response.data.access;
    //     })
    //     .catch(error => {

    //       this.removeToken();
    //     });
    // },
  },
});
