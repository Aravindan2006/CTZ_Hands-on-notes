import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Course } from '../../models/course.model';
import { CourseService } from '../../services/course.service';

@Component({
  selector: 'app-course-detail',
  templateUrl: './course-detail.component.html',
  styleUrls: ['./course-detail.component.css'],
})
export class CourseDetailComponent implements OnInit {
  course?: Course;
  loading = true;
  notFound = false;
  enrolled = false;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private courseService: CourseService
  ) {}

  ngOnInit(): void {
    const idParam = this.route.snapshot.paramMap.get('id');
    const id = idParam ? Number(idParam) : NaN;

    if (Number.isNaN(id)) {
      this.notFound = true;
      this.loading = false;
      return;
    }

    this.courseService.getCourseById(id).subscribe({
      next: (course) => {
        this.course = course;
        this.notFound = !course;
        this.loading = false;
      },
      error: () => {
        this.notFound = true;
        this.loading = false;
      },
    });
  }

  onEnroll(): void {
    this.enrolled = true;
    // Navigate the student to their profile after enrolling, as
    // required by the routing hands-on.
    setTimeout(() => this.router.navigate(['/profile']), 600);
  }

  goBack(): void {
    this.router.navigate(['/']);
  }
}
