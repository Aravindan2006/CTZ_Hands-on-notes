<script setup>
import { useEnrollmentStore } from '../stores/enrollment';

defineProps({
  siteName: {
    type: String,
    default: 'Student Portal',
  },
});

const enrollment = useEnrollmentStore();
</script>

<template>
  <header class="app-header">
    <div class="container header-inner">
      <RouterLink to="/" class="brand">{{ siteName }}</RouterLink>

      <nav aria-label="Main navigation">
        <ul class="nav-links">
          <li><RouterLink to="/" exact-active-class="active">Home</RouterLink></li>
          <li><RouterLink to="/courses" active-class="active">Courses</RouterLink></li>
          <li><RouterLink to="/profile" active-class="active">Profile ({{ enrollment.enrolledCourses.length }})</RouterLink></li>
        </ul>
      </nav>
    </div>
  </header>
</template>

<style scoped>
.app-header {
  background: var(--color-surface);
  border-bottom: 1px solid var(--color-border);
  box-shadow: var(--shadow);
}

.header-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem 0;
}

.brand {
  font-weight: 700;
  font-size: 1.25rem;
  text-decoration: none;
  color: var(--color-text);
}

.nav-links {
  list-style: none;
  display: flex;
  gap: 1.5rem;
  margin: 0;
  padding: 0;
}

.nav-links a {
  text-decoration: none;
  color: var(--color-muted);
  font-weight: 500;
  padding-bottom: 2px;
  border-bottom: 2px solid transparent;
}

.nav-links a:hover,
.nav-links a.active {
  color: var(--color-primary);
  border-bottom-color: var(--color-primary);
}

@media (max-width: 480px) {
  .header-inner {
    flex-direction: column;
    gap: 0.75rem;
    align-items: flex-start;
  }
}
</style>
