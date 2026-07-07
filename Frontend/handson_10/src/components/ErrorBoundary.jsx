import { Component } from 'react';

/**
 * Global error boundary (Hands-On 10, Task 3, Step 150). Class
 * components are still required for error boundaries in React — there
 * is no Hooks equivalent for getDerivedStateFromError/componentDidCatch.
 * Wraps the whole app in main.jsx so any uncaught render error shows a
 * friendly fallback instead of a blank white screen.
 */
class ErrorBoundary extends Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }

  componentDidCatch(error, errorInfo) {
    console.error('Uncaught application error:', error, errorInfo);
  }

  handleReset = () => {
    this.setState({ hasError: false, error: null });
  };

  render() {
    if (this.state.hasError) {
      return (
        <div className="error-boundary" role="alert">
          <h2>Something went wrong</h2>
          <p>
            An unexpected error occurred while rendering this page. You can try
            reloading the affected section below.
          </p>
          <button className="btn btn-outline" onClick={this.handleReset}>
            Try again
          </button>
        </div>
      );
    }

    return this.props.children;
  }
}

export default ErrorBoundary;
