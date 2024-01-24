#include <stdio.h>

int Map[31][11] = {0,};
int N,M,H;
int minVal = 4;


int Min(int x, int y) {
    return (x<=y) ? x:y;
}

int Check(void) {
    for (int j=1; j<=N; j++) {
        int ny = j;
        for (int i=1; i<=H; i++){
            if (Map[i][ny]==1) 
                ny++;
            else if (Map[i][ny-1]==1)
                ny--;
        }
        if (ny!=j)
            return 0;
    }
    return 1;
}

void DFS(int x, int y, int step) {
    
    if (step>3){
        return;
    }
    
    if (Check()==1){
        minVal = Min(minVal, step);
        return;
    }
        
    for (int i=x; i<=H; i++){
        for (int j=1; j<N; j++){
        
            if (i==x && j<y) continue; 
            
            if (Map[i][j]==1) continue;
            else if (Map[i][j+1]==1) continue;
            else if (Map[i][j-1]==1) continue;
            Map[i][j]=1;
            DFS(i,j,step+1);
            Map[i][j]=0;
        }
    }
    
    
}


int main()
{
    scanf("%d %d %d", &N, &M, &H);
    for (int i=0; i<M; i++) {
        int x,y;
        scanf("%d %d", &x,&y);
        Map[x][y] = 1;
    }
    DFS(1,1,0);
    printf("%d", (minVal==4) ? -1:minVal);
    
    return 0;
}
