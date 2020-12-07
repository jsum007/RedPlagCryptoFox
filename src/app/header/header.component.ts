import { Component, OnInit } from '@angular/core';
import { UserServiceService } from '../user-service.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {
  	page : String;

  constructor(private userSer: UserServiceService, private router : Router) {
	  this.page = window.location.href.split("/")[window.location.href.split("/").length-1]
  }

  ngOnInit(): void {
  }
  foo = 1;
  log = localStorage.getItem('userToken') !== null;
  //log2 = true;

  Logout() {
    //alert(this.userSer.loggedIn);
    this.userSer.LogoutUser();
    //alert(this.userSer.loggedIn);
  }

  Disp(log : Boolean, page : String){
  	if(log){
  		if(page!="login"){
  			return true;
  		}
  		else
  			return false;
  	}
  }



}
