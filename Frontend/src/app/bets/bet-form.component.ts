import {Component} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {BetsApiService} from "./bets.service";
import {Router} from "@angular/router";


@Component({
    selector: 'bet-form',
    template: `
      <div>
        <h2>New Bet</h2>
        <label for="exam-title">Title</label>
        <input id="exam-title" (keyup)="updateTitle($event)">
        <label for="exam-description">Description</label>
        <input id="exam-description" (keyup)="updateDescription($event)">
        <button (click)="saveExam()">Save Exam</button>
      </div>
    `
})