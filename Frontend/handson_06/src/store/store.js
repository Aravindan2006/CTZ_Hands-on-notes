import { configureStore } from '@reduxjs/toolkit';
import enrollmentReducer from './enrollmentSlice';

// configureStore (Hands-On 6, Task 3, Step 86) sets up the Redux
// store with good defaults (Redux DevTools support, thunk middleware)
// with a single call, instead of the manual createStore + middleware
// wiring required by classic Redux.
export const store = configureStore({
  reducer: {
    enrollment: enrollmentReducer,
  },
});

export default store;
