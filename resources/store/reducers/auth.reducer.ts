import * as actions from '../actions';
import { createReducer, on, Action } from '@ngrx/store';

export type AuthState = {
  loggedIn: boolean;
  loggingIn: boolean;
  userInfo: {
    username: string;
    firstName: string;
    lastName: string;
  } | null
};

export const initialState: AuthState = {
  loggedIn: false,
  loggingIn: false,
  userInfo: null
};

export const authReducer = createReducer(
  initialState,
  on(actions.Login, (state, action) => ({ ...state, loggedIn: false, loggingIn: true })),
  on(actions.LoginSuccess, (state, action) => ({ ...state, loggedIn: true, loggingIn: false, userInfo: action.payload.userInfo })),
  on(actions.LoginFailure, () => initialState)
);

export function reducer(
  state: AuthState | undefined,
  action: Action
): AuthState {
  return authReducer(state, action);
}

export const getAuthState = (state: AuthState) => state;
