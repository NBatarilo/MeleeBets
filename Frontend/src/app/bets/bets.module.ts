import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { BetsComponent } from './bets.component';
import { BetsService } from '../services/bets.service';
import { RouterModule } from '@angular/router';
import { MatCardModule } from '@angular/material/card';
import { MatGridListModule } from '@angular/material/grid-list';
import { MatButtonModule } from '@angular/material/button';

@NgModule({
  declarations: [
    BetsComponent,
  ],
  imports: [
    CommonModule,
    RouterModule,
    MatCardModule,
    MatGridListModule,
    MatButtonModule
  ],
  providers: [ BetsService ],
})
export class BetsModule { }
