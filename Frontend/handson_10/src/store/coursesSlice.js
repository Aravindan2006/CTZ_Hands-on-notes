import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import { getAllCourses } from '../api/courseApi';

/**
 * Async thunk (Hands-On 10, Task 2, Step 143): wraps the API call so
 * components dispatch a plain action instead of calling the API
 * layer directly.
 */
export const fetchAllCourses = createAsyncThunk(
  'courses/fetchAll',
  async (_, { rejectWithValue }) => {
    try {
      return await getAllCourses();
    } catch (error) {
      // Normalise the error into a plain, serialisable payload for the
      // rejected action (Redux state must stay serialisable).
      return rejectWithValue({
        message: error.message,
        statusCode: error.statusCode ?? 0,
      });
    }
  }
);

const initialState = {
  items: [],
  loading: false,
  error: null,
};

const coursesSlice = createSlice({
  name: 'courses',
  initialState,
  reducers: {},
  // The three thunk lifecycle actions (Hands-On 10, Task 2, Step 144):
  extraReducers: (builder) => {
    builder
      .addCase(fetchAllCourses.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchAllCourses.fulfilled, (state, action) => {
        state.loading = false;
        state.items = action.payload;
      })
      .addCase(fetchAllCourses.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload?.message || action.error.message || 'Failed to load courses';
      });
  },
});

export default coursesSlice.reducer;

// -----------------------------------------------------------------
// Selectors (Hands-On 10, Task 2, Step 146): components read state
// through these functions, never by reaching into `state.courses...`
// directly, so the store shape can change without touching consumers.
// -----------------------------------------------------------------
export const selectCourses = (state) => state.courses.items;
export const selectCoursesLoading = (state) => state.courses.loading;
export const selectCoursesError = (state) => state.courses.error;
export const selectCourseById = (id) => (state) =>
  state.courses.items.find((c) => c.id === Number(id));
