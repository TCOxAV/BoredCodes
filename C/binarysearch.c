#include <stdio.h>

int binarysearch(int arr[], int n, int key) {
    int low = 0, high = n-1;
    while (low<=high) {
        int mid = (low+high)/2;
        if (arr[mid]==key)
            return mid;
        else if (arr[mid] > key)
            high = mid - 1;
        else
            low = mid + 1;
    }
    return -1;
}

int main() {
    int arr[100],n,key,result;
    
    printf("Enter the number of Elements:");
    scanf("%d",&n);
    
    printf("Enter the Elements:");
    for (int i = 0;i < n;i++)
        scanf("%d",&arr[i]);
    
    printf("Enter the key:");
    scanf("%d",&key);
    
    result = binarysearch(arr, n, key);
    
    if (result==-1)
        printf("Value not in Array");
    else
        printf("Value at index %d, position %d",result,result+1);
    return 0;
}
