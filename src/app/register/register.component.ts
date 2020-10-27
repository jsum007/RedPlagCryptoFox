import { Component, OnInit } from '@angular/core';
import { UserService } from '../user.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss'],
  providers: [UserService]
})
export class RegisterComponent implements OnInit {

  input;

  constructor(private userService: UserService) {}

  ngOnInit() {
    this.input = {
      username: '',
      password: '',
      email: ''
    };
  }

  onRegister() {
    this.userService.registerUser(this.input).subscribe(
      response => {
        alert('User ' + this.input.username + ' has been created!');
        console.log(response);
      },
      error => console.log('error', error)
    )
    
  }

}
