#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a,k;
    scanf("%d %d", &a, &k);
    
    int* _p = (int*)calloc(a,sizeof(a));
    
    int idx=0;
    
    for (int i=1; i<=a; i++) {
        if (a%i==0){
            *(_p+idx) = i;
            idx++;
        }    
    }
    
    printf("%d", _p[k-1]);
    free(_p);
    return 0;
}
