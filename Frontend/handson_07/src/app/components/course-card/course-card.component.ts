import { Component, EventEmitter, Input, Output } from '@angular/core';

@Component({
  selector: 'app-course-card',
  templateUrl: './course-card.component.html',
  styleUrls: ['./course-card.component.css'],
})
export class CourseCardComponent {
  @Input() id!: number;
  @Input() name!: string;
  @Input() code!: string;
  @Input() credits!: number;
  @Input() grade?: string;

  @Output() select = new EventEmitter<number>();

  onActivate(): void {
    this.select.emit(this.id);
  }

  onKeydown(event: KeyboardEvent): void {
    // Keyboard accessibility: Enter or Space activates the card,
    // matching what a mouse click would do (Hands-On 9 pattern).
    if (event.key === 'Enter' || event.key === ' ') {
      event.preventDefault();
      this.onActivate();
    }
  }
}
