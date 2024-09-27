import { Component } from '@angular/core';
import { SharedModule } from '../../../shared';
import { AuthService } from '../../services/auth.service';
import { NotesService, Note } from '../../services/notes.service';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [SharedModule],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.scss'
})
export class DashboardComponent {

  constructor (
    private authService: AuthService,
    private noteService: NotesService,
  ) {  }

  userNotes: any | null = null;
  currentNoteDepth: string | null = "low";

  logoutUser(): void {
    try {
      this.authService.logout();
    } catch(e) {
      console.log(e);
    }
  }

  getNotes() {
    this.noteService.fetchNotesByUser().subscribe(
      (resp: any) => {
        this.userNotes = resp;
        console.log(this.userNotes);
      }
    )
  }

  handleNoteDepth(e: any) {
    this.currentNoteDepth = e.target.value ?? "low";
  }

}
