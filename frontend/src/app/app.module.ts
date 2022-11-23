import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {HttpClientModule} from '@angular/common/http';
import {AppComponent} from './app.component';
import {UsersApiService} from './users/users-api.service';
import { MatchesComponent } from './matches/matches.component';
import { BetsApiService } from './bets/bets-api.service';
import {UserFormComponent} from './users/user-form.component';
import {RouterModule, Routes} from '@angular/router';
import {UsersComponent} from './users/users.component';
import {CommonModule} from '@angular/common';
import { OverviewComponent, OverviewModule } from 'projects/overview/src/public-api';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

const appRoutes: Routes = [
  { path: 'overview', component: OverviewComponent},
  { path: 'new-user', component: UserFormComponent },
  { path: '', component: UsersComponent },
];

@NgModule({
  declarations: [
    AppComponent,
    MatchesComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    CommonModule,
    OverviewModule,
    RouterModule.forRoot(
      appRoutes,
    ),
    BrowserAnimationsModule,  
  ],
  providers: [UsersApiService, BetsApiService],
  bootstrap: [AppComponent]
})
export class AppModule {
}
