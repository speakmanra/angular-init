import { Injectable } from '@angular/core';
import { Actions, createEffect, ofType } from '@ngrx/effects';
import { MatSnackBar } from '@angular/material/snack-bar';

import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

import { Message } from '../../store/models/message.model';

import * as notificationsActions from '../actions';
import * as authActions from '../../../store/actions/auth.actions';

@Injectable()
export class NotificationEffects {
  constructor(
    private actions$: Actions,
    private snackBar: MatSnackBar,
  ) {}

  signupSuccess$: Observable<any> = createEffect(() =>
  this.actions$
    .pipe(ofType(authActions.LoginSuccess))
    .pipe(
      map(() => {
        const message = {
          text: 'Login Successful.',
          type: 'success'
        };

        this.open(message);

        return new notificationsActions.NotifySuccess();
      })
    )
  );

  open(message: Message, duration: number = 5000): void {
    this.snackBar.open(message.text, 'Dismiss', {
      duration,
      panelClass: message.type
    });
  }
}
