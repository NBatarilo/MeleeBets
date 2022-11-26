import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import { catchError } from 'rxjs/operators';
import { Observable, throwError } from 'rxjs';
import {API_URL} from '../env';
import {User} from '../users/user.model';

@Injectable({
  providedIn: 'root'
})
export class UsersService {

  constructor(private http: HttpClient) {
  }

  private static _handleError(err: HttpErrorResponse | any) {
    return throwError(() => err);
  }

  // GET list of users
  getUsers(): Observable<User[]> {
    return this.http
      .get<User[]>(`${API_URL}/users`)
      .pipe(catchError(UsersService._handleError));
  }

  createAccount(user: User): Observable<any> {
    return this.http
      .post(`${API_URL}/users`, user)
  }
}