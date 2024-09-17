import { CanActivateFn } from '@angular/router';
import { inject } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../services/auth.service';

export const routeGuard: CanActivateFn = (route, state) => {
  const authService = inject(AuthService); // Inject AuthService
  const router = inject(Router); // Inject Router

  if (authService.isLoggedIn()) { 
    // If user is authenticated, allow to route.
    return true;
  } else {
    // if user not authenticated, route to login.
    router.navigate(['/login']);
    return false;
  }
};
