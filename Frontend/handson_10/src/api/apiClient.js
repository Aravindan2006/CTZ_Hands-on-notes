import axios from 'axios';

/**
 * Centralised Axios instance (Hands-On 10, Task 1).
 *
 * Every API module in this project (see courseApi.js) is built on top
 * of this single client, so the base URL, timeout, headers, auth
 * token, and error handling all live in exactly one place.
 */
const apiClient = axios.create({
  baseURL: 'https://jsonplaceholder.typicode.com',
  timeout: 8000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// ---------------------------------------------------------------------
// Request interceptor: attaches an Authorization header to every
// outgoing request (Hands-On 10, Task 1, Step 141). In a real app this
// token would come from an auth store / secure storage rather than
// being hardcoded.
// ---------------------------------------------------------------------
apiClient.interceptors.request.use(
  (config) => {
    const mockToken = 'mock-jwt-token-for-student-portal-demo';
    config.headers.Authorization = `Bearer ${mockToken}`;
    console.log(`API call started: ${config.baseURL}${config.url}`);
    return config;
  },
  (error) => Promise.reject(error)
);

// ---------------------------------------------------------------------
// Response interceptor: unwraps `response.data` so every caller gets
// plain data (not the Axios response envelope), and converts any
// error into a standardised { message, statusCode } shape so
// components never have to deal with HTTP status codes directly
// (Hands-On 10, Task 1, Step 140).
// ---------------------------------------------------------------------
apiClient.interceptors.response.use(
  (response) => response.data,
  (error) => {
    const statusCode = error.response?.status ?? 0;
    const message =
      error.response?.data?.message ||
      error.message ||
      'An unexpected network error occurred.';

    const standardisedError = new Error(message);
    standardisedError.statusCode = statusCode;

    return Promise.reject(standardisedError);
  }
);

export default apiClient;

/*
 * Fetch vs. Axios — three differences (Hands-On 4, Task 3, Step 59):
 *
 * 1. JSON parsing: Fetch requires an explicit `await response.json()`
 *    step; Axios parses the response body automatically.
 * 2. Error behaviour: Fetch only rejects on network failures (offline,
 *    DNS errors) — a 404/500 response is still a "successful" Promise
 *    that you must check via `response.ok`. Axios rejects automatically
 *    on any non-2xx status code.
 * 3. Built-in conveniences: Axios ships with request/response
 *    interceptors, automatic request timeouts, and a `params` option
 *    for query strings — Fetch requires manual work (AbortController
 *    for timeouts, URLSearchParams for query strings) to match this.
 */
