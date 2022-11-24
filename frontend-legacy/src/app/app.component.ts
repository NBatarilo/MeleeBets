import {Component, OnInit, OnDestroy} from '@angular/core';
import {Subscription} from 'rxjs';
import { take } from 'rxjs/operators';
import {UsersApiService} from './users/users-api.service';
import {User} from './users/user.model';



@Component({
  selector: 'app-root',
  template: `
    <navbar> </navbar>
    <div style="text-align:center">
      <h1>Users</h1>
    </div>
    <h2>Here are the users created so far: </h2>
    <router-outlet></router-outlet>
  `,
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, OnDestroy {
  title = 'app';

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