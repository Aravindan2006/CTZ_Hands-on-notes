import { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { selectEnrolledCourses, selectTotalCredits, unenroll } from '../store/enrollmentSlice';

function ProfilePage() {
  const dispatch = useDispatch();
  const enrolledCourses = useSelector(selectEnrolledCourses);
  const totalCredits = useSelector(selectTotalCredits);

  const [profile, setProfile] = useState({ name: '', email: '', semester: 1 });
  const [errors, setErrors] = useState({});
  const [submitted, setSubmitted] = useState(false);

  const handleChange = (field) => (event) => {
    const value = field === 'semester' ? Number(event.target.value) : event.target.value;
    setProfile((prev) => ({ ...prev, [field]: value }));
  };

  const validate = () => {
    const nextErrors = {};
    if (!profile.name || profile.name.trim().length < 2) {
      nextErrors.name = 'Name is required (min. 2 characters).';
    }
    if (!/^\S+@\S+\.\S+$/.test(profile.email)) {
      nextErrors.email = 'Enter a valid email address.';
    }
    if (profile.semester < 1 || profile.semester > 8) {
      nextErrors.semester = 'Semester must be between 1 and 8.';
    }
    setErrors(nextErrors);
    return Object.keys(nextErrors).length === 0;
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    setSubmitted(true);
    if (validate()) {
      console.log('Profile submitted:', profile);
    }
  };

  const isValid = Object.keys(errors).length === 0;

  return (
    <section aria-labelledby="profile-heading">
      <h1 id="profile-heading">My Profile</h1>

      <form className="profile-form" onSubmit={handleSubmit} noValidate>
        <div className="form-field">
          <label htmlFor="name">Full name</label>
          <input id="name" type="text" value={profile.name} onChange={handleChange('name')} />
          {submitted && errors.name && <p className="field-error">{errors.name}</p>}
        </div>

        <div className="form-field">
          <label htmlFor="email">Email</label>
          <input id="email" type="email" value={profile.email} onChange={handleChange('email')} />
          {submitted && errors.email && <p className="field-error">{errors.email}</p>}
        </div>

        <div className="form-field">
          <label htmlFor="semester">Semester</label>
          <input
            id="semester"
            type="number"
            min="1"
            max="8"
            value={profile.semester}
            onChange={handleChange('semester')}
          />
          {submitted && errors.semester && <p className="field-error">{errors.semester}</p>}
        </div>

        <button type="submit" className="btn btn-primary" disabled={submitted && !isValid}>
          Save profile
        </button>

        {submitted && isValid && (
          <p className="success-msg" role="status">
            Profile saved successfully.
          </p>
        )}
      </form>

      <h2>Enrolled Courses</h2>
      <p className="total-credits">
        Total credits: <strong>{totalCredits}</strong>
      </p>

      {enrolledCourses.length === 0 ? (
        <p>You haven't enrolled in any courses yet.</p>
      ) : (
        <ul className="enrolled-list">
          {enrolledCourses.map((course) => (
            <li key={course.id} className="enrolled-item">
              <div>
                <strong>{course.name}</strong>
                <span className="course-code">
                  {' '}
                  &middot; {course.code} &middot; {course.credits} credits
                </span>
              </div>
              <button className="btn btn-outline" onClick={() => dispatch(unenroll(course.id))}>
                Remove
              </button>
            </li>
          ))}
        </ul>
      )}
    </section>
  );
}

export default ProfilePage;
