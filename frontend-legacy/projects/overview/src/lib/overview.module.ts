import { NgModule } from '@angular/core';
import { OverviewComponent } from './overview.component';
import { MatSlideToggleModule } from '@angular/material/slide-toggle';


@NgModule({
  declarations: [
    OverviewComponent
  ],
  imports: [
    MatSlideToggleModule
  ],
  exports: [
    OverviewComponent
  ]
})
export class OverviewModule { }
