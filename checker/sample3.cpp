#include <iostream>  
using namespace std;  
int main()  
{  
	int i,f=1,number;    
	cout<<"Enter a no.: ";    
	cin>>/*this is a comment*/number;    //input the number you want the factorial for
	for(i=1;i<=number;i++/* a comment in the middle of the program */){    
		f=f*i;    
	}    
	cout<<"factorial of " /*another comment in the middle of the program */<<number<<" is: "<<f<<endl;  /*this gives the output
	this is a multi line comment*/return 0;  


} 
