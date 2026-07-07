import { createSlice } from '@reduxjs/toolkit';

/**
 * Hands-On 6, Task 3: Redux Toolkit enrollment slice.
 *
 * This replaces the Context-based state from Task 2
 * (../context/EnrollmentContext.jsx) with the modern, recommended
 * Redux approach — createSlice eliminates action-type-constant and
 * switch-statement reducer boilerplate, and uses Immer internally so
 * we can write "mutating" code like `state.enrolledCourses.push(...)`
 * that is actually applied immutably under the hood.
 */
const enrollmentSlice = createSlice({
  name: 'enrollment',
  initialState: {
    enrolledCourses: [],
  },
  reducers: {
    enroll(state, action) {
      const course = action.payload;
      const alreadyEnrolled = state.enrolledCourses.some((c) => c.id === course.id);
      if (!alreadyEnrolled) {
        state.enrolledCourses.push(course);
      }
    },
    unenroll(state, action) {
      const courseId = action.payload;
      state.enrolledCourses = state.enrolledCourses.filter((c) => c.id !== courseId);
    },
  },
});

export const { enroll, unenroll } = enrollmentSlice.actions;
export default enrollmentSlice.reducer;

// Selectors — components read state through these, not by reaching
// into `state.enrollment...` shape directly.
export const selectEnrolledCourses = (state) => state.enrollment.enrolledCourses;
export const selectEnrolledCount = (state) => state.enrollment.enrolledCourses.length;
export const selectIsEnrolled = (courseId) => (state) =>
  state.enrollment.enrolledCourses.some((c) => c.id === courseId);
