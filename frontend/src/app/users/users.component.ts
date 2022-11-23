import {Component, OnInit, OnDestroy} from '@angular/core';
import {Subscription} from 'rxjs';
import { take } from 'rxjs/operators';
import {UsersApiService} from './users-api.service';
import {User} from './user.model';


@Component({
    selector: 'users',
    template: `
      <div>
        <button routerLink="/new-user">New User</button>
        <ul>
          <li *ngFor="let user of usersList">
            {{user.name}}, {{user.password}}
          </li>
        </ul>
      </div>
    `
  })

  export class UsersComponent implements OnInit, OnDestroy {
  
    usersListSubs?: Subscription;
    usersList?: User[]; 
  
    
  
     constructor(private usersApi: UsersApiService) {
    } 
    
    
    ngOnInit() {
      this.usersListSubs = this.usersApi
        .getUsers()
        .pipe(take(1))
        .subscribe(
          user_res => {this.usersList = user_res;},
        ); 
    }
  
    ngOnDestroy() {
      if(this.usersListSubs){
        this.usersListSubs.unsubscribe();
      } 
    }
  }