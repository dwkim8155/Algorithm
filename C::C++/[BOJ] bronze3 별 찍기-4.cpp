#include <string>
#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;
    
    int star,space;
    string str;
    
    for (int i=n; i>0; --i)
    {
        star = i;
        space = n-i;
        str.clear(); 
        for (int i=0; i<space; ++i)
        {
            str+=' ';
        }
        
         for (int i=0; i<star; ++i)
        {
            str+='*';
        }
        
        cout << str << endl;
        
    }
    
    
    
    return 0;
}
