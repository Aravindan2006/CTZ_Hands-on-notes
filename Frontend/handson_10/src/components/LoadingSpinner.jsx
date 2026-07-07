function LoadingSpinner({ message = 'Loading...' }) {
  return (
    <div className="spinner-wrapper" role="status" aria-live="polite">
      <span className="spinner" aria-hidden="true" />
      <span>{message}</span>
    </div>
  );
}

export default LoadingSpinner;
