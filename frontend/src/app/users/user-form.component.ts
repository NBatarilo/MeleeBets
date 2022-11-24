import {Component, OnInit, OnDestroy} from '@angular/core';
import {Subscription} from 'rxjs';
import { take } from 'rxjs/operators';
import {UsersApiService} from './users-api.service';
import {User} from './user.model';
import {Router} from "@angular/router";

@Component({
    selector: 'app-root',
    template:`
    <div>
      <h2>Create Account</h2>
      <label for="user-name">Name</label>
      <input id="user-name" (keyup)="updateName($event)">
      <label for="user-password">Password</label>
      <input id="user-password" (keyup)="updatePassword($event)">
      <button (click)="createAccount()">Create Account</button>
    </div>
  `
})
export class UserFormComponent {
    user = {
      name: '',
      password: '',
    };

    constructor(private usersApi: UsersApiService, private router: Router) { }

    updateName(event: any) {
        this.user.name = event.target.value;
    }

    updatePassword(event: any) {
        this.user.password = event.target.value;
    }

    createAccount(){
        this.usersApi
            .createAccount(this.user)
            .pipe(take(1))
            .subscribe(
                () => this.router.navigate(['/']),
            );
    }
  }