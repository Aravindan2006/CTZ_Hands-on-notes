<script setup>
import { ref, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import CourseCard from '../components/CourseCard.vue';
import { courses as sampleCourses } from '../data/courses';
import { useEnrollmentStore } from '../stores/enrollment';

const router = useRouter();
const enrollment = useEnrollmentStore();

const courses = ref([]);
const searchTerm = ref('');
const loading = ref(true);

onMounted(() => {
  // Simulate an async data load so the loading state has something to show.
  setTimeout(() => {
    courses.value = sampleCourses;
    loading.value = false;
  }, 400);
});

// computed() is cached and only re-evaluates when courses or
// searchTerm change (Hands-On 8, Task 1).
const filteredCourses = computed(() => {
  const term = searchTerm.value.trim().toLowerCase();
  if (!term) return courses.value;
  return courses.value.filter((c) => c.name.toLowerCase().includes(term));
});

function goToDetail(id) {
  router.push(`/courses/${id}`);
}

function handleEnroll(course) {
  enrollment.enroll(course);
}
</script>

<template>
  <section aria-labelledby="courses-heading">
    <h1 id="courses-heading">Browse Courses</h1>

    <div class="search-row">
      <label for="search-courses" class="visually-hidden">Search courses</label>
      <input id="search-courses" type="text" v-model="searchTerm" placeholder="Search courses..." />
      <p class="results-count" role="status" aria-live="polite">
        {{ filteredCourses.length }} course{{ filteredCourses.length === 1 ? '' : 's' }} found
      </p>
    </div>

    <p v-if="loading">Loading courses...</p>

    <div class="course-grid" v-else>
      <div v-for="course in filteredCourses" :key="course.id" class="card-wrapper">
        <CourseCard
          :id="course.id"
          :name="course.name"
          :code="course.code"
          :credits="course.credits"
          :grade="course.grade"
          @select="goToDetail"
        />
        <button
          class="btn btn-primary enroll-btn"
          :disabled="enrollment.isEnrolled(course.id)"
          @click="handleEnroll(course)"
        >
          {{ enrollment.isEnrolled(course.id) ? 'Enrolled ✓' : 'Enroll' }}
        </button>
      </div>
    </div>

    <p v-if="!loading && filteredCourses.length === 0">No courses found.</p>
  </section>
</template>

<style scoped>
.search-row {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex-wrap: wrap;
  margin-bottom: 1.5rem;
}

.search-row input {
  flex: 1;
  min-width: 220px;
  padding: 0.65rem 0.9rem;
  border: 1px solid var(--color-border);
  border-radius: var(--radius);
  font-size: 1rem;
}

.results-count {
  color: var(--color-muted);
  font-size: 0.9rem;
  margin: 0;
}

.card-wrapper {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.enroll-btn {
  align-self: flex-start;
}
</style>
