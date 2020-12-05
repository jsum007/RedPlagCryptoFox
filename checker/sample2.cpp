#include <iostream>  
using namespace std;  
int main()  
{  
	int i,f=1,number;    
	cout<<"Enter a no.: ";    
	cin>>number;    
	for(i=1;i<=number;i++){    
		f=f*i;    
	}    
	cout<<"factorial of " <<number<<" is: "<<f<<endl;  
	return 0;  


} 