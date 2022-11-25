import {Component} from '@angular/core';




@Component({
  selector: 'app-root',
  template: `
    <navbar> </navbar>
    <div style="text-align:center">
      <h1>Bets</h1>
    </div>
    <h2>Here are the bets created so far: </h2>
    <router-outlet></router-outlet>
  `,
  styleUrls: ['./app.component.css']
})
export class AppComponent {}