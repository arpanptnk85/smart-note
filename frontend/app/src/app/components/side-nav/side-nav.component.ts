import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import {MatButtonModule} from '@angular/material/button';
import { MatRadioModule } from '@angular/material/radio';
import {MatSidenavModule, MatDrawerMode, MatSidenav} from '@angular/material/sidenav';
import { SharedModule } from '../../shared/shared.module';



@Component({
  selector: 'app-side-nav',
  standalone: true,
  imports: [MatButtonModule, MatSidenavModule, MatRadioModule, SharedModule],
  templateUrl: './side-nav.component.html',
  styleUrl: './side-nav.component.scss'
})
export class SideNavComponent implements OnInit {

  @ViewChild('sidenav') sidenav!: MatSidenav;

  ngOnInit(): void {
    this.toggleSidenav();
  }
  

  toggleSidenav(): void {
    console.log(this.sidenav);
    this.sidenav.toggle();
  }


}
