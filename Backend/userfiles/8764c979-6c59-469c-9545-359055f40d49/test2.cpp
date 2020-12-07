#include <iostream>
#include<string>
#include<map>
#include<memory.h>
#include<cmath>
#include<vector>
#include <algorithm>
using namespace std;
#define pii pair<int,int>
#define FAST ios::sync_with_stdio(false),cin.tie(0),cout.tie(0)
typedef long long ll;
const int Max = 2e5 + 5;
int lst[Max];
int Mod = 1e9 + 7;

int main()
{
    int n;
    cin >> n;
    int a;
    vector < int >  v;
    vector<int> ans(n, 0);
    for (int i=0; i < n; i++)
    {
        cin >> a;
        v.push_back(a);
    }
    int d = 0;
    sort(v.begin(), v.end());
    for (int i = 1; i < n; i+=2)
    {
        ans[i] = v[(i - 1) / 2];
        d++;
    }
    for (int j = 0; j < n; j+=2)
    {
        ans[j] = v[d];
        d++;
    }
    if (n % 2 == 0) cout << n / 2 - 1<<endl;
    else cout << n / 2<<endl;
    for (int i=0; i < n; i++)
    {
        cout << ans[i]<<" ";
    }
    cin >> n;int l, r;
    for (int i = 1;i <= n;i++)
    {
 
        cin >> lst[i];
    }int f = 0;ll sum = 0;
    for (int i = 1;i <= n - 1;i++)
    {
        if (lst[i] == 2 && lst[i + 1] == 3)f = 1;
        if (lst[i] == 3 && lst[i + 1] == 2)f = 1;
 
    }
    for (int i = 2;i <= n;i++)
    {
        if (i >= 2)
        {
            if (lst[i] == 1)    
            {
                if (lst[i - 1] == 2)sum += 3;
                if (lst[i - 1] == 3)sum += 4;
            }
            else if (lst[i] == 2)sum += 3;
            else if (lst[i] == 3)sum += 4;
        }
    }
    for (int i = 3;i <= n;i++)
    {
        if (lst[i] == 2 && lst[i - 1] == 1 && lst[i - 2] == 3)sum--;
    }
    if (f)cout << "Infinite" << endl;
    else
    {
        cout << "Finite" << endl;
        cout << sum << endl;
    }
 
}