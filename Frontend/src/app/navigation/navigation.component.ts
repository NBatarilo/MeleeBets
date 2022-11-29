import { Component, Inject, OnDestroy } from '@angular/core';
import { RouterModule } from '@angular/router';
import { LayoutModule } from '@angular/cdk/layout';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule } from '@angular/material/button';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatIconModule } from '@angular/material/icon';
import { MatListModule } from '@angular/material/list';
import { BrowserModule } from '@angular/platform-browser';
import { AuthService } from '@auth0/auth0-angular';
import { Subject, takeUntil } from 'rxjs';
import { DOCUMENT } from '@angular/common';


@Component({
  standalone: true,
  imports: [
    RouterModule,
    LayoutModule,
    MatToolbarModule,
    MatButtonModule,
    MatSidenavModule,
    MatIconModule,
    MatListModule,
    BrowserModule,
  ],
  selector: 'app-navigation',
  templateUrl: './navigation.component.html',
  styleUrls: ['./navigation.component.css']
})
export class NavigationComponent implements OnDestroy {

  private destroy$: Subject<boolean> = new Subject<boolean>()
  
  constructor(
    @Inject(DOCUMENT) public document: Document,
    private _auth: AuthService
  ) {}

  auth$ = this._auth.isAuthenticated$
  user$ = this._auth.user$

  login(){
    this._auth.loginWithRedirect();
  }

  logout() {
    this._auth.logout({ 
      returnTo: this.document.location.origin 
    });
  }

  ngOnDestroy(): void {
      this.destroy$.next(true)
      this.destroy$.complete()
  }
}
