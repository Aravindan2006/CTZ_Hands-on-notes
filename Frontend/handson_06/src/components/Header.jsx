import { Link, NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import { selectEnrolledCount } from '../store/enrollmentSlice';

// Task 1, Step 78: nav links use <Link>/<NavLink> instead of <a> tags,
// so navigation is client-side (no full page reload).
function Header() {
  const enrolledCount = useSelector(selectEnrolledCount);

  return (
    <header className="app-header">
      <Link to="/" className="brand">Student Portal</Link>
      <nav aria-label="Main navigation">
        <ul className="nav-links">
          <li><NavLink to="/" end className={({ isActive }) => (isActive ? 'active' : '')}>Home</NavLink></li>
          <li><NavLink to="/courses" className={({ isActive }) => (isActive ? 'active' : '')}>Courses</NavLink></li>
          {/* Task 3, Step 89: read enrolled count via useSelector — no props passed from CoursesPage. */}
          <li><NavLink to="/profile" className={({ isActive }) => (isActive ? 'active' : '')}>Profile ({enrolledCount})</NavLink></li>
        </ul>
      </nav>
    </header>
  );
}

export default Header;
