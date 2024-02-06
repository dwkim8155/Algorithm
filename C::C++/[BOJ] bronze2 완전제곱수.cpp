#include <stdio.h>

int main() {
    int M, N;
    scanf("%d %d", &M, &N);
    
    int total = 0;
    int min = 0;
    
    int now = 1;
    
    while (now*now <= N) {
        
        if (M <= now*now) {
            total+= now*now;
            
            if (!min) {
                min = now*now;    
            }
            
        }
        
        ++now;
    }
    
    if (min==0) {
        printf("%d", -1);
    }
    else {
        printf("%d\n", total);
        printf("%d", min);
    }
    
    return 0;
}
