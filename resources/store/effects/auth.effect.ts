import { Injectable } from '@angular/core';
import { createEffect, Actions, ofType } from '@ngrx/effects';
import { Action, Store } from '@ngrx/store';
import { Observable, of } from 'rxjs';
import { catchError, map, exhaustMap } from 'rxjs/operators';
import { AuthService } from '../../services/auth.service';
import * as fromActions from '../actions';

@Injectable()
export class AuthEffect {

  constructor(
    private actions$: Actions,
    public authService: AuthService
  ) {}

  loginAttempt$: Observable<Action> = createEffect(() =>
    this.actions$.pipe(ofType(fromActions.Login)).pipe(
      exhaustMap((action) =>
        this.authService.login(action.payload).pipe(
          map((res: any) => fromActions.LoginSuccess(res)),
          catchError((err) => of(fromActions.LoginFailure(err)))
        )
      )
    )
  );
}
