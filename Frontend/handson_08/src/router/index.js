import { createRouter, createWebHistory } from 'vue-router';

import HomeView from '../views/HomeView.vue';
import CoursesView from '../views/CoursesView.vue';
import CourseDetailView from '../views/CourseDetailView.vue';
import ProfileView from '../views/ProfileView.vue';

const routes = [
  { path: '/', name: 'home', component: HomeView },
  { path: '/courses', name: 'courses', component: CoursesView },
  { path: '/courses/:id', name: 'course-detail', component: CourseDetailView, props: true },
  { path: '/profile', name: 'profile', component: ProfileView },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior() {
    return { top: 0 };
  },
});

// Navigation guard (Hands-On 8, Task 2): logs every route change.
router.beforeEach((to, from) => {
  console.log(`Navigating to: ${to.path}`);
  return true;
});

export default router;
