import { Component } from '@angular/core';
import { SharedModule } from '../../shared/shared.module';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [SharedModule],
  templateUrl: './register.component.html',
  styleUrl: './register.component.scss',
})
export class RegisterComponent {
  constructor(private auth: AuthService) {}

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
      this.errorMessage = 'Please ensure all fields are filled out correctly.';
      this.errorMessageTimeout();
      return;
    }
    this.auth
      .registerUser({
        username: this.username,
        password: this.password,
        email: this.userEmail,
      })
      .pipe()
      .subscribe({
        error: (err) => {
          if (err && err.error.message) {
            this.errorMessage = err.error.message;
          } else {
            this.errorMessage = 'Registration failed. Please try again later.';
          }
          this.errorMessageTimeout();
        },
      });
  }
}
