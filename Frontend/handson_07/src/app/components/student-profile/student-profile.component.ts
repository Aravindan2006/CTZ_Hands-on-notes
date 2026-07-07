import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-student-profile',
  templateUrl: './student-profile.component.html',
  styleUrls: ['./student-profile.component.css'],
})
export class StudentProfileComponent {
  profileForm: FormGroup;
  submitted = false;

  constructor(private fb: FormBuilder) {
    // Reactive Forms are defined in the component class, which keeps
    // validation logic explicit and testable (Hands-On 7, Task 3).
    this.profileForm = this.fb.group({
      name: ['', [Validators.required, Validators.minLength(2)]],
      email: ['', [Validators.required, Validators.email]],
      semester: [1, [Validators.required, Validators.min(1), Validators.max(8)]],
    });
  }

  get name() {
    return this.profileForm.get('name')!;
  }

  get email() {
    return this.profileForm.get('email')!;
  }

  get semester() {
    return this.profileForm.get('semester')!;
  }

  onSubmit(): void {
    this.submitted = true;
    if (this.profileForm.valid) {
      console.log('Profile submitted:', this.profileForm.value);
    }
  }
}
