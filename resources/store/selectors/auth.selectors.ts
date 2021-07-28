import { createSelector } from '@ngrx/store';
import * as fromFeature from '../reducers';
import * as fromAuth from '../reducers/auth.reducer';

export const getAuthDataState = createSelector(
  fromFeature.getAuthState,
  (state: fromFeature.AppState) => (state ? state.auth : {})
);
