import {Component, OnInit, OnDestroy} from '@angular/core';
import {Subscription} from 'rxjs';
import { take } from 'rxjs/operators';

import {BetsApiService} from './bets-api.service';
import {Bet} from './bet.model';

@Component({
  selector: 'app-root',
  template: `
  <div>
    <button routerLink="/new-bet">New Bet</button>
    <ul>
      <li *ngFor="let bet of betsList">
        {{bet.bettor_username}}, {{bet.amount}}
      </li>
    </ul>
  </div>
`
})
export class BetsComponent implements OnInit, OnDestroy {

  betsListSubs?: Subscription;
  betsList?: Bet[];
  
  constructor(private betsApi: BetsApiService) {
  }
  
  ngOnInit() {

      this.betsListSubs = this.betsApi
      .getBets()
      .pipe(take(1))
      .subscribe(
        bet_res => {this.betsList = bet_res;},
      );
  }

  ngOnDestroy() {
   
    if(this.betsListSubs){
      this.betsListSubs.unsubscribe();
    }
  }
}