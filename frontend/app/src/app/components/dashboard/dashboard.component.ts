import { Component } from '@angular/core';
import { SharedModule } from '../../../shared';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [SharedModule],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.scss'
})
export class DashboardComponent {

  constructor (
    private auth: AuthService,
  ) {  }

  logoutUser(): void {
    try {
      this.auth.logout();
    } catch(e) {
      console.log(e);
    }
  }

}
