import { useEffect, useState } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';

import LoadingSpinner from '../components/LoadingSpinner';
import { selectCourseById, selectCourses } from '../store/coursesSlice';
import { enroll, selectIsEnrolled } from '../store/enrollmentSlice';

function CourseDetailPage() {
  const { courseId } = useParams();
  const navigate = useNavigate();
  const dispatch = useDispatch();

  const courses = useSelector(selectCourses);
  const course = useSelector(selectCourseById(courseId));
  const isEnrolled = useSelector(selectIsEnrolled(Number(courseId)));

  const [justEnrolled, setJustEnrolled] = useState(false);

  // If the user navigates straight to /courses/:id (e.g. a page
  // refresh) before the course list has loaded, show a brief loading
  // state instead of an immediate "not found".
  const stillLoadingCourses = courses.length === 0;

  useEffect(() => {
    if (justEnrolled) {
      const timer = setTimeout(() => navigate('/profile'), 600);
      return () => clearTimeout(timer);
    }
  }, [justEnrolled, navigate]);

  const handleEnroll = () => {
    if (!course) return;
    dispatch(enroll(course));
    setJustEnrolled(true);
  };

  if (stillLoadingCourses) {
    return <LoadingSpinner message="Loading course details..." />;
  }

  if (!course) {
    return (
      <section>
        <Link to="/" className="btn btn-outline back-link">
          &larr; Back to courses
        </Link>
        <p>Sorry, we couldn't find that course.</p>
      </section>
    );
  }

  return (
    <section aria-labelledby="detail-heading">
      <Link to="/" className="btn btn-outline back-link">
        &larr; Back to courses
      </Link>

      <div className="detail-card">
        <h1 id="detail-heading">{course.name}</h1>
        <p className="course-code">
          {course.code} &middot; {course.credits} credits
        </p>
        <p>{course.description}</p>
        {course.grade && (
          <p>
            Current grade: <strong>{course.grade}</strong>
          </p>
        )}

        <button className="btn btn-primary" onClick={handleEnroll} disabled={isEnrolled}>
          {isEnrolled ? 'Enrolled ✓ redirecting…' : 'Enroll'}
        </button>
      </div>
    </section>
  );
}

export default CourseDetailPage;
