<script setup>
import { RouterLink } from 'vue-router';
</script>

<template>
  <section class="hero">
    <h1>Welcome to the Student Portal</h1>
    <p>Browse your courses, manage your profile, and track your enrollments — all in one place.</p>
    <RouterLink to="/courses" class="btn btn-primary">Explore Courses</RouterLink>
  </section>

  <section class="stats-bar" aria-label="Student statistics">
    <div class="stat-item">
      <span class="stat-value">3</span>
      <span class="stat-label">Courses Enrolled</span>
    </div>
    <div class="stat-item">
      <span class="stat-value">3.8</span>
      <span class="stat-label">GPA</span>
    </div>
    <div class="stat-item">
      <span class="stat-value">6</span>
      <span class="stat-label">Semester</span>
    </div>
  </section>
</template>

<style scoped>
.hero {
  text-align: center;
  padding: 3rem 1rem;
  min-height: 30vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 1rem;
}

.hero h1 {
  font-size: clamp(1.75rem, 4vw, 2.5rem);
}

.hero p {
  color: var(--color-muted);
  max-width: 40ch;
}

.stats-bar {
  display: flex;
  justify-content: center;
  gap: 2.5rem;
  flex-wrap: wrap;
  padding: 1.5rem 0 3rem;
}

.stat-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  min-width: 120px;
}

.stat-value {
  font-size: 1.75rem;
  font-weight: 700;
  color: var(--color-primary);
}

.stat-label {
  color: var(--color-muted);
  font-size: 0.9rem;
}
</style>
