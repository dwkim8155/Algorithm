#include <stdio.h>
#include <stdlib.h>

int min(int a, int b){
    return (a<=b) ? a:b;
}

int main()
{
    int n,k;
    scanf("%d %d", &n, &k);
  
    
    int** bPtr = (int**)malloc(sizeof(int*)*(n+1));
    for (int i=0; i<=n; i++) {
        bPtr[i] = (int*)malloc(sizeof(int)*(i+1));
    }
    
    for (int i=0; i<=n; i++) {
        for (int j=0; j<=min(i,k); j++) {
            if (j==0 || i==j) {
                bPtr[i][j]=1;
                continue;
            }
            bPtr[i][j] = (bPtr[i-1][j-1] + bPtr[i-1][j])%10007;
        }
    }        
    
    printf("%d", bPtr[n][k]);
    return 0;
}
