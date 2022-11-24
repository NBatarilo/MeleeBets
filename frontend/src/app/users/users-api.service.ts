import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import { catchError } from 'rxjs/operators';
import { Observable, throwError } from 'rxjs';
import 'rxjs/add/operator/catch';
import {API_URL} from '../env';
import {User} from './user.model';

@Injectable()
export class UsersApiService {

  constructor(private http: HttpClient) {
  }

  private static _handleError(err: HttpErrorResponse | any) {
    return throwError(() => err);
  }

  // GET list of users
  getUsers(): Observable<User[]> {
    return this.http
      .get<User[]>(`${API_URL}/users`)
      .pipe(catchError(UsersApiService._handleError));
  }
}