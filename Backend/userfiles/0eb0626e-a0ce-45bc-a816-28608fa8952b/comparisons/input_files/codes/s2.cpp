#include <bits/stdc++.h>

using namespace std; 

#define M0 1000000007
#define M1 998244353
#define S 1000000

typedef unsigned long long ull;
typedef long long ll;

ull kbit(ull n, ull k) 
{ 
    return ((n >> k) & 1);
} 

ll gcd(ll a, ll b){
    if(b == 0) return a;
    else return gcd(b, a % b);
}

bool sieve[S];
void SieveOfEratosthenes(int n) 
{ 
    memset(sieve, true, sizeof(sieve)); 
    
    for(int p=2; p*p<=n; p++) 
    { 
        if(sieve[p]) 
        { 
            for(int i=p*p; i<=n; i += p) 
                sieve[i] = false;
        }
    }
}

ll gcdEx(ll a, ll b, ll *x, ll *y) {
    if (a == 0) {
        *x = 0, *y = 1;
        return b;
    }
    ll x1, y1;
    ll gcd = gcdEx(b%a, a, &x1, &y1);
    *x = y1 - (b/a) * x1;
    *y = x1;
    return gcd;
}

ll mmt(ll a, ll m)
{
    ll x, y;
    ll g = gcdEx(a, m, &x, &y);
    if (g != 1) return 0;
    ll res = (x%m + m) % m;
    return res;
}

ull powerm(ull x, ull p, ull m){
    ull base;
    if(p == 0) return 1;
    base = powerm(x, p>>1, m);
    if(p % 2 == 0) return (base % m)*(base % m) % m;
    else return (x % m)*((base % m)*(base % m) % m) % m;
}

ull power(ull x, ull p){
    ull base;
    if(p == 0) return 1;
    base = power(x, p>>1);
    if(p % 2 == 0) return base * base;
    else return x * base * base;
}

int main() {
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        string s;
        cin>>s;
        for(int i = 0, j = n-1; i < j && j >= 0; i++) {
            if(s[i] == 't') {
                while(j >= 0 && s[j] == 't') j--;
                s[i] = s[j], s[j] = 't';
            }
        } cout<<s<<'\n';
    }
	return 0;
}