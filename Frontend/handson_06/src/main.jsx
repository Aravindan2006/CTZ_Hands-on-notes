import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import { Provider } from 'react-redux';
import App from './App';
import { store } from './store/store';
import './styles.css';

// Task 1, Step 76: wrap <App /> in <BrowserRouter> for client-side routing.
// Task 3: wrap in Redux's <Provider> (replacing the Task 2
// <EnrollmentProvider> from context/EnrollmentContext.jsx) so every
// component can useSelector/useDispatch against the shared store.
ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <Provider store={store}>
      <BrowserRouter>
        <App />
      </BrowserRouter>
    </Provider>
  </React.StrictMode>
);
