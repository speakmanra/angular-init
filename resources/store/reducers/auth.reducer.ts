import * as actions from '../actions';
import { createReducer, on, Action } from '@ngrx/store';

export type UserInfo = {
  username: string;
  firstName: string;
  lastName: string;
}

export type AuthState = {
  loggedIn: boolean;
  loggingIn: boolean;
  userInfo: UserInfo | null;
};

export const initialState: AuthState = {
  loggedIn: false,
  loggingIn: false,
  userInfo: null
};

export const authReducer = createReducer(
  initialState,
  on(actions.Login, (state, action) => ({
    ...state,
    loggedIn: false,
    loggingIn: true
  })),
  on(actions.LoginSuccess, (state, action) => ({
    ...state,
    loggedIn: true,
    loggingIn: false,
    userInfo: action.payload
  })),
  on(actions.LoginFailure, () => initialState),
  on(actions.Logout, () => initialState)
);

export function reducer(
  state: AuthState | undefined,
  action: Action
): AuthState {
  return authReducer(state, action);
}

export const isLoggedIn = (state: AuthState) => {
  return state && state.loggedIn ? state.loggedIn : false}
export const getUserInfo = (state: AuthState) => state && state.userInfo;
