//OM NAMO NARAYANA
#include<bits/stdc++.h>
#include<random>
// #include<fstream>
using namespace std;
int main()
{
    int T;cin>>T;
    // file<<T;
    // file<<'\n';
    // cin>>T;
    for(int t = 0; t < T; t++)
    {
        long long int N;
        cin>>N;
        long long int x;cin>>x;
        long long odd = 0, even = 0;
        char ch;
        for(long long int n = 0; n < N; n++)
        {
            cin>>ch;
            if(ch == 'F')odd++;
            cin>>ch;
            if(ch == 'F')even++;
        }
        if(abs(odd - even)%3 == 0)
            cout<<"YES\n";
        else 
            cout<<"NO\n";
    }
    return 0;
}