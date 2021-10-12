import { createSelector } from '@ngrx/store';
import * as fromFeature from '../reducers';
import * as fromAuth from '../reducers/auth.reducer';

export const getAuthDataState = createSelector(
  fromFeature.getUserState,
  (state: fromFeature.AppState) => (state.auth)
);

export const isLoggedIn = createSelector(
  fromFeature.getAuthState,
  fromAuth.isLoggedIn
);

export const getUserInfo = createSelector(
  fromFeature.getAuthState,
  fromAuth.getUserInfo
);

