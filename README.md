# RED PLAG - A SOURCE CODE PLAGIARISM CHECKER

## Introduction and FLow

This projects aims at making a software for detecting plagiarism between C++ source code files. Here implemented is the website which will allow users to interact with the tool. Any user who opens the website land on the `Home Page` where they are given two options - `Login` for existing user and `Registration` for new user. After doing either, the user is taken to their `Dashboard` where they can select the files to upload for running through the plagiarism checker. There is also a `Logout` button to allow the user to logout and redirects to the `Home Page`. 

<p slign="center">
<img src="https://github.com/jsum007/RedPlagCryptoFox/blob/final/screenshots/home.png" width="500" height="250"/>  
<img src="https://github.com/jsum007/RedPlagCryptoFox/blob/final/screenshots/login.png" width="500" height="250"/>   
<img src="https://github.com/jsum007/RedPlagCryptoFox/blob/final/screenshots/register.png" width="500" height="250"/>
<img src="https://github.com/jsum007/RedPlagCryptoFox/blob/final/screenshots/dashboard.png" width="500" height="250"/>
 </p>

## Currently implemented part of project 

As of now, we have implemented the [Frontend](#front) of the website in Angular CLI and the [Backend](#back) in Django along with REST Framework allowing registration, login and authentication of users along with upload and download of files. For the processing of files, we have developed a basic checker in python using which works on tokenization and bag of words model. First the code is tokenized to remove comments, whitespaces and literals, then vectors of these tokens for each file are generated by concatenating onehot encoding of the tokens. Then cosine similarity is calculated between a pair of files by taking dot product of their vectors. Further explanation and details of website are given later.

## Steps to run the project 

`git clone https://github.com/jsum007/RedPlagCryptoFox`

(This won't work now as the repo is private but is added for later)

1. To get the Angular Frontend running - <br>
```
npm install
ng serve --open
````

2. To get the Django Backend running - <br>
```
cd backend
python3 manage.py migrate
python3 manage.py makemigrations
python3 manage.py runserver
```

# Red Plag - Frontend <a name="front"></a>

The frontend of the project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 10.1.6.

### Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

### Code scaffolding

Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive|pipe|service|class|guard|interface|enum|module`.

### Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory. Use the `--prod` flag for a production build.

### Running unit tests

Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).

### Running end-to-end tests

Run `ng e2e` to execute the end-to-end tests via [Protractor](http://www.protractortest.org/).

### Further help

To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI README](https://github.com/angular/angular-cli/blob/master/README.md).

****** 

# Red Plag - Backend

The backend of the project was generated with Django and the APIs were generated using Django REST Framework. 

### Registration of new User

### login and Authentication of existing user

### File upload/download

## Further part to be implemented

1. Improve Tokenization - Right now only a limited vocabulary of keywords and operators are declared which are being used in similarity calculation. This needs to be improved by 
expnading vocabulary, splitting declaration of multiple variables in separate lines and injecting the body of function each time a function is called. 
2. Incorporate exclusion - If there's some boilerplate code that is going to stay common across all files, they should be excluded from similarity calculation as that does not count as plagiarism.
3. Allow upload and extraction of zip files to compare a large number of files at once
4. Improve similarity estimation algorithm
