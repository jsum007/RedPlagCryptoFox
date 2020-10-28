import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable  } from 'rxjs'
import { HttpClientModule } from '@angular/common/http';
import { Router } from '@angular/router';

@Injectable()

export class UserServiceService {

  constructor(private http: HttpClient,  private router : Router) {}

registerNewUser(userData) : Observable<any> {
  return this.http.post('http://127.0.0.1:8000/api/signup/', userData);
}

loginNewUser(userData) : Observable<any> {
  return this.http.post('http://127.0.0.1:8000/api/signin/', userData);
}


uploadFile_service(userData) : Observable<any> {
  return this.http.post('http://127.0.0.1:8000/files/upload/', userData);
}

public get loggedIn(): boolean {
  return (localStorage.getItem('userToken') !== null);
}

LogoutUser(){
  localStorage.removeItem('userToken');
  this.router.navigate(['/home']);
}

//getUserClaims(){
  //return  this.http.get('http://127.0.0.1:8000/api/');
 //}

}
