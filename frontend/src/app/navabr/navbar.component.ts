import {Component} from '@angular/core';
import {MatToolbarModule} from '@angular/material/toolbar';
import {MatIcon, MatIconModule} from '@angular/material/icon'

@Component({
    standalone: true,
    selector: 'navbar',
    imports: [
        MatToolbarModule,
        MatIconModule,
    ],
    templateUrl: './navbar.component.html'
  })

  export class NavbarComponent {}