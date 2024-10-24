import { Component } from '@angular/core';
<<<<<<< Updated upstream
import { SharedModule } from '../../shared/shared.module';
=======
import { SharedModule } from '../../../shared';
>>>>>>> Stashed changes
import { AuthService } from '../../services/auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [SharedModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.scss',
})
export class LoginComponent {
  constructor(
    private auth: AuthService,
    private router: Router,
  ) {}

  username: string | null = null;
  password: string | null = null;
  errorMessage: string | null = null;

  errorMessageTimeout(): void {
    setTimeout(() => {
      this.errorMessage = null;
    }, 2400);
  }

  login(): void {
    if (!this.username || !this.password) {
      this.errorMessage = 'Please ensure all fields are filled out correctly.';
      this.errorMessageTimeout();
    }
    this.auth.loginUser({ username: this.username, password: this.password }).pipe().subscribe((response) => {
      if ('message' in response) {
        this.errorMessage = 'There was an error processing your login. Please try again later.';
        this.errorMessageTimeout();
      } else {
        this.router.navigate(['/dashboard']);
      }
    });
  }
}
