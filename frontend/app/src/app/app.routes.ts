import { Routes } from '@angular/router';
import { routeGuard } from './guards/route.guard';
import { LoginComponent } from './components/login/login.component';
import { RegisterComponent } from './components/register/register.component';
import { MainComponent } from './components/main/main.component';
import { NotesComponent } from './components/notes/notes.component';
import { TasksComponent } from './components/tasks/tasks.component';
import { TodosComponent } from './components/todos/todos.component';

export const routes: Routes = [
    { path: 'login', component: LoginComponent },
    { path: 'register', component: RegisterComponent },
    { path: 'main', component: MainComponent, canActivate: [routeGuard], children: [
        { path: 'notes', component: NotesComponent, canActivate: [routeGuard] },
        { path: 'tasks', component: TasksComponent, canActivate: [routeGuard]  },
        { path: 'todos', component: TodosComponent, canActivate: [routeGuard]  },
    ] },
    { path: '', redirectTo: '/login', pathMatch: 'full' },
    { path: '**', redirectTo: '/login' },
];
