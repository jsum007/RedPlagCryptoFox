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
    alert(this.userSer.loggedIn);
    this.userSer.LogoutUser();
    alert(this.userSer.loggedIn);
  }

  onFile(event: any) {
    this.file = event.target.files[0];
  }
 uploadFile() {
   const uploadData = new FormData();
   uploadData.append('file', this.file, this.file.name);
  this.userSer.uploadFile_service(uploadData).subscribe(
    response => {
      console.log(response)
      alert('File'+ this.file.name + 'has been uploaded')
    },
    error => {console.log('error', error), alert('error')
  }
  );
 }
}
