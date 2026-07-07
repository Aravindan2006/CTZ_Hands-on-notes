<script setup>
import { computed, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { courses } from '../data/courses';
import { useEnrollmentStore } from '../stores/enrollment';

const route = useRoute();
const router = useRouter();
const enrollment = useEnrollmentStore();

const courseId = computed(() => Number(route.params.id));
const course = computed(() => courses.find((c) => c.id === courseId.value));

const justEnrolled = ref(false);

function handleEnroll() {
  if (!course.value) return;
  enrollment.enroll(course.value);
  justEnrolled.value = true;
  // Programmatic navigation to profile after enrolling (Hands-On 8, Task 2).
  setTimeout(() => router.push('/profile'), 600);
}
</script>

<template>
  <section aria-labelledby="detail-heading">
    <RouterLink to="/courses" class="btn btn-outline back-link">&larr; Back to courses</RouterLink>

    <div v-if="course" class="card detail-card">
      <h1 id="detail-heading">{{ course.name }}</h1>
      <p class="course-code">{{ course.code }} &middot; {{ course.credits }} credits</p>
      <p>{{ course.description }}</p>
      <p v-if="course.grade">Current grade: <strong>{{ course.grade }}</strong></p>

      <button
        class="btn btn-primary"
        :disabled="enrollment.isEnrolled(course.id)"
        @click="handleEnroll"
      >
        {{ enrollment.isEnrolled(course.id) ? 'Enrolled ✓ redirecting…' : 'Enroll' }}
      </button>
    </div>

    <p v-else>Sorry, we couldn't find that course.</p>
  </section>
</template>

<style scoped>
.back-link {
  display: inline-flex;
  margin-bottom: 1.5rem;
  text-decoration: none;
}

.detail-card {
  max-width: 560px;
}

.course-code {
  color: var(--color-muted);
  margin-bottom: 1rem;
}
</style>
