// Online C compiler to run C program online
#include <stdio.h>
#include <stdlib.h>

int n, st;

void merge(int* arr, int s, int mid, int e) {
    int i = s;
    int j = mid+1;
    int k = s;
    int* sorted = (int*)malloc(sizeof(int)*n);
    
    while (i<=mid && j<=e){
        if (arr[i]<arr[j]) sorted[k++]=arr[i++];
        else sorted[k++]=arr[j++];
    }
    
    int ii = (i>mid) ? j:i;
    for (int i=k; i<=e;i++){
        sorted[i] = arr[ii++];
    }
    
    for (int i=s; i<=e; i++){
        arr[i] = sorted[i];
    }
    
    free(sorted);
    
}

void mergeSort(int* arr, int s, int e, int step) {
    
    if (s<e) {
        int mid = (s+e)/2;
        mergeSort(arr, s, mid, step*2);
        mergeSort(arr, mid+1, e, step*2);
        merge(arr,s,mid,e);
        if (step == st) {
            for (int i=s; i<=e; i++){
                printf("%d ",arr[i]);
            }
        }
    }
    return;
}

int main() {
    
    scanf("%d", &n);
    int* arr = (int*)malloc(sizeof(int)*n);
    for (int i=0; i<n; i++){
        scanf("%d", arr+i);
    }
    scanf("%d", &st);   
    
    mergeSort(arr, 0, n-1, 1);
    
    free(arr);
    return 0;
}