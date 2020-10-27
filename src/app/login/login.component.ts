import { Component, OnInit } from '@angular/core';
import { UserService } from '../user.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
  providers: [UserService]
})
export class LoginComponent implements OnInit {

  input;
  constructor(private userService: UserService, private router: Router) {}

  ngOnInit(): void {
    this.input = {
      username: '',
      password: '',
      //email: ''
    };
  }

  onLogin() {
    this.userService.loginUser(this.input).subscribe(
      response => {
        alert('User ' + this.input.username + ' has been logged in!');
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
