#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long int t;
    cin>>t;
    while(t)
    {
        t = t-1;
        long long int n;
        cin>>n;
        long long int a[200001];
        long long int var;
        for(int i=0;i<n;i++){cin>>a[i];}
        unsigned long long int ans1=0,ans2=0;
        var=a[0];
        a[0]=a[1];
        for(int i=n-1;i>0;i--)
        {
            ans1+=(abs(a[i]-a[i-1]));
        }
        a[0]=var;var=a[n-1];a[n-1]=a[n-2];
        for(int i=n-1;              i>0;i--){ans2+=(abs(a[i]-a[i-1]));}
        a[n-1]=var; unsigned long long int y=0; if(ans1<ans2){
            y=ans1;
        }
        else{
            y=ans2;
        }
        
        unsigned long long int total=0,index=0,diff1=0,diff2=0;
        for(int i=1;i<n-1;i++)
        {



            if        ((    a[i]>=a[i-1] && a[i+1]>=a[i]) || (a[i]<=a[i-1] && a[i+1]<=a[i]))
            {continue;}
            else{
                if((abs(a[i]-a[i-1])+abs(a[i]-a[i+1])-abs(a[i+1]-a[i-1]))>total)
                

                {
                            total=abs(a[i]-a[i-1])+abs(a[i]-a[i+1])-abs(a[i+1]-a[i-1]);
index=i;
                }
            }
        }
        // if(index!=0)
        // {
        //     a[index]=a[index+1];
        // }
        unsigned long long int ans=0;
        for(int i=n-1;i>0;i--)
        {
            ans+=(abs(a[i]-a[i-1]));
        }
        // if(y<ans)
        //     cout<<y<<endl;
        // else
        // {
        //     cout<<ans<<endl;
        // }
 
        
    }
    return 0;
}