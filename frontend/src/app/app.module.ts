import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {HttpClientModule} from '@angular/common/http';

import {AppComponent} from './app.component';
import {UsersApiService} from './users/users-api.service';
import { MatchesComponent } from './matches/matches.component';
import { BetsApiService } from './bets/bets-api.service';

@NgModule({
  declarations: [
    AppComponent,
    MatchesComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
  ],
  providers: [UsersApiService, BetsApiService],
  bootstrap: [AppComponent]
})
export class AppModule {
}
