import { Component, OnDestroy, OnInit } from '@angular/core';
import { select, Store } from '@ngrx/store';
import { Subscription } from 'rxjs';
import { UserInfo } from 'src/app/store/reducers/auth.reducer';
import * as fromStore from '../../store';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit, OnDestroy {

  userInfo$ = this.store.pipe(select(fromStore.getUserInfo));
  userInfoSub: Subscription | undefined;
  userInfo: UserInfo | null = null;

  isLoggedIn$ = this.store.pipe(select(fromStore.isLoggedIn));

  constructor(private store: Store<fromStore.AppState>) {}

  ngOnInit(): void {
    this.userInfoSub = this.userInfo$.subscribe(data => this.userInfo = data);
  }

  login(): void {
    this.store.dispatch(fromStore.Login());
  }

  logout(): void {
    this.store.dispatch(fromStore.Logout());
  }

  ngOnDestroy(): void {
    if (this.userInfoSub) {
      this.userInfoSub.unsubscribe();
    }
  }
}
