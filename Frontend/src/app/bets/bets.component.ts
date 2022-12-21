import {Component, OnInit, OnDestroy} from '@angular/core';
import {Subscription} from 'rxjs';
import { take } from 'rxjs/operators';
import { BetsService } from '../services/bets.service';
import {Bet} from './bet.model';

@Component({
  selector: 'app-bets',
  templateUrl: './bets.component.html',
  styleUrls: ['./bets.component.scss']
})
export class BetsComponent implements OnInit, OnDestroy {

  betsListSubs?: Subscription;
  betsList?: Bet[];
  
  constructor(private betsApi: BetsService) {
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