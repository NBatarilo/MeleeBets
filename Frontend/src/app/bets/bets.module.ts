import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { BetsComponent } from './bets.component';
import { BetsService } from '../services/bets.service';
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [
    BetsComponent,
  ],
  imports: [
    CommonModule,
    HttpClientModule,
    
  ],
  providers: [ BetsService ],
  bootstrap: [ BetsComponent ]
})
export class BetsModule { }
