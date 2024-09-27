import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { AuthService } from './auth.service';

export interface Note {
  id: string;
  title: string;
  text: string;
  tag: any[];
  depth: string;
  user_id: string;
  created: string;
  updated: string;
}

@Injectable({
  providedIn: 'root'
})
export class NotesService {

  constructor(
    private http: HttpClient,
    private auth: AuthService,
  ) { }

  private baseUrl: string = 'http://127.0.0.1:5000/api/v1/notes';

  public fetchNotesByUser(): Observable<any> {
    const url: string = [this.baseUrl, 'user-notes'].join('/');
    const headers: any = {
      'Authorization': `Bearer ${localStorage.getItem('token')}`
    };
    return this.http.get<any>(url, { headers })
      .pipe(map(response => {
        return response;
      }));
  }


}
