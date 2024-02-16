#include <iostream>
#include <string>
using namespace std;

int main()
{
    int M, D, total,ans;
    total = 0;
    ans = 0;
    
    string week;
    
    cin >> M >> D;
    
    for (int i=1; i<M; i++) {
        if (i==2) {
            total+=28;
            continue;
        }
        
        if (i==1 || i==3 || i==5 || i==7 || i==8 || i==10 || i==12) total+= 31;
        else total += 30;
    }
    
    total+=D;
    ans = total%7;
    
    if (ans==1) week = "MON";
    else if (ans==2) week = "TUE";
    else if (ans==3) week = "WED";
    else if (ans==4) week = "THU";
    else if (ans==5) week = "FRI";
    else if (ans==6) week = "SAT";
    else week = "SUN";
    
    cout << week;
    return 0;
}