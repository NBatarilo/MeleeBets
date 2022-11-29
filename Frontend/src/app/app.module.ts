import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NavigationComponent } from './navigation/navigation.component';
import { RouterModule } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';
import { BetsModule } from './bets/bets.module';
import { UsersModule } from './users/users.module';
import { AuthModule } from '@auth0/auth0-angular';

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
    UsersModule,
    AuthModule.forRoot({
      domain: 'dev-a8quaktpx2vpip8p.us.auth0.com',
      clientId: 'JiC84wkkHrpHnH33n5qYSp5nyKxRdMQj'
    })
  ],
  providers: [  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
