import { Component, OnInit } from '@angular/core';
import { UserService } from '../user.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss'],
  providers: [UserService]
})
export class RegisterComponent implements OnInit {

  input;

  constructor(private userService: UserService, private router: Router) {}

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
        this.redirect();
      },
      error => console.log('error', error)
    )
    
  }

  redirect() {
    this.router.navigate(['/dashboard']);
  }

}
