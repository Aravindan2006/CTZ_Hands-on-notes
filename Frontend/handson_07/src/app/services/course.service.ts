import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, catchError, map, of, tap } from 'rxjs';
import { Course } from '../models/course.model';

/**
 * CourseService centralises all course data-fetching logic so
 * components never talk to HttpClient directly (Hands-On 7, Task 2).
 *
 * providedIn: 'root' makes this a singleton shared across the whole
 * app via Angular's dependency injection.
 */
@Injectable({
  providedIn: 'root',
})
export class CourseService {
  private readonly postsUrl = 'https://jsonplaceholder.typicode.com/posts?_limit=5';

  // Local fallback/sample data used to enrich the API response with
  // course-shaped fields (credits, code, grade) that JSONPlaceholder
  // doesn't provide, and used directly by CourseDetailComponent.
  private readonly sampleCourses: Course[] = [
    { id: 1, name: 'Data Structures & Algorithms', code: 'CS101', credits: 4, grade: 'A', description: 'Core data structures, algorithmic complexity, and problem solving.' },
    { id: 2, name: 'Database Management Systems', code: 'CS102', credits: 3, grade: 'B', description: 'Relational modelling, SQL, normalisation, and transactions.' },
    { id: 3, name: 'Object Oriented Programming', code: 'CS103', credits: 4, grade: 'A', description: 'Classes, inheritance, polymorphism, and design patterns.' },
    { id: 4, name: 'Circuit Theory', code: 'EC101', credits: 3, grade: 'B', description: 'Fundamentals of electrical circuits and network analysis.' },
    { id: 5, name: 'Thermodynamics', code: 'ME101', credits: 3, grade: 'C', description: 'Laws of thermodynamics and energy transfer systems.' },
  ];

  constructor(private http: HttpClient) {}

  /**
   * Fetches 5 posts from JSONPlaceholder and maps them onto our local
   * course sample data (by index) so the UI shows realistic course
   * fields while still exercising a real HTTP round trip.
   */
  getCourses(): Observable<Course[]> {
    return this.http.get<any[]>(this.postsUrl).pipe(
      map((posts) =>
        posts.map((post, index) => {
          const base = this.sampleCourses[index % this.sampleCourses.length];
          return {
            ...base,
            id: post.id,
            name: base.name,
          } as Course;
        })
      ),
      tap((courses) => console.log(`CourseService: loaded ${courses.length} courses`)),
      catchError((error) => {
        console.error('CourseService: failed to load courses, falling back to sample data', error);
        return of(this.sampleCourses);
      })
    );
  }

  getCourseById(id: number): Observable<Course | undefined> {
    return this.getCourses().pipe(
      map((courses) => courses.find((c) => c.id === id))
    );
  }
}
