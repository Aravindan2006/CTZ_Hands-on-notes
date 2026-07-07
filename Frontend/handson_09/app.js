// =====================================================================
// Student Portal — Accessible Edition — app.js
// =====================================================================
import { courses as allCourses } from './data.js';

const courseGrid = document.getElementById('course-grid');
const resultsCount = document.getElementById('results-count');
const searchInput = document.getElementById('search-courses');
const sortBtn = document.getElementById('sort-btn');
const selectedCourseEl = document.getElementById('selected-course');
const navToggle = document.getElementById('nav-toggle');
const primaryNav = document.getElementById('primary-nav');
const exploreBtn = document.getElementById('explore-btn');

let currentCourses = [...allCourses];

// ---------------------------------------------------------------------
// Rendering
// ---------------------------------------------------------------------

function renderCourses(list) {
  // Clear before re-rendering to avoid duplicate cards.
  courseGrid.innerHTML = '';

  const fragment = document.createDocumentFragment();

  list.forEach((course) => {
    const card = document.createElement('article');
    card.className = 'course-card';
    card.dataset.courseId = String(course.id);

    // Accessibility: cards act as buttons, so they need tabindex,
    // role, and an accessible name (Hands-On 9, Task 2, Step 129).
    card.setAttribute('tabindex', '0');
    card.setAttribute('role', 'button');
    card.setAttribute('aria-label', `${course.name}, ${course.credits} credits`);

    card.innerHTML = `
      <h3>${course.name}</h3>
      <p class="course-code">${course.code}</p>
      <p class="course-credits">${course.credits} credits</p>
      ${course.grade ? `<p class="course-grade">Grade: <strong>${course.grade}</strong></p>` : ''}
    `;

    fragment.appendChild(card);
  });

  courseGrid.appendChild(fragment);
  updateResultsCount(list.length);
}

function updateResultsCount(count) {
  // aria-live="polite" on this element (set in HTML) means screen
  // readers announce this text change without interrupting the user.
  resultsCount.textContent = `${count} course${count === 1 ? '' : 's'} found`;
}

// ---------------------------------------------------------------------
// Search (Hands-On 3, Task 3, Step 41)
// ---------------------------------------------------------------------

searchInput.addEventListener('input', (event) => {
  const term = event.target.value.trim().toLowerCase();
  const filtered = term
    ? currentCourses.filter((c) => c.name.toLowerCase().includes(term))
    : currentCourses;
  renderCourses(filtered);
});

// ---------------------------------------------------------------------
// Sort (Hands-On 3, Task 3, Step 42)
// ---------------------------------------------------------------------

sortBtn.addEventListener('click', () => {
  currentCourses = [...currentCourses].sort((a, b) => b.credits - a.credits);
  renderCourses(currentCourses);
});

// ---------------------------------------------------------------------
// Event delegation for card clicks + keyboard activation
// (Hands-On 3, Task 3, Steps 43-44; Hands-On 9, Task 2, Step 129)
// ---------------------------------------------------------------------

function activateCard(cardEl) {
  const id = Number(cardEl.dataset.courseId);
  const course = allCourses.find((c) => c.id === id);
  if (!course) return;

  selectedCourseEl.textContent = `Selected: ${course.name} — Grade ${course.grade ?? 'N/A'}`;
}

courseGrid.addEventListener('click', (event) => {
  const card = event.target.closest('.course-card');
  if (card) activateCard(card);
});

courseGrid.addEventListener('keydown', (event) => {
  const card = event.target.closest('.course-card');
  if (!card) return;

  // Enter or Space activates the focused card, matching a mouse click
  // (Hands-On 9, Task 2, Step 129 — keyboard parity with pointer input).
  if (event.key === 'Enter' || event.key === ' ') {
    event.preventDefault();
    activateCard(card);
  }
});

// ---------------------------------------------------------------------
// Mobile nav toggle — real <button> with aria-expanded (Hands-On 9)
// ---------------------------------------------------------------------

navToggle.addEventListener('click', () => {
  const isOpen = primaryNav.classList.toggle('open');
  navToggle.setAttribute('aria-expanded', String(isOpen));
});

exploreBtn.addEventListener('click', () => {
  document.getElementById('courses').scrollIntoView({ behavior: 'smooth' });
});

// ---------------------------------------------------------------------
// Profile form validation (Hands-On 3/9): basic HTML5 + custom message
// ---------------------------------------------------------------------

const profileForm = document.getElementById('profile-form');
const profileStatus = document.getElementById('profile-status');

profileForm.addEventListener('submit', (event) => {
  event.preventDefault();

  if (!profileForm.checkValidity()) {
    profileStatus.textContent = 'Please fix the highlighted fields before saving.';
    profileForm.reportValidity();
    return;
  }

  profileStatus.textContent = 'Profile saved successfully.';
});

// ---------------------------------------------------------------------
// Notifications — Fetch API with loading/error/retry (Hands-On 4)
// ---------------------------------------------------------------------

const notificationsList = document.getElementById('notifications-list');
const retryBtn = document.getElementById('retry-btn');

async function apiFetch(url) {
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`Request failed with status ${response.status}`);
  }
  return response.json();
}

async function loadNotifications() {
  notificationsList.innerHTML = '<p id="notifications-loading">Loading notifications...</p>';
  retryBtn.hidden = true;

  try {
    const posts = await apiFetch('https://jsonplaceholder.typicode.com/posts?_limit=3');
    notificationsList.innerHTML = '';

    const fragment = document.createDocumentFragment();
    posts.forEach((post) => {
      const card = document.createElement('div');
      card.className = 'notification-card';
      card.innerHTML = `<strong>${post.title}</strong><p>${post.body}</p>`;
      fragment.appendChild(card);
    });
    notificationsList.appendChild(fragment);
  } catch (error) {
    // Never just log to console for user-facing errors — show a
    // friendly, actionable message plus a Retry control.
    notificationsList.innerHTML = `<p class="error-banner">We couldn't load your notifications right now. Please try again.</p>`;
    retryBtn.hidden = false;
    console.error('Failed to load notifications:', error);
  }
}

retryBtn.addEventListener('click', loadNotifications);

// ---------------------------------------------------------------------
// Feature detection & polyfill note (Hands-On 9, Task 3, Step 137)
// ---------------------------------------------------------------------
// Prefer feature detection (checking whether the browser supports a
// feature) over browser/user-agent sniffing (checking *which*
// browser it is) — it degrades gracefully as browsers evolve.
if (!('IntersectionObserver' in window)) {
  console.warn('IntersectionObserver not supported — lazy-loading features will be skipped.');
}

if (typeof CSS !== 'undefined' && CSS.supports && !CSS.supports('gap', '1rem')) {
  // Older Safari (<14.1) did not support `gap` in Flexbox. In that
  // case we fall back to margin-based spacing via this class, applied
  // only when the feature is genuinely absent.
  document.documentElement.classList.add('no-flex-gap');
}

// ---------------------------------------------------------------------
// Init
// ---------------------------------------------------------------------

renderCourses(currentCourses);
loadNotifications();
