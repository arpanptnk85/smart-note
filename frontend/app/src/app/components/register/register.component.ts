import { Component } from '@angular/core';
import { SharedModule } from '../../../shared';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [SharedModule],
  templateUrl: './register.component.html',
  styleUrl: './register.component.scss'
})
export class RegisterComponent {

  constructor() { }

  username: string | null = null;
  password: string | null = null;
  userEmail: string | null = null;
  errorMessage: string | null = null;

  errorMessageTimeout(): void {
    setTimeout(() => {
      this.errorMessage = null;
    }, 2400);
  }

  register(): void {
    if (!this.username || !this.password || !this.userEmail) {
      this.errorMessage = "Please ensure all fields are filled out correctly."
      this.errorMessageTimeout();
      return;
    };
    this.errorMessage = "There was an error processing your registration. Please try again later."
    this.errorMessageTimeout();
  }

}
