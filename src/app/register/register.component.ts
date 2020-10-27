import { Component, OnInit } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { UserServiceService } from '../user-service.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss'],
  providers: [UserServiceService]
})
export class RegisterComponent implements OnInit {
user;
  constructor(private userSer: UserServiceService) { }

  ngOnInit()  {
    this.user = {
      email : '',
      password: ''
    };
  }
registerUser(){
  this.userSer.registerNewUser(this.user).subscribe(
    response => {
      alert('User'+ this.user.email + 'has been created')
    },
    error => {console.log('error', error), alert('error')}
  );
}
}
