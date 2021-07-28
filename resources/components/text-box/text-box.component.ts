import { Component, OnInit } from '@angular/core';
import { Store } from '@ngrx/store';
import * as fromStore from '../../store';

@Component({
  selector: 'app-text-box',
  templateUrl: './text-box.component.html',
  styleUrls: ['./text-box.component.scss']
})
export class TextBoxComponent {

  constructor(private store: Store<fromStore.AppState>) { }

  login(): void {
    this.store.dispatch(fromStore.Login())
  }

}
