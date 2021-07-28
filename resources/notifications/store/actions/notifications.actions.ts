import { Action } from '@ngrx/store';

export const NOTIFY = '[NOTIFICATION] Notify';
export const NOTIFY_SUCCESS = '[NOTIFICATION] Notify Success';
export const NOTIFY_ERROR = '[NOTIFICATION] Notify Error';

export class Notify implements Action {
  readonly type = NOTIFY;

  constructor(public payload: string) {}
}

export class NotifySuccess implements Action {
  readonly type = NOTIFY_SUCCESS;
}

export class NotifyError implements Action {
  readonly type = NOTIFY_ERROR;

  constructor(public payload: string) {}
}

export type NotifyActions = Notify | NotifySuccess | NotifyError;
