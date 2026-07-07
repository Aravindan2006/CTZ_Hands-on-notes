// Task 1, Step 62-64: functional component receiving props.
function Header({ siteName, enrolledCount = 0 }) {
  return (
    <header className="app-header">
      <p className="brand">{siteName}</p>
      <nav aria-label="Main navigation">
        <ul className="nav-links">
          <li>Home</li>
          <li>Courses</li>
          <li>Profile ({enrolledCount})</li>
        </ul>
      </nav>
    </header>
  );
}

export default Header;
