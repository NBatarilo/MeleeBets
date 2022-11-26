import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { BetsComponent } from './bets.component';
import { BetsService } from '../services/bets.service';
import { RouterModule } from '@angular/router';

@NgModule({
  declarations: [
    BetsComponent,
  ],
  imports: [
    CommonModule,
    RouterModule,
  ],
  providers: [ BetsService ],
})
export class BetsModule { }
