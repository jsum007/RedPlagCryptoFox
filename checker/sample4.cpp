#include <iostream>  
using namespace std;

void print() {
	cout<<1235466889<<endl;
}

class Point {

public:

	int x, y;

	Point (int c, int d) {
		x=c; y=d;
	}

}; 

int point;

class box {
	
	Point tl, br;

	Point numa(int g) {
		return Point(7, 8);
	}

	void print() {
		cout<<tl.x<<" "<<tl.y;
	}
};

int main()  
{  
   int i,fact=1,number;    
  cout<<"Enter any Number: ";    
 cin>>number;    
  for(i=1;i<=number;i++){    
      fact=fact*i;    
  }    
  cout<<"Factorial of " <<number<<" is: "<<fact<<endl;  
  return 0;  

  Point(5, 6);
} 