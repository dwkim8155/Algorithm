#include <stdio.h>

int fibonacci(int n, int* _pOne, int* _pZero) {
    if (n==1) {
        *_pOne+=1;
        return 1;
    }
    else if (n==0) {
        *_pZero+=1;
        return 0;
    };
    
    return fibonacci(n-1, _pOne, _pZero) + fibonacci(n-2, _pOne, _pZero);
    
}

int main()
{
    int t;
    scanf("%d", &t);
    for (int i=0; i<t; i++) {
        int n;
        int one = 0;
        int zero = 0;
        
        int* _pO = &one;
        int* _pZ = &zero;
        
        scanf("%d", &n);
        fibonacci(n,_pO,_pZ);
        
        printf("%d %d\n", zero, one);
    }
    printf("%d", 'a'<'b');

    return 0;
}