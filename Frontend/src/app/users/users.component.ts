import {Component, OnInit, OnDestroy} from '@angular/core';
import {Subscription} from 'rxjs';
import { take } from 'rxjs/operators';
import {UsersService} from '../services/users.service';
import {User} from './user.model';

@Component({
  selector: 'app-users',
  templateUrl: './users.component.html',
  styleUrls: ['./users.component.css']
})
export class UsersComponent implements OnInit, OnDestroy {
  
  usersListSubs?: Subscription;
  usersList?: User[]; 

  

   constructor(private usersApi: UsersService) {
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
