import { useState } from 'react';

// Task 3, Step 74: local state form bound via onChange handlers.
function StudentProfile() {
  const [profile, setProfile] = useState({ name: '', email: '', semester: 1 });

  const handleChange = (field) => (event) => {
    const value = field === 'semester' ? Number(event.target.value) : event.target.value;
    setProfile((prev) => ({ ...prev, [field]: value }));
  };

  return (
    <section className="profile-section">
      <h2>Student Profile</h2>
      <form className="profile-form" onSubmit={(e) => e.preventDefault()}>
        <label>
          Name
          <input type="text" value={profile.name} onChange={handleChange('name')} />
        </label>
        <label>
          Email
          <input type="email" value={profile.email} onChange={handleChange('email')} />
        </label>
        <label>
          Semester
          <input
            type="number"
            min="1"
            max="8"
            value={profile.semester}
            onChange={handleChange('semester')}
          />
        </label>
      </form>
      <p className="profile-preview">
        {profile.name || 'Your name'} &middot; {profile.email || 'your@email.com'} &middot; Semester{' '}
        {profile.semester}
      </p>
    </section>
  );
}

export default StudentProfile;
