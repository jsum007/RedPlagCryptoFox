#include<iostream>
#include<string>
#include<vector>
using namespace std;
using ll = long long;



ll sub_4(string sub, string inthis){
	ll j=0;
	ll res=-1;
	ll lens=sub.length();
	ll leni= inthis.length();
	ll temp=0;

	for(ll i=0; i<leni && j<lens; i++){
		if(sub[j]==inthis[i]) j++;
		temp=i+1;
	}
	if(j==lens) res=temp;
	return res;
}



string nth_from_prev(string Sn_1, string inp[]){

	ll len1=Sn_1.length();
	string Sn="";

	for(int ik=0; ik<len1; ik++){Sn+=inp[(int) Sn_1[ik]-int('a')];

	}
return Sn;
}


/******Referred GeeksForGeeks for implementation of KMP SEarch*******/

void computeLPSArray(string pat, ll M, ll* lps); 
  
ll KMPSearch(string pat, string txt) 
{ 
    ll M = pat.length(); 
    ll N = txt.length(); 
    ll lps[M]; 
    computeLPSArray(pat, M, lps); 
  
    ll i = 0; 
    ll j = 0; 
    while (i < N) { 
        if (pat[j] == txt[i]) { 
            j++; 
            i++; 
        } 
  
        if (j == M) { 
            return (i-j); 
        } 
  
        else if (i < N && pat[j] != txt[i]) { 
            
            if (j != 0) 
                j = lps[j - 1]; 
            else
                i = i + 1; 
        } 
    }
    return -1; 
} 
  
void computeLPSArray(string pat, ll M, ll* lps) 
{ 
    ll len = 0; 
  
    lps[0] = 0;  
    ll i = 1; 
    while (i < M) { 
        if (pat[i] == pat[len]) { 
            len++; 
            lps[i] = len; 
            i++; 
        } 
        else
        { 
            
            if (len != 0) { 
                len = lps[len - 1]; 
  
            } 
            else 
            { 
                lps[i] = 0; 
                i++; 
            } 
        } 
    } 
} 


void mat_mul(ll A[][6], ll B[][6], int k){
	ll temp[6][6];	
	for(int i=0; i<k;i++){
		for(int j=0; j<k;j++){
			temp[i][j]=0;
			for(int m=0;m<k;m++){
				temp[i][j]+=A[i][m]*B[m][j];    

			}
		}
	}

	for(int i=0;i<k;i++){
		for(int j=0; j<k; j++){
			A[i][j]=temp[i][j];
		}
	}
}



void mat_exp(ll a[][6], int k, ll n, ll res[][6]){
 ll A[6][6];

	for(int i=0;i<6;i++){
		for(int j=0; j<6; j++){
			if(i==j) res[i][j]=1;
			else res[i][j]=0;
		}
	}

	for(int i=0;i<k;i++){
		for(int j=0; j<k; j++){
			A[i][j]=a[i][j];
		}
	}

	ll tt=n;

	while (tt>0){
		if(tt%2==1) mat_mul(res,A,k); 

		mat_mul(A,A,k);

		tt=tt/2;

	}

}


void nlen(ll count[][6], ll n, int k, ll len_f1[], ll part1_ans[]){

	ll res[6][6];
	mat_exp(count,k,n-1,res);


	for(int i=0; i<k;i++){
			part1_ans[i]=0;
			for(int j=0;j<k;j++){
				part1_ans[i]+=res[i][j]*len_f1[j];    

			}
		}

}


char ith_term(vector<ll> ff[], string inp[], ll ith, char ww, ll n){
		int a=int('a');
	if(ith<=inp[(int) ww - a].length()-1) return inp[(int) ww - a][ith];

ll ni=0, tempi=ith;
char te=ww;
	while(tempi>=0){ tempi=tempi-ff[(int)inp[(int) ww - a][ni] -a][n-2];
		if(tempi>=0) {ith=tempi; }
		te=inp[(int) ww -a][ni];
		ni++;
		//cout<<"ith"<<" "<<ith;
		//cout<<te<<endl;

	}
return ith_term(ff,inp,ith,te,n-1);

}



