import { Link, NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import { selectEnrolledCount } from '../store/enrollmentSlice';

function Header({ siteName = 'Student Portal' }) {
  const enrolledCount = useSelector(selectEnrolledCount);

  return (
    <header className="app-header">
      <div className="container header-inner">
        <Link to="/" className="brand">
          {siteName}
        </Link>

        <nav aria-label="Main navigation">
          <ul className="nav-links">
            <li>
              <NavLink to="/" end className={({ isActive }) => (isActive ? 'active' : '')}>
                Courses
              </NavLink>
            </li>
            <li>
              <NavLink to="/profile" className={({ isActive }) => (isActive ? 'active' : '')}>
                Profile ({enrolledCount})
              </NavLink>
            </li>
          </ul>
        </nav>
      </div>
    </header>
  );
}

export default Header;
