import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  enrolledCourses: [],
};

const enrollmentSlice = createSlice({
  name: 'enrollment',
  initialState,
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

// Selectors
export const selectEnrolledCourses = (state) => state.enrollment.enrolledCourses;
export const selectEnrolledCount = (state) => state.enrollment.enrolledCourses.length;
export const selectTotalCredits = (state) =>
  state.enrollment.enrolledCourses.reduce((sum, c) => sum + (c.credits || 0), 0);
export const selectIsEnrolled = (courseId) => (state) =>
  state.enrollment.enrolledCourses.some((c) => c.id === courseId);
