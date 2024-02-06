#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int graph[101][101] = {0};

void drawLine(int sy, int sx, int deg, char** stack, int idx, int num) {
    
    if (deg==0) {
        graph[sy][sx+1]=num;
        stack[idx][0] = sy;
        stack[idx][1] = sx+1;
    }
    else if (deg==1) {
        graph[sy-1][sx]=num;
        stack[idx][0] = sy-1;
        stack[idx][1] = sx;
    }
    else if (deg==2) {
        graph[sy][sx-1]=num;
        stack[idx][0] = sy;
        stack[idx][1] = sx-1;
    }
    else {
        graph[sy+1][sx]=num;
        stack[idx][0] = sy+1;
        stack[idx][1] = sx;
    }
    stack[idx][2] = deg;
}

void drawG(char** stack, int drawNum, int num){
    int idx = drawNum-1;
    for (int i=drawNum; i>0; i--){
        int sy = stack[idx][0];
        int sx = stack[idx][1];
        int deg = stack[i-1][2];
        deg = (deg+1)%4;
        drawLine(sy, sx, deg, stack, idx+1, num);
        idx++;
    }
    
}


char** draw(int sy, int sx, int deg, int g, int num){
    
    char** stack = (char**)malloc(sizeof(char*));
    stack[0] = (char*)malloc(sizeof(char)*3);
    
    int step=0;
    int idx=0;
    
    drawLine(sy, sx, deg, stack, idx, num);
    
    
    while (step!=g) {
        
        step++;
        
        int p = (int)pow(2.0, (double)step);
        stack = (char**)realloc(stack, sizeof(char*)*p);
        
        for (int i=(p/2); i<p; i++){
            stack[i] = (char*)malloc(sizeof(char)*3);
        } 
        
        drawG(stack, p/2, num);
    }
    
    return stack;
    
    
}

int fourPointCheck(int x, int y) {
    
    int ans = 1;
    int dx[4] = {0,1,0,1};
    int dy[4] = {0,0,1,1};
    for (int i=0; i<4; i++){
        int nx = dx[i]+x;
        int ny = dy[i]+y;
        if (graph[nx][ny]==0){
            return 0;
        }
    }
    return ans;
}

int check(void) {
    int ans=0;
    
    for (int i=0; i<100; i++) {
        for (int j=0; j<100; j++){
            if (graph[i][j]==0) continue;
            if (fourPointCheck(i,j)) ans++;
        }
    }
    
    return ans;
}

int main()
{   
    int N;
    scanf("%d", &N);
    for (int i=0; i<N; i++){
        int x,y,d,g;
        scanf("%d %d %d %d", &x,&y,&d,&g);
        graph[y][x] = i+1;
        char** st = draw(y,x,d,g,i+1);
        
        int arrNum = (int)pow(2.0, (double)g);
        for (int j=0; j<arrNum; j++){
            free(st[j]);
        }
        free(st);
    }
    
    printf("%d", check());
    
    return 0;
}
