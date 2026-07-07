import { Link } from 'react-router-dom';

function HomePage() {
  return (
    <section className="hero">
      <h1>Welcome to the Student Portal</h1>
      <p>Browse your courses, manage your profile, and track enrollments.</p>
      <Link to="/courses" className="btn btn-primary">Explore Courses</Link>
    </section>
  );
}

export default HomePage;
