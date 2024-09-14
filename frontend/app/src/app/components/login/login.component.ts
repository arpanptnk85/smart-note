import { Component } from '@angular/core';
import { SharedModule } from '../../../shared';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [SharedModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.scss'
})

export class LoginComponent {

  constructor() { }

  username: string|null = null;
  password: string|null = null;
  errorMessage: string|null = null;

  errorMessageTimeout(): void {
    setTimeout(() => {
      this.errorMessage = null;
    }, 2400);
  }

  login(): void {
    if (!this.username || !this.password) {
      this.errorMessage = "Please ensure all fields are filled out correctly."
      this.errorMessageTimeout();
    };
    this.errorMessage = "There was an error processing your login. Please try again later."
    this.errorMessageTimeout();
  }

}
