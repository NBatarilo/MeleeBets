import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AppComponent } from './app.component';
import { BetsComponent } from './bets/bets.component';
import { BetsModule } from './bets/bets.module';

const routes: Routes = [
  { path: 'overview', component: AppComponent},
  { path: 'bets', component: BetsComponent },
];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
