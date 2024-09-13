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

  login(): void {
    if (!this.username || !this.password) { return }
    console.log(this.username, this.password)
  }

}
