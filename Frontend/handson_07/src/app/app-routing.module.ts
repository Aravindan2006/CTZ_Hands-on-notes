import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { CourseListComponent } from './components/course-list/course-list.component';
import { StudentProfileComponent } from './components/student-profile/student-profile.component';
import { CourseDetailComponent } from './components/course-detail/course-detail.component';

// Route map for the Student Portal:
//   ''            -> course list (home / course browsing page)
//   'courses/:id' -> single course detail page
//   'profile'     -> student profile page (reactive form)
const routes: Routes = [
  { path: '', component: CourseListComponent, title: 'Courses | Student Portal' },
  { path: 'courses/:id', component: CourseDetailComponent, title: 'Course Detail | Student Portal' },
  { path: 'profile', component: StudentProfileComponent, title: 'My Profile | Student Portal' },
  { path: '**', redirectTo: '' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
