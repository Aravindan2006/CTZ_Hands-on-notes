# Hands-On 4 — Async JavaScript, Fetch API & API Integration

Replaces hardcoded data with live data from JSONPlaceholder, covering
Promises, `async`/`await`, error handling, loading states, and a first
look at Axios.

## Files

- `index.html` — courses, notifications, and Axios demo sections; loads Axios via CDN
- `app.js` — all three tasks: Promises/async-await, Fetch + error handling, Axios
- `styles.css` — styling for cards, error banner, retry button

## Run

Open `index.html` directly in your browser (requires internet access
to reach `jsonplaceholder.typicode.com` and the Axios CDN). Open the
DevTools console to see the Promise-chaining and `Promise.all` logs.

## What's demonstrated

- **Task 1:** `fetch().then()` chaining vs. `async`/`await` with
  `try/catch`; a simulated 1-second delay before rendering courses with
  a loading message; `Promise.all()` fetching two users in parallel
- **Task 2:** a reusable `apiFetch()` helper that checks `response.ok`
  and throws a descriptive error; a loading indicator; a friendly
  on-page error message (never console-only) with a working **Retry**
  button
- **Task 3:** Axios via CDN, automatic JSON parsing, automatic
  rejection on non-2xx responses, `params` object for query strings,
  and a request interceptor that logs every outgoing call

## Try the error path

Edit the last commented-out line in `app.js`
(`loadNotifications('https://jsonplaceholder.typicode.com/nonexistent')`)
to simulate a 404 and confirm the error banner + Retry button appear
and that Retry successfully re-fetches.
