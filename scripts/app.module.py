import os, sys

content = '''

import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { environment } from '../environments/environment';

// Store
import { StoreModule, MetaReducer, ActionReducer } from '@ngrx/store';
import { StoreDevtoolsModule } from '@ngrx/store-devtools';
import { storeFreeze } from 'ngrx-store-freeze';
import { EffectsModule } from '@ngrx/effects';
import { reducers, effects } from './store';
import { localStorageSync } from 'ngrx-store-localstorage';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

// Components
import { AppComponent } from './app.component';
import { TextBoxComponent } from './components/text-box/text-box.component';

// Containers
import { HomeComponent } from './containers/home/home.component';
import { NotFoundComponent } from './containers/not-found/not-found.component';

// Routing
import { Routes, RouterModule } from '@angular/router';
import { NotificationsModule } from './notifications/notifications.module';

// Guards

export function localStorageSyncReducer(
  reducer: ActionReducer<any>
): ActionReducer<any> {
  return localStorageSync({
    keys: ['auth'],
    rehydrate: true
  })(reducer);
}

export const metaReducers: MetaReducer<any>[] = !environment.production
  ? [storeFreeze, localStorageSyncReducer]
  : [localStorageSyncReducer];

const routes: Routes = [
  {
    path: '',
    component: HomeComponent
  },
  // Must come last -----------
  {
    path: '404',
    component: NotFoundComponent
  },
  {
    path: '**',
    redirectTo: '/404'
  }
];

@NgModule({
  declarations: [
    AppComponent,
    TextBoxComponent,
    HomeComponent,
    NotFoundComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    StoreModule,
    FormsModule,
    ReactiveFormsModule,
    NotificationsModule,
    StoreModule.forRoot(reducers, { metaReducers }),
    EffectsModule.forRoot(effects),
    HttpClientModule,
    RouterModule.forRoot(routes),
    environment.production ? [] : StoreDevtoolsModule.instrument()
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {}
'''

project_name = sys.argv[1]
package_file_path = '../' + project_name + '/src/app/app.module.ts'

with open(package_file_path, 'r+') as f:
  lineArr = []
  lineArr.append(content)
  f.seek(0)
  f.write('\n'.join(lineArr))
  f.write('\n')
  f.truncate()