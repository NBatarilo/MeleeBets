import {Component, OnInit, OnDestroy} from '@angular/core';
import {Subscription} from 'rxjs';
import { take } from 'rxjs/operators';
import {UsersApiService} from './users/users-api.service';
import {User} from './users/user.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, OnDestroy {
  title = 'app';
  usersListSubs?: Subscription;
  usersList?: User[];

  constructor(private usersApi: UsersApiService) {
  }

  //Is this right???? CHECK
  ngOnInit() {
    this.usersListSubs = this.usersApi
      .getUsers()
      .pipe(take(1))
      .subscribe(
        res => {this.usersList = res;},
      );
  }

  ngOnDestroy() {
    if(this.usersListSubs){
      this.usersListSubs.unsubscribe();
    }
  }
}