import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { UsersComponent } from './users.component';
import { RouterModule } from '@angular/router';
import { UsersService } from '../services/users.service';



@NgModule({
  declarations: [ 
    UsersComponent, 
  ],
  imports: [
    CommonModule,
    RouterModule, 
  ],
  providers: [
    UsersService
  ]
})
export class UsersModule { }
