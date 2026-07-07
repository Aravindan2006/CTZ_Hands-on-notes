// Task 1, Step 65: accepts props and renders a styled card.
function CourseCard({ name, code, credits, grade, onEnroll, enrolled }) {
  return (
    <article className="course-card">
      <h3>{name}</h3>
      <p className="course-code">{code}</p>
      <p className="course-credits">{credits} credits</p>
      {grade && <p className="course-grade">Grade: {grade}</p>}
      {onEnroll && (
        <button className="btn btn-primary" onClick={onEnroll} disabled={enrolled}>
          {enrolled ? 'Enrolled ✓' : 'Enroll'}
        </button>
      )}
    </article>
  );
}

export default CourseCard;
