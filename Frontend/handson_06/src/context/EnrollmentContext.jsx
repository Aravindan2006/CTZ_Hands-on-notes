import { createContext, useContext, useState } from 'react';

/**
 * Hands-On 6, Task 2: Context API for global state.
 *
 * NOTE: This context is superseded by Redux Toolkit in Task 3
 * (see ../store/enrollmentSlice.js) — the running app wires up Redux
 * instead of this Provider. This file is kept to demonstrate the
 * Context API pattern the exercise book asks for in Task 2, and to
 * show the "before" state that Task 3 refactors away from.
 *
 * To use this instead of Redux: wrap <App /> in <EnrollmentProvider>
 * in main.jsx, and call useEnrollment() in any component that needs
 * enrolledCourses instead of useSelector/useDispatch.
 */
const EnrollmentContext = createContext(null);

export function EnrollmentProvider({ children }) {
  const [enrolledCourses, setEnrolledCourses] = useState([]);

  function enroll(course) {
    setEnrolledCourses((prev) =>
      prev.some((c) => c.id === course.id) ? prev : [...prev, course]
    );
  }

  function unenroll(courseId) {
    setEnrolledCourses((prev) => prev.filter((c) => c.id !== courseId));
  }

  const value = { enrolledCourses, enroll, unenroll };

  return <EnrollmentContext.Provider value={value}>{children}</EnrollmentContext.Provider>;
}

export function useEnrollment() {
  const context = useContext(EnrollmentContext);
  if (!context) {
    throw new Error('useEnrollment must be used within an EnrollmentProvider');
  }
  return context;
}
