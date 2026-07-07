// =====================================================================
// Hands-On 3 — JavaScript ES6+ & DOM Manipulation
// =====================================================================
import { courses } from './data.js';

// ---------------------------------------------------------------------
// TASK 1: ES6+ Syntax Practice (Steps 30-34)
// ---------------------------------------------------------------------

// Destructuring inside a loop (Step 30)
for (const { name, credits } of courses) {
  console.log(`${name} — ${credits} credits`);
}

// Array.map(): formatted strings (Step 31)
const formatted = courses.map(
  (course) => `${course.code} — ${course.name} (${course.credits} credits)`
);
console.log('Formatted courses:', formatted);

// Array.filter(): courses with credits >= 4 (Step 32)
const heavyCourses = courses.filter((course) => course.credits >= 4);
console.log(`Courses with 4+ credits: ${heavyCourses.length}`);

// Array.reduce(): total credits (Step 33)
const totalCredits = courses.reduce((sum, course) => sum + course.credits, 0);
console.log(`Total credits enrolled: ${totalCredits}`);

// Arrow function + template literal (Step 34)
const describeCourse = (course) => `${course.name} (${course.code})`;
console.log(courses.map(describeCourse).join(', '));

// ---------------------------------------------------------------------
// TASK 2: DOM Selection & Dynamic Rendering (Steps 35-39)
// ---------------------------------------------------------------------

const courseGrid = document.querySelector('.course-grid');
const totalCreditsEl = document.getElementById('total-credits');

let currentCourses = [...courses];

function renderCourses(list) {
  // Clear before re-rendering — avoids duplicate cards (Hint, Task 3).
  courseGrid.innerHTML = '';

  // DocumentFragment batches DOM insertion into a single update
  // instead of N separate appendChild calls (Hint, Task 2).
  const fragment = document.createDocumentFragment();

  list.forEach((course) => {
    const article = document.createElement('article');
    article.className = 'course-card';
    article.dataset.courseId = String(course.id);
    article.innerHTML = `
      <h3>${course.name}</h3>
      <p class="course-code">${course.code}</p>
      <p class="course-credits">${course.credits} credits</p>
    `;
    fragment.appendChild(article);
  });

  courseGrid.appendChild(fragment);

  const sumCredits = list.reduce((sum, c) => sum + c.credits, 0);
  totalCreditsEl.textContent = `Total credits shown: ${sumCredits}`;
}

// ---------------------------------------------------------------------
// TASK 3: Event Listeners & Interactivity (Steps 40-44)
// ---------------------------------------------------------------------

const searchInput = document.getElementById('search-courses');
const sortBtn = document.getElementById('sort-btn');
const selectedCourseEl = document.getElementById('selected-course');

// Search: filter by name on every keystroke (Step 41)
searchInput.addEventListener('input', (event) => {
  const term = event.target.value.trim().toLowerCase();
  const filtered = term
    ? currentCourses.filter((c) => c.name.toLowerCase().includes(term))
    : currentCourses;
  renderCourses(filtered);
});

// Sort by credits descending (Step 42)
sortBtn.addEventListener('click', () => {
  currentCourses = [...currentCourses].sort((a, b) => b.credits - a.credits);
  renderCourses(currentCourses);
});

// Event delegation: one listener on the grid container, not one per
// card (Step 44) — uses event.target.closest to find the clicked card.
courseGrid.addEventListener('click', (event) => {
  const card = event.target.closest('.course-card');
  if (!card) return;

  const id = Number(card.dataset.courseId);
  const course = courses.find((c) => c.id === id);
  if (course) {
    selectedCourseEl.textContent = `Selected: ${course.name} — Grade ${course.grade}`;
  }
});

// ---------------------------------------------------------------------
// Init
// ---------------------------------------------------------------------
renderCourses(currentCourses);
