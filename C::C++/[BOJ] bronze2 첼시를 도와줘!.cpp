#include <stdio.h>
#include <string.h>

using namespace std;

int main() {
    int n;
    int p;
    int price;
    char name[20];
    int max;
    char maxName[20];
    
    scanf("%d",&n);
    
    for (int i=0; i<n; ++i) {
        scanf("%d", &p);
        max = 0;
        for (int j=0; j<p; ++j){
            scanf("%d %s",&price, name);

            if (price > max) {
                max = price;
                strcpy(maxName, name);
            }
        }
        printf("%s\n", maxName);
    }
    
    return 0;
}