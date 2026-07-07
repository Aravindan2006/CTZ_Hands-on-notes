import { useState, useEffect } from 'react';
import Header from './components/Header';
import Footer from './components/Footer';
import CourseCard from './components/CourseCard';
import StudentProfile from './components/StudentProfile';
import { courses as fallbackCourses } from './data/courses';

function App() {
  // Task 2, Step 66: state for the course list.
  const [courses, setCourses] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [enrolledCourses, setEnrolledCourses] = useState([]);

  // Task 3, Steps 71-73: fetch on mount, with loading + error state.
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    let isMounted = true;

    async function loadCourses() {
      setLoading(true);
      setError(null);
      try {
        const response = await fetch('https://jsonplaceholder.typicode.com/posts?_limit=5');
        if (!response.ok) {
          throw new Error(`Request failed with status ${response.status}`);
        }
        const posts = await response.json();

        // Map the 5 posts onto course-like objects, enriched with our
        // local sample fields (code, credits, grade) by index.
        const mapped = posts.map((post, index) => ({
          ...fallbackCourses[index % fallbackCourses.length],
          id: post.id,
        }));

        if (isMounted) setCourses(mapped);
      } catch (err) {
        if (isMounted) setError('Unable to load courses right now. Please try again later.');
        console.error(err);
      } finally {
        if (isMounted) setLoading(false);
      }
    }

    loadCourses();
    return () => {
      isMounted = false;
    };
  }, []); // empty dependency array: run once after mount (like componentDidMount).
  // A missing dependency array here would re-run this effect after every
  // render; since the effect itself sets state, that would cause an
  // infinite fetch loop.

  useEffect(() => {
    console.log('Courses updated:', courses.length);
  }, [courses]);

  const filteredCourses = courses.filter((c) =>
    c.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  // Task 2, Step 69: lift enroll state up to the closest common ancestor.
  const handleEnroll = (course) => {
    setEnrolledCourses((prev) =>
      prev.some((c) => c.id === course.id) ? prev : [...prev, course]
    );
  };

  return (
    <>
      <Header siteName="Student Portal" enrolledCount={enrolledCourses.length} />

      <main className="container">
        <section className="courses-section">
          <h1>Your Courses</h1>

          <input
            type="text"
            className="search-input"
            placeholder="Search courses..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            aria-label="Search courses"
          />

          {loading && <p>Loading...</p>}
          {error && !loading && <p className="error-banner">{error}</p>}

          {!loading && !error && (
            <div className="course-grid">
              {filteredCourses.map((course) => (
                <CourseCard
                  key={course.id}
                  {...course}
                  enrolled={enrolledCourses.some((c) => c.id === course.id)}
                  onEnroll={() => handleEnroll(course)}
                />
              ))}
            </div>
          )}
        </section>

        <StudentProfile />
      </main>

      <Footer />
    </>
  );
}

export default App;
