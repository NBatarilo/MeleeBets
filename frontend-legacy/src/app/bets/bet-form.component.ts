import {Component} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {BetsApiService} from "./bets-api.service";
import {Router} from "@angular/router";



@Component({
    selector: 'bet-form',
    template: `
      <div>
        <h2>New Bet</h2>
        <label for="bet-user">User</label>
        <input id="bet-user" (keyup)="updateUser($event)">
        <label for="bet-amount">Amount</label>
        <input id="bet-amount" (keyup)="updateAmount($event)">
        <button (click)="createBet()">Create Bet</button>
      </div>
    `
})

export class BetFormComponent {
  bet = {
    bettor_username: '',
    amount: 420,
    odds: 350, 
    outcome: -1, 
    payout: -1
  };

  constructor(private BetsApi: BetsApiService, private router: Router) { }

  updateUser(event: any) {
    this.bet.bettor_username = event.target.value;
  }

  updateAmount(event: any) {
    this.bet.amount = event.target.value;
  }

  createBet() {
    this.BetsApi
      .createBet(this.bet)
      .subscribe(
        () => this.router.navigate(['/']),
        error => alert(error.message)
      );
  }
}