int main(){ int k;
	cin>>k;
	string inp[k];

	for(int i=0; i<k;i++) cin>> inp[i];

	ll count[6][6],len_f1[k]={0};

	for(int i=0;i<6;i++){
		for(int j=0; j<6; j++){
			count[i][j]=0;
		}
	}

	for( int i=0; i<k; i++){
		len_f1[i]=inp[i].length();
		for(int j=0;j<inp[i].length();j++){
			count[i][(int)inp[i][j] - int('a')]++;

		}

	}

int testcas=0;
cin>>testcas;

for(int ooo=0;ooo<testcas;ooo++){

int oper;
cin>>oper;

	/********************PART1************/
if(oper==0){
ll n;
cin>>n;

ll part1_ans[k];

if(n!=0){nlen(count,n,k,len_f1,part1_ans);
		cout<<part1_ans[0]<<"\n";}
		else cout<<1<<"\n";
	}

	/************************************part2**********************************************************************/


if(oper==1){		

ll ith;
cin>> ith;

vector<ll>* lens =new vector<ll>[k];
ll ni=1;
while(true){


	ll temp_1[k];

nlen(count,ni,k,len_f1,temp_1);

for(int i=0; i<k;i++) lens[i].push_back(temp_1[i]);

//cout<<temp_1[0]<<"\n";
if(temp_1[0]>ith) break;
ni++;

}

cout<<ith_term(lens,inp,ith,'a',lens[0].size())<<"\n";

}

/**************************************PART3*******************/

if(oper==2){

string inp_w;
cin>>inp_w;

ll len_w=inp_w.length();

if(inp_w=="a") cout<<0<<" "<<0;

else{
ll ni3=1;
while(true){


	ll tempa[k];

nlen(count,ni3,k,len_f1,tempa);
//cout<<tempa[0]<<endl;
if(tempa[0]>=len_w) break;
ni3++;
}
//cout<<ni3<<endl;
string temp_S_1=inp[0];
string S_ni=inp[0];
for(int i=1; i<ni3;i++) { S_ni=nth_from_prev(temp_S_1, inp);
	temp_S_1=S_ni;
}

ll n_for3=ni3;
ll out_3=-1;
ll temp3=0;
string S_new=S_ni;
while(true){
	out_3=KMPSearch(inp_w, S_new);
	if(out_3==-1) {S_new=nth_from_prev(S_new,inp);
		n_for3++;}
	
	if(out_3!=-1 || S_new.length()>10e6) break;
}

if (out_3!=-1) cout<<n_for3<<" "<<out_3<<"\n";
else cout<<out_3<<"\n";
}

}

/*****************PArt4*******************************/

if(oper==3){

string inp_w4;
cin>>inp_w4;

ll len_w4=inp_w4.length();

if(inp_w4=="a") cout<<0<<" "<<1;

else{
ll ni4=1;
while(true){


	ll tempe[k];

nlen(count,ni4,k,len_f1,tempe);
//cout<<tempa[0]<<endl;
if(tempe[0]>=len_w4) break;
ni4++;
}
//cout<<ni3<<endl;
string temp_S_11=inp[0];
string S_ni4=inp[0];
for(int i=1; i<ni4;i++) { S_ni4=nth_from_prev(temp_S_11, inp);
	temp_S_11=S_ni4;
}

ll n_for4=ni4;
ll out_4=-1;
int temp4=0;
string S_new4=S_ni4;
while(true){
	out_4= sub_4(inp_w4, S_new4);
	if(out_4==-1) {S_new4=nth_from_prev(S_new4,inp);
		n_for4++;}
	
	if(out_4!=-1 || S_new4.length()>10e6) break;
}

if (out_4!=-1) cout<<n_for4<<" " <<out_4<<"\n";
else cout<<out_4<<"\n";

}

}
}

}