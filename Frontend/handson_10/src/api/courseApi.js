import apiClient from './apiClient';
import { sampleCourses } from '../data/courses';

/**
 * courseApi (Hands-On 10, Task 1, Step 139): a small, focused module
 * of exported functions that components/thunks call instead of
 * reaching for axios/apiClient directly. Because the response
 * interceptor in apiClient already unwraps `response.data`, every
 * function here works with plain data.
 */

// JSONPlaceholder doesn't model "courses", so posts are mapped onto
// our local sample course shape (by index) — this still exercises a
// real HTTP round trip through the centralised client while keeping
// realistic course fields (name, code, credits, grade) in the UI.
function mapPostsToCourses(posts) {
  return posts.map((post, index) => {
    const base = sampleCourses[index % sampleCourses.length];
    return { ...base, id: post.id };
  });
}

export async function getAllCourses() {
  const posts = await apiClient.get('/posts?_limit=5');
  return mapPostsToCourses(posts);
}

export async function getCourseById(id) {
  const courses = await getAllCourses();
  const course = courses.find((c) => c.id === Number(id));
  if (!course) {
    const notFoundError = new Error(`Course ${id} not found`);
    notFoundError.statusCode = 404;
    throw notFoundError;
  }
  return course;
}

export async function enrollStudent(studentId, courseId) {
  // Simulated write: JSONPlaceholder accepts POSTs and echoes them
  // back without persisting, which is perfect for demonstrating the
  // request/response interceptor pipeline end-to-end.
  return apiClient.post('/posts', {
    title: `enrollment:${studentId}:${courseId}`,
    body: 'Student enrollment request',
    userId: studentId,
  });
}
