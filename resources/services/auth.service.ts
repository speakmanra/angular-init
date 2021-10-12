import { Injectable, Inject } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  fakeReturn = {
    username: 'ThereAndBackAgain1',
    firstName: 'Bilbo',
    lastName: 'Baggins'
  }
  constructor(private http: HttpClient) {}

  login(data: any): Observable<HttpResponse<{}>> {
    return this.http.get<HttpResponse<{}>>(`http://localhost:3000/assets/fake-return.json`);
  }
}
