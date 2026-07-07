import { defineStore } from 'pinia';
import { ref, computed } from 'vue';

/**
 * Enrollment store (Composition API "setup store" style — Hands-On 8,
 * Task 3). Holds the list of enrolled courses and exposes actions and
 * a computed total-credits value shared across every component that
 * uses this store.
 */
export const useEnrollmentStore = defineStore('enrollment', () => {
  const enrolledCourses = ref([]);

  const totalCredits = computed(() =>
    enrolledCourses.value.reduce((sum, c) => sum + (c.credits || 0), 0)
  );

  const isEnrolled = computed(
    () => (courseId) => enrolledCourses.value.some((c) => c.id === courseId)
  );

  function enroll(course) {
    if (!enrolledCourses.value.some((c) => c.id === course.id)) {
      enrolledCourses.value.push(course);
    }
  }

  function unenroll(courseId) {
    enrolledCourses.value = enrolledCourses.value.filter((c) => c.id !== courseId);
  }

  /**
   * Advanced Pinia pattern (Hands-On 10): an async action that calls
   * an API and updates state in a single action, so components don't
   * need to orchestrate the fetch + mutation themselves.
   */
  async function fetchAndEnroll(courseId, courseApi) {
    const course = await courseApi.getCourseById(courseId);
    enroll(course);
    return course;
  }

  function $reset() {
    enrolledCourses.value = [];
  }

  return {
    enrolledCourses,
    totalCredits,
    isEnrolled,
    enroll,
    unenroll,
    fetchAndEnroll,
    $reset,
  };
});
