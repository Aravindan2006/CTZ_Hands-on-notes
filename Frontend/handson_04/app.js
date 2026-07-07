// =====================================================================
// Hands-On 4 — Async JavaScript, Fetch API & API Integration
// =====================================================================

const localCourses = [
  { id: 1, name: 'Data Structures & Algorithms', code: 'CS101', credits: 4 },
  { id: 2, name: 'Database Management Systems', code: 'CS102', credits: 3 },
  { id: 3, name: 'Object Oriented Programming', code: 'CS103', credits: 4 },
  { id: 4, name: 'Circuit Theory', code: 'EC101', credits: 3 },
  { id: 5, name: 'Thermodynamics', code: 'ME101', credits: 3 },
];

// ---------------------------------------------------------------------
// TASK 1: Promises and async/await (Steps 45-49)
// ---------------------------------------------------------------------

// Step 45: fetchUser with .then() chaining
function fetchUserThenStyle(id) {
  return fetch(`https://jsonplaceholder.typicode.com/users/${id}`)
    .then((response) => response.json())
    .then((user) => {
      console.log('(.then style) User name:', user.name);
      return user;
    });
}

// Step 46: same function rewritten with async/await + try/catch
async function fetchUser(id) {
  try {
    const response = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`);
    const user = await response.json();
    console.log('(async/await style) User name:', user.name);
    return user;
  } catch (error) {
    console.error('fetchUser failed:', error);
    throw error;
  }
}

// Step 47: simulated 1-second network delay before returning local data
function fetchAllCourses() {
  return new Promise((resolve) => {
    setTimeout(() => resolve(localCourses), 1000);
  });
}

// Step 48: render courses only after the promise resolves, with a
// loading message shown in the meantime.
async function loadAndRenderCourses() {
  const statusEl = document.getElementById('courses-status');
  const grid = document.getElementById('course-grid');

  statusEl.textContent = 'Loading courses...';
  const courses = await fetchAllCourses();

  statusEl.textContent = '';
  grid.innerHTML = courses
    .map(
      (c) => `
      <article class="course-card">
        <h3>${c.name}</h3>
        <p class="course-code">${c.code}</p>
        <p class="course-credits">${c.credits} credits</p>
      </article>`
    )
    .join('');
}

// Step 49: Promise.all() — fetch two users simultaneously
async function fetchTwoUsersInParallel() {
  const [user1, user2] = await Promise.all([fetchUser(1), fetchUser(2)]);
  console.log('Promise.all resolved both users:', user1.name, user2.name);
}

fetchUserThenStyle(1);
loadAndRenderCourses();
fetchTwoUsersInParallel();

// ---------------------------------------------------------------------
// TASK 2: Fetch API with Error Handling (Steps 50-54)
// ---------------------------------------------------------------------

// Step 50: reusable apiFetch — checks response.ok, throws a
// descriptive error, returns parsed JSON.
async function apiFetch(url) {
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`Request to ${url} failed with status ${response.status}`);
  }
  return response.json();
}

const notificationsList = document.getElementById('notifications-list');
const retryBtn = document.getElementById('retry-btn');

// Step 51-53: load notifications, show a spinner/loading state, and
// display a friendly error + Retry button on failure (never console-only).
async function loadNotifications(url = 'https://jsonplaceholder.typicode.com/posts?_limit=3') {
  notificationsList.innerHTML = '<p id="notifications-loading">Loading notifications...</p>';
  retryBtn.hidden = true;

  try {
    const posts = await apiFetch(url);
    notificationsList.innerHTML = posts
      .map((post) => `<div class="notification-card"><strong>${post.title}</strong><p>${post.body}</p></div>`)
      .join('');
  } catch (error) {
    console.error('Failed to load notifications:', error);
    notificationsList.innerHTML =
      '<p class="error-banner">We couldn\'t load your notifications right now. Please try again.</p>';
    retryBtn.hidden = false;
  }
}

// Step 54: Retry button re-calls the fetch and re-renders
retryBtn.addEventListener('click', () => loadNotifications());

loadNotifications();

// Uncomment to simulate a 404 and see the error + Retry flow (Step 53):
// loadNotifications('https://jsonplaceholder.typicode.com/nonexistent');

// ---------------------------------------------------------------------
// TASK 3: Introduction to Axios (Steps 55-59)
// ---------------------------------------------------------------------

// Step 58: request interceptor logging every outgoing Axios request
axios.interceptors.request.use((config) => {
  console.log(`API call started: ${config.url}`);
  return config;
});

// Step 56-57: Axios automatically parses JSON and throws on non-2xx
// responses — no manual response.ok check needed, unlike Fetch.
async function loadUser1PostsWithAxios() {
  const statusEl = document.getElementById('axios-status');
  const listEl = document.getElementById('axios-posts');

  try {
    const { data: posts } = await axios.get('https://jsonplaceholder.typicode.com/posts', {
      params: { userId: 1 },
    });
    statusEl.textContent = `Loaded ${posts.length} posts for user 1 via Axios.`;
    listEl.innerHTML = posts.slice(0, 5).map((p) => `<li>${p.title}</li>`).join('');
  } catch (error) {
    statusEl.textContent = 'Failed to load posts via Axios.';
    console.error(error);
  }
}

loadUser1PostsWithAxios();

/*
 * Step 59 — Fetch vs Axios, three differences:
 * 1. JSON parsing: Fetch needs `await response.json()`; Axios parses
 *    the response body automatically into `response.data`.
 * 2. Error behaviour: Fetch only rejects on network failure — HTTP
 *    errors like 404/500 still resolve, so you must check
 *    `response.ok` yourself. Axios rejects automatically on any
 *    non-2xx status.
 * 3. Convenience features: Axios has built-in interceptors, a
 *    `timeout` option, and a `params` object for query strings; Fetch
 *    requires manual work (AbortController, URLSearchParams) to match.
 */
