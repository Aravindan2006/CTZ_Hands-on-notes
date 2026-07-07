import { Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import ErrorBoundary from './components/ErrorBoundary';
import CoursesPage from './pages/CoursesPage';
import CourseDetailPage from './pages/CourseDetailPage';
import ProfilePage from './pages/ProfilePage';

function App() {
  return (
    <>
      <Header siteName="Student Portal" />

      <main className="container page-main">
        <ErrorBoundary>
          <Routes>
            <Route path="/" element={<CoursesPage />} />
            <Route path="/courses/:courseId" element={<CourseDetailPage />} />
            <Route path="/profile" element={<ProfilePage />} />
          </Routes>
        </ErrorBoundary>
      </main>

      <footer className="site-footer">
        <div className="container">
          <p>&copy; 2026 Student Portal. Built with React + Redux Toolkit for Digital Nurture 5.0.</p>
        </div>
      </footer>
    </>
  );
}

export default App;
