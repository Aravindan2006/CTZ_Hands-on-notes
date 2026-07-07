<script setup>
import Header from './components/Header.vue';
</script>

<template>
  <Header site-name="Student Portal" />

  <main class="container page-main">
    <RouterView />
  </main>

  <footer class="site-footer">
    <div class="container">
      <p>&copy; 2026 Student Portal. Built with Vue 3 for Digital Nurture 5.0.</p>
    </div>
  </footer>
</template>

<style scoped>
.page-main {
  min-height: 60vh;
  padding-top: 2rem;
  padding-bottom: 2rem;
}

.site-footer {
  margin-top: 3rem;
  padding: 1.5rem 0;
  background: var(--color-surface);
  border-top: 1px solid var(--color-border);
  color: var(--color-muted);
  font-size: 0.9rem;
  text-align: center;
}
</style>
