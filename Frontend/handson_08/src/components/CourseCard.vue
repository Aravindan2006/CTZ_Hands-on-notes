<script setup>
defineProps({
  id: { type: Number, required: true },
  name: { type: String, required: true },
  code: { type: String, required: true },
  credits: { type: Number, required: true },
  grade: { type: String, default: '' },
});

const emit = defineEmits(['select']);
</script>

<template>
  <article
    class="card course-card"
    tabindex="0"
    role="button"
    :aria-label="`${name}, ${credits} credits`"
    @click="emit('select', id)"
    @keydown.enter.space.prevent="emit('select', id)"
  >
    <h3>{{ name }}</h3>
    <p class="course-code">{{ code }}</p>
    <p class="course-credits"><strong>{{ credits }}</strong> credits</p>
    <p class="course-grade" v-if="grade">Grade: <strong>{{ grade }}</strong></p>
  </article>
</template>

<style scoped>
.course-card {
  cursor: pointer;
  transition: transform 0.12s ease, box-shadow 0.12s ease;
}

.course-card:hover,
.course-card:focus-visible {
  transform: translateY(-3px);
  box-shadow: 0 6px 18px rgba(20, 30, 60, 0.14);
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}

.course-code {
  color: var(--color-muted);
  font-size: 0.85rem;
  margin-bottom: 0.5rem;
}

.course-credits {
  font-size: 0.9rem;
  color: var(--color-muted);
}

.course-grade {
  margin-top: 0.5rem;
  font-size: 0.9rem;
}
</style>
