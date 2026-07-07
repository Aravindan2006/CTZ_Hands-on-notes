import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Course } from '../../models/course.model';
import { CourseService } from '../../services/course.service';

@Component({
  selector: 'app-course-list',
  templateUrl: './course-list.component.html',
  styleUrls: ['./course-list.component.css'],
})
export class CourseListComponent implements OnInit {
  courses: Course[] = [];
  filteredCourses: Course[] = [];
  searchTerm = '';
  loading = true;
  errorMessage = '';

  constructor(private courseService: CourseService, private router: Router) {}

  ngOnInit(): void {
    this.fetchCourses();
  }

  private fetchCourses(): void {
    this.loading = true;
    this.errorMessage = '';

    this.courseService.getCourses().subscribe({
      next: (courses) => {
        this.courses = courses;
        this.applyFilter();
        this.loading = false;
      },
      error: (err) => {
        this.errorMessage = 'Unable to load courses right now. Please try again.';
        console.error(err);
        this.loading = false;
      },
    });
  }

  onSearchChange(): void {
    this.applyFilter();
  }

  private applyFilter(): void {
    const term = this.searchTerm.trim().toLowerCase();
    this.filteredCourses = term
      ? this.courses.filter((c) => c.name.toLowerCase().includes(term))
      : [...this.courses];
  }

  onSelectCourse(id: number): void {
    this.router.navigate(['/courses', id]);
  }

  trackByCourseId(_index: number, course: Course): number {
    return course.id;
  }
}
