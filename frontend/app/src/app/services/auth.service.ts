import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Observable, take } from 'rxjs';
import { map } from 'rxjs/operators';
import { Router } from '@angular/router';
import { JwtHelperService } from '@auth0/angular-jwt';

interface User {
  id: string;
  username: string;
  email: string;
}

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  private currentUserSubject = new BehaviorSubject<User | null>(null);
  public currentUser$ = this.currentUserSubject.asObservable();

  constructor(
    private router: Router,
    private http: HttpClient,
    private jwt: JwtHelperService
  ) {}

<<<<<<< Updated upstream
  private devUrl: string = 'http://127.0.0.1:5000/auth/';
=======
  private baseUrl = 'http://127.0.0.1:5000/auth/';
>>>>>>> Stashed changes

  public registerUser(data: {
    username: string;
    password: string;
    email: string;
  }): Observable<any> {
<<<<<<< Updated upstream
    return this.http.post<any>(this.devUrl + 'register', data).pipe(
=======
    return this.http.post<any>(this.baseUrl + 'register', data).pipe(
>>>>>>> Stashed changes
      map((response) => {
        if (response) {
          this.router.navigate(['/login']);
        }
      })
    );
  }

  public loginUser(credentials: any): Observable<any> {
<<<<<<< Updated upstream
    return this.http.post<any>(this.devUrl + 'login', credentials).pipe(
=======
    return this.http.post<any>(this.baseUrl + 'login', credentials).pipe(
>>>>>>> Stashed changes
      map((response) => {
        if (response && response.token) {
          localStorage.setItem('token', response.token);
          this.currentUserSubject.next(response.user);
          return response;
        }
      })
    );
  }

  public logout(): void {
    localStorage.removeItem('token');
    this.currentUserSubject.next(null);
    this.router.navigate(['/login']);
  }

  public isLoggedIn(): boolean {
    const token: any = localStorage.getItem('token');
    return token && !this.jwt.isTokenExpired(token);
  }
}
