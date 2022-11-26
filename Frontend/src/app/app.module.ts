import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NavigationComponent } from './navigation/navigation.component';
import { RouterModule } from '@angular/router';
import { UsersComponent } from './users/users.component';
import { HttpClientModule } from '@angular/common/http';
import { BetsComponent } from './bets/bets.component';
import { BetsModule } from './bets/bets.module';
import { UsersModule } from './users/users.module';


@NgModule({
  declarations: [
    AppComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    RouterModule,
    BrowserAnimationsModule,
    NavigationComponent,
    HttpClientModule,
    BetsModule,
    UsersModule
  ],
  providers: [  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
