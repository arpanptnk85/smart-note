import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { JwtHelperService } from '@auth0/angular-jwt';

interface User {
  _id: string;
  username: string;
  email: string;
  password: string;
  created_at: any;
  updated_at: any;
}

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private currentUserSubject = new BehaviorSubject<User | null>(null);
  public currentUser$ = this.currentUserSubject.asObservable();

  constructor(private http: HttpClient, private jwt: JwtHelperService) { }

  public login(credentials: any): Observable<any> {
    return this.http.post<any>(
      'http://localhost:5000/auth/login', credentials
    ).pipe(map(response => {
      if (response && response.token) {
        localStorage.setItem('token', response.token);
        this.currentUserSubject.next(response.user);
      }
      return response;
    }));
  }

  public logout(): void {
    localStorage.removeItem('token');
    this.currentUserSubject.next(null);
  }

  public isLoggedIn(): boolean {
    const token: any = localStorage.getItem('token');
    return token && !this.jwt.isTokenExpired(token);
  }
}
