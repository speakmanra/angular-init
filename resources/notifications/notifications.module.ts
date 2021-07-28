import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatSnackBarModule, MatSnackBar } from '@angular/material/snack-bar';

// Effects
import { EffectsModule } from '@ngrx/effects';
import { effects } from './store';

@NgModule({
  declarations: [],
  imports: [CommonModule, MatSnackBarModule, EffectsModule.forFeature(effects)],
  providers: [MatSnackBar]
})
export class NotificationsModule {}
