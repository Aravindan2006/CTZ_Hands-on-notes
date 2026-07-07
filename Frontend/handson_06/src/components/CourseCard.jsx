function CourseCard({ id, name, code, credits, grade, onSelect }) {
  return (
    <article
      className="course-card"
      tabIndex={0}
      role="button"
      onClick={() => onSelect(id)}
      onKeyDown={(e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          onSelect(id);
        }
      }}
    >
      <h3>{name}</h3>
      <p className="course-code">{code}</p>
      <p className="course-credits">{credits} credits</p>
      {grade && <p className="course-grade">Grade: {grade}</p>}
    </article>
  );
}

export default CourseCard;
