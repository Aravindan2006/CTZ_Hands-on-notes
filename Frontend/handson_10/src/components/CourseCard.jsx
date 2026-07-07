function CourseCard({ id, name, code, credits, grade, onSelect }) {
  const handleKeyDown = (event) => {
    if (event.key === 'Enter' || event.key === ' ') {
      event.preventDefault();
      onSelect?.(id);
    }
  };

  return (
    <article
      className="course-card"
      tabIndex={0}
      role="button"
      aria-label={`${name}, ${credits} credits`}
      onClick={() => onSelect?.(id)}
      onKeyDown={handleKeyDown}
    >
      <h3>{name}</h3>
      <p className="course-code">{code}</p>
      <p className="course-credits">
        <strong>{credits}</strong> credits
      </p>
      {grade && (
        <p className="course-grade">
          Grade: <strong>{grade}</strong>
        </p>
      )}
    </article>
  );
}

export default CourseCard;
