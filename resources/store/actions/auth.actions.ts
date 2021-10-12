import { createAction } from '@ngrx/store';

// An example action set up that defaults with a payload of null

export const Login = createAction('[AUTH] Login', (payload = null) => ({
  payload
}));
export const LoginSuccess = createAction(
  '[AUTH] Login Success',
  (payload = null) => ({ payload })
);
export const LoginFailure = createAction(
  '[AUTH] Login Failure',
  (payload = null) => ({ payload })
);

export const Logout = createAction('[AUTH] Logout');
