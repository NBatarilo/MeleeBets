import {Component, OnInit, OnDestroy} from '@angular/core';
import {Subscription} from 'rxjs';
import { take } from 'rxjs/operators';
import {UsersApiService} from './users/users-api.service';
import {User} from './users/user.model';
import {BetsApiService} from './bets/bets-api.service';
import {Bet} from './bets/bet.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  /* template: `
    <div style="text-align:center">
      <h1>Bets</h1>
    </div>
    <h2>Here are the bets created so far: </h2>
    <router-outlet></router-outlet>
  `, */
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, OnDestroy {
  title = 'app';

  /* usersListSubs?: Subscription;
  usersList?: User[]; */

  betsListSubs?: Subscription;
  betsList?: Bet[];

  /* constructor(private usersApi: UsersApiService) {
  } */
  
  constructor(private betsApi: BetsApiService) {
  }
  
  ngOnInit() {
    /* this.usersListSubs = this.usersApi
      .getUsers()
      .pipe(take(1))
      .subscribe(
        user_res => {this.usersList = user_res;},
      ); */

      this.betsListSubs = this.betsApi
      .getBets()
      .pipe(take(1))
      .subscribe(
        bet_res => {this.betsList = bet_res;},
      );
  }

  ngOnDestroy() {
    /* if(this.usersListSubs){
      this.usersListSubs.unsubscribe();
    } */

    if(this.betsListSubs){
      this.betsListSubs.unsubscribe();
    }
  }
}