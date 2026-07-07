<script setup>
import { reactive } from 'vue';
import { storeToRefs } from 'pinia';
import { useEnrollmentStore } from '../stores/enrollment';

const enrollment = useEnrollmentStore();
// storeToRefs keeps reactivity when destructuring store state/getters
// (plain destructuring would break reactivity) — Hands-On 8/10 pattern.
const { enrolledCourses, totalCredits } = storeToRefs(enrollment);

const profile = reactive({
  name: '',
  email: '',
  semester: 1,
});

function unenroll(courseId) {
  enrollment.unenroll(courseId);
}
</script>

<template>
  <section aria-labelledby="profile-heading">
    <h1 id="profile-heading">My Profile</h1>

    <form class="card profile-form" @submit.prevent>
      <div class="form-field">
        <label for="name">Full name</label>
        <input id="name" type="text" v-model="profile.name" />
      </div>
      <div class="form-field">
        <label for="email">Email</label>
        <input id="email" type="email" v-model="profile.email" />
      </div>
      <div class="form-field">
        <label for="semester">Semester</label>
        <input id="semester" type="number" min="1" max="8" v-model.number="profile.semester" />
      </div>
    </form>

    <h2>Enrolled Courses</h2>
    <p class="total-credits">Total credits: <strong>{{ totalCredits }}</strong></p>

    <ul class="enrolled-list" v-if="enrolledCourses.length">
      <li v-for="course in enrolledCourses" :key="course.id" class="card enrolled-item">
        <div>
          <strong>{{ course.name }}</strong>
          <span class="course-code"> &middot; {{ course.code }} &middot; {{ course.credits }} credits</span>
        </div>
        <button class="btn btn-outline" @click="unenroll(course.id)">Remove</button>
      </li>
    </ul>
    <p v-else>You haven't enrolled in any courses yet.</p>
  </section>
</template>

<style scoped>
.profile-form {
  max-width: 480px;
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
  margin-bottom: 2rem;
}

.form-field {
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
}

.form-field label {
  font-weight: 600;
  font-size: 0.9rem;
}

.form-field input {
  padding: 0.6rem 0.8rem;
  border: 1px solid var(--color-border);
  border-radius: var(--radius);
  font-size: 1rem;
}

.total-credits {
  color: var(--color-muted);
  margin-bottom: 1rem;
}

.enrolled-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.enrolled-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}

.course-code {
  color: var(--color-muted);
  font-size: 0.9rem;
}
</style>
