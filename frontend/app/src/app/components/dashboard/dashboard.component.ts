import { Component } from '@angular/core';
import { SharedModule } from '../../../shared';
import {MatSidenavModule} from '@angular/material/sidenav'; 

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [SharedModule, MatSidenavModule],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.scss'
})
export class DashboardComponent {
  showFiller = false;
}
