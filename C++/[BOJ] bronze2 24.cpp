#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

int TotalSecond(int, int, int);
int TimeFormat(int);

int main()
{
    int sh, sm, ss;
    int ph, pm, ps; 
    
    scanf("%d:%d:%d", &ph, &pm, &ps);
    scanf("%d:%d:%d", &sh, &sm, &ss);
    
    int st = TotalSecond(sh, sm, ss);
    int pt = TotalSecond(ph, pm, ps);
    
    int tt;
    
    if (pt <= st) 
    {
        tt = st -pt;
    }
    else
    {
        tt = TotalSecond(24,0,0) - (pt - st);
    }
    
    TimeFormat(tt);
    
    return 0;
}

int TotalSecond(int h, int m, int s)
{
    return h*3600 + m*60 + s;
}

int TimeFormat(int ts)
{
    int h, m ,s;
    string hour, min, sec;
    
    h = ts/3600;
    hour = (h < 10) ? '0'+to_string(h):to_string(h); ts %= 3600;
    m = ts/60; 
    min = (m < 10) ? '0'+to_string(m):to_string(m); ts %= 60;
    s = ts;
    sec = (s < 10) ? '0'+to_string(s):to_string(s);
    cout << hour << ':' << min << ':' << sec;
    return 0; 
}