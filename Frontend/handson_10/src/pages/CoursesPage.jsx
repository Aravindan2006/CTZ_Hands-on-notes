import { useEffect, useMemo, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useNavigate } from 'react-router-dom';

import CourseCard from '../components/CourseCard';
import LoadingSpinner from '../components/LoadingSpinner';
import { fetchAllCourses, selectCourses, selectCoursesLoading, selectCoursesError } from '../store/coursesSlice';
import { enroll, selectIsEnrolled } from '../store/enrollmentSlice';

function CoursesPage() {
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const courses = useSelector(selectCourses);
  const loading = useSelector(selectCoursesLoading);
  const error = useSelector(selectCoursesError);

  const [searchTerm, setSearchTerm] = useState('');

  // Dispatch the thunk on mount; the component never calls the API
  // directly (Hands-On 10, Task 2, Step 145).
  useEffect(() => {
    dispatch(fetchAllCourses());
  }, [dispatch]);

  const filteredCourses = useMemo(() => {
    const term = searchTerm.trim().toLowerCase();
    if (!term) return courses;
    return courses.filter((c) => c.name.toLowerCase().includes(term));
  }, [courses, searchTerm]);

  const handleSelect = (id) => {
    navigate(`/courses/${id}`);
  };

  const handleRetry = () => {
    dispatch(fetchAllCourses());
  };

  return (
    <section aria-labelledby="courses-heading">
      <h1 id="courses-heading">Browse Courses</h1>

      <div className="search-row">
        <label htmlFor="search-courses" className="visually-hidden">
          Search courses
        </label>
        <input
          id="search-courses"
          type="text"
          placeholder="Search courses..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />
        <p className="results-count" role="status" aria-live="polite">
          {filteredCourses.length} course{filteredCourses.length === 1 ? '' : 's'} found
        </p>
      </div>

      {loading && <LoadingSpinner message="Loading courses..." />}

      {!loading && error && (
        <div className="error-banner">
          <p>{error}</p>
          <button className="btn btn-outline" onClick={handleRetry}>
            Retry
          </button>
        </div>
      )}

      {!loading && !error && (
        <div className="course-grid">
          {filteredCourses.map((course) => (
            <CourseCardWithEnroll key={course.id} course={course} onSelect={handleSelect} />
          ))}
        </div>
      )}

      {!loading && !error && filteredCourses.length === 0 && <p>No courses found.</p>}
    </section>
  );
}

function CourseCardWithEnroll({ course, onSelect }) {
  const dispatch = useDispatch();
  const isEnrolled = useSelector(selectIsEnrolled(course.id));

  return (
    <div className="card-wrapper">
      <CourseCard {...course} onSelect={onSelect} />
      <button
        className="btn btn-primary enroll-btn"
        disabled={isEnrolled}
        onClick={() => dispatch(enroll(course))}
      >
        {isEnrolled ? 'Enrolled ✓' : 'Enroll'}
      </button>
    </div>
  );
}

export default CoursesPage;
