#include <iostream>
using namespace std;

int sorted[9];

void Merge(int arr[], int s, int mid, int e)
{
    int i=s;
    int j=mid+1;
    int k=s;
    
    while (i<=mid && j<=e)
    {
        if (arr[i] <= arr[j])
        {
            sorted[k++] = arr[i++];
        }
        else
        {
            sorted[k++] = arr[j++];
        }
    }
    
    int v = (i > mid) ? j:i;
    
    for (int t=k; k<=e; ++k)
    {
        sorted[k] = arr[v++];
        
    }

    
    for (int i=s; i<=e; ++i)
    {
        arr[i] = sorted[i];   
    }
}
 
void MergeSort(int arr[], int s, int e) 
{
    int mid = (s+e)/2;
    if (s < e)
    {
        MergeSort(arr, s, mid);
        MergeSort(arr, mid+1, e);
        Merge(arr, s, mid, e);
    }
}


int main()
{
    int arr[9]= {4,2,1,3,9,5,7,6,8};
    MergeSort(arr,0,8);
    
    for (int i=0; i<9; ++i)
    {
        cout << arr[i];
    }
    
    return 0;
}