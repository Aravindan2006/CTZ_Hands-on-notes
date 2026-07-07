import { useDispatch, useSelector } from 'react-redux';
import { selectEnrolledCourses, unenroll } from '../store/enrollmentSlice';

// Task 3, Step 89: reads enrolled courses via useSelector, no props
// passed in from CoursesPage or CourseDetailPage — pure global state.
function ProfilePage() {
  const dispatch = useDispatch();
  const enrolledCourses = useSelector(selectEnrolledCourses);

  return (
    <section aria-labelledby="profile-heading">
      <h1 id="profile-heading">My Profile</h1>
      <h2>Enrolled Courses</h2>

      {enrolledCourses.length === 0 ? (
        <p>You haven't enrolled in any courses yet.</p>
      ) : (
        <ul className="enrolled-list">
          {enrolledCourses.map((course) => (
            <li key={course.id} className="enrolled-item">
              <span>{course.name} &middot; {course.code}</span>
              {/* Task 2/3, "Remove" un-enroll action */}
              <button className="btn btn-outline" onClick={() => dispatch(unenroll(course.id))}>
                Remove
              </button>
            </li>
          ))}
        </ul>
      )}
    </section>
  );
}

export default ProfilePage;
