import { Injectable, Inject } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  constructor(
    private http: HttpClient,
  ) {}

  login(data: any): Observable<HttpResponse<{}>> {
    return this.http.get<HttpResponse<{}>>(`/api/login`);
  }
}
