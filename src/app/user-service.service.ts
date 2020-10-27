import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable  } from 'rxjs'
import { HttpClientModule } from '@angular/common/http';

@Injectable()

export class UserServiceService {

  constructor(private http: HttpClient) {}

registerNewUser(userData) : Observable<any> {
  return this.http.post('http://127.0.0.1:8000/api/signup/', userData);
}

loginNewUser(userData) : Observable<any> {
  return this.http.post('http://127.0.0.1:8000/api/signin/', userData);
}


//getUserClaims(){
  //return  this.http.get('http://127.0.0.1:8000/api/');
 //}

}
