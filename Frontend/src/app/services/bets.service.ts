import { Injectable } from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import { catchError } from 'rxjs/operators';
import { Observable, throwError } from 'rxjs';
import {API_URL} from '../env';
import {Bet} from '../bets/bet.model';

@Injectable({
  providedIn: 'root'
})
export class BetsService {
  constructor(private http: HttpClient) {
  }

  private static _handleError(err: HttpErrorResponse | any) {
    return throwError(() => err);
  }

  // GET list of bets
  getBets(): Observable<Bet[]> {
    return this.http
      .get<Bet[]>(`${API_URL}/bets`)
      .pipe(catchError(BetsService._handleError));
  }
}
