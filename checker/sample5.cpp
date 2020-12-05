#include<iostream>
using namespace std;


int main(){

int n;
int k;
cin>>n>>k;

int bag[k];


 
 for(int i=0; i<k ; i++){

 	cin>> bag[i];
 	
 }

 bool flag = true;
	int q_init = n/k;

	for (int i = 0; (i < k) && flag; i++)
				/*this is a comment*/if ((bag[i] < q_init) || (bag[i] > q_init+1)) flag = false;
	if/*a comment*/ (flag) //this is also a comment
	{
		
			return 0;	//comment again
	}



while(true){

for(int i=1; i<k;/*this is a comment*/ i++){

	while(bag[i] !=0){

		int temp= bag[i]/k;/*this is a
		multiline comment*/int res= bag[i] % k;

				bag[i] = temp;/*this is a multiline
				comment*/

		for(int j=1; j<k; j++){
			bag[(j+i)%k]+=temp;

				
		}

		for(int j=0; j<res;j++){

			bag[(j+i+1)%k]++;
		}

		
 cout<<i<<" ";

	}



}

int count=0;
for(int km=1; km<k; km++){
	count+=bag[km];
}

if(count==0) break;
}



int temp= bag[0]/k;
int res= bag[0] % k;

		bag[0] = temp;

		for(int j=1; j<k; j++){
			bag[(j)%k]+=temp;

				
		}

		for(int j=0; j<res;j++){

			bag[(j+1)%k]++;
		}

cout<<0<<endl;

return 0;



}
