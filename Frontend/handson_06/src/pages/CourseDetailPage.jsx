import { useParams, useNavigate, Link } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { courses } from '../data/courses';
import { enroll, selectIsEnrolled } from '../store/enrollmentSlice';

// Task 1, Step 79: useParams() reads :courseId from the URL.
function CourseDetailPage() {
  const { courseId } = useParams();
  const navigate = useNavigate();
  const dispatch = useDispatch();

  const course = courses.find((c) => c.id === Number(courseId));
  const isEnrolled = useSelector(selectIsEnrolled(Number(courseId)));

  if (!course) {
    return (
      <section>
        <Link to="/courses" className="btn btn-outline">&larr; Back to courses</Link>
        <p>Sorry, we couldn't find that course.</p>
      </section>
    );
  }

  // Task 1, Step 80: useNavigate() redirects to /profile after enrolling.
  const handleEnroll = () => {
    dispatch(enroll(course));
    navigate('/profile');
  };

  return (
    <section aria-labelledby="detail-heading">
      <Link to="/courses" className="btn btn-outline back-link">&larr; Back to courses</Link>
      <div className="detail-card">
        <h1 id="detail-heading">{course.name}</h1>
        <p className="course-code">{course.code} &middot; {course.credits} credits</p>
        <p>{course.description}</p>
        <button className="btn btn-primary" onClick={handleEnroll} disabled={isEnrolled}>
          {isEnrolled ? 'Enrolled ✓' : 'Enroll'}
        </button>
      </div>
    </section>
  );
}

export default CourseDetailPage;
