import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import { catchError } from 'rxjs/operators';
import { Observable, throwError } from 'rxjs';
import {API_URL} from '../env';
import {Bet} from './bet.model';

@Injectable()
export class BetsApiService {

  constructor(private http: HttpClient) {
  }

  private static _handleError(err: HttpErrorResponse | any) {
    return throwError(() => err);
  }

  // GET list of bets
  getBets(): Observable<Bet[]> {
    return this.http
      .get<Bet[]>(`${API_URL}/bets`)
      .pipe(catchError(BetsApiService._handleError));
  }

  createBet(bet: Bet): Observable<any> {
    return this.http
      .post(`${API_URL}/bets`, bet);
  }
}