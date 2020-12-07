#include<vector>
#include<iostream>
#include<algorithm>
using namespace std;


int* lb_left_func( int* a, int n){
	int* lb_left = new int[n];
lb_left[0] = -1;
for (int i = 1; i < n; i++)
{
      int j =i-1;
      while ((j >= 0) && (a[j]<a[i]))  j = lb_left[j];
      lb_left[i] =j;

}

//for (int i=0; i < n; i++){if(lb_left[i]==-1) lb_left[i]=1;} 
return lb_left;
}



int* lb_right_func( int* a, int n){
	int* lb_right = new int[n];
	int* lb_right_f = new int[n];
lb_right[0] = -1;
for (int i = 1; i < n; i++){
      int j =i-1;
      while ((j >=0) && (a[j]<a[i]))  j = lb_right[j];
      lb_right[i] =j;
}

for (int i=0; i < n; i++){
	if(lb_right[i]!=-1) lb_right[i]=n-lb_right[i]-1;
	else lb_right[i]=n;
} 
for (int i=0; i < n; i++) lb_right_f[i] = lb_right[n-1-i];

	delete [] lb_right;
return lb_right_f;
}


int main(){ int n;
	cin>>n;

	int* inp= new int[n];
	int* rev= new int[n];
	for(int i=0; i<n;i++) {cin>>inp[i];
		rev[n-i-1]=inp[i];
	}


	int* temp_left=lb_left_func(inp,n);
	int* temp_right=lb_right_func(rev,n);

	//for(int i=0; i<n; i++) cout<< temp_right[i]<<" ";
		//cout<<endl;


	for(int i=0; i<n; i++){ //cout<< temp[i]<<" ";
		cout<< (i-temp_left[i])*(temp_right[i]-i)<<" ";} 
	cout<<endl;
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

	vector<int> inp_2(inp,inp+n);



	int* greatest_to_left= new int[n];
greatest_to_left[0] = -1;
for (int i = 1; i < n; i++)
{
      int j =i-1;
      while ((j >= 0) && (inp[j]<=inp[i]))  j = greatest_to_left[j];
      greatest_to_left[i] =j;

}

delete [] rev;
delete [] inp;

long long int final=0;

	vector<int> min_to;
	/*min_to[0].push_back(0);
	for(int i=1; i<n;i++){
		if(inp[i-1]<=inp[i]){
			min_to[i]=min_to[i-1];
			min_to[i].push_back(i-1);
			min_to[i].push_back(i);
		}

		else
	}
	
	for(int i=0;i<n;i++){ final += (min_to[i].end() -lower_bound(min_to[i].begin(), min_to[i].end(),greatest_to_left[i]));
		
	}	 

	cout<<final;*/

	for(int i=0; i<n; i++){
		if(min_to.empty()) final+=1;

		else {


			while(min_to.empty()!=true && inp_2[min_to[min_to.size()-1]]>inp_2[i]) min_to.pop_back();

			if(min_to.empty()) final+=1;

			else {int tmp= lower_bound(min_to.begin(), min_to.end(),greatest_to_left[i])- min_to.begin();
					final+= (min_to.size()-tmp+1);}
			
		}
		min_to.push_back(i);
	}

cout<<final<<endl;

}
