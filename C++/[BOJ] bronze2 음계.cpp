#include <iostream>

using namespace std;

int main()
{
    int arr[8];
    bool as = true;
    bool ds = true;
    
    for (int i=0; i<8; ++i)
    {
        cin >> arr[i];
        
        if (arr[i] != i+1)
        {
            as = false;
        }
        
        if (arr[i] != 8-i)
        {
            ds = false;
        }
    }
    
    if (as)
    {
        cout << "ascending";
    }
    else if (ds)
    {
        cout << "descending";
    }
    else 
    {
        cout << "mixed";
    }

    return 0;
}