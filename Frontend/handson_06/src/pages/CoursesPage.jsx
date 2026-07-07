import { useNavigate } from 'react-router-dom';
import { courses } from '../data/courses';
import CourseCard from '../components/CourseCard';

// Task 1, Steps 77-79: this page is rendered at the /courses route.
function CoursesPage() {
  const navigate = useNavigate();

  return (
    <section aria-labelledby="courses-heading">
      <h1 id="courses-heading">Browse Courses</h1>
      <div className="course-grid">
        {courses.map((course) => (
          <CourseCard key={course.id} {...course} onSelect={(id) => navigate(`/courses/${id}`)} />
        ))}
      </div>
    </section>
  );
}

export default CoursesPage;
