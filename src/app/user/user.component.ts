import { Component, OnInit } from '@angular/core';
import { UserServiceService } from '../user-service.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.scss']
})
export class UserComponent implements OnInit {
    file: File;



  constructor(private userSer: UserServiceService, private router : Router) { }

  ngOnInit(){
    //this.userSer.getUserClaims().subscribe((data: any) => {
     // this.userClaims = data;

    //});

  }

  Logout() {
    localStorage.removeItem('userToken');
    this.router.navigate(['/login']);
  }

}
