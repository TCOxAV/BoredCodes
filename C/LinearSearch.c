#include <stdio.h>
int main() {
    int n,i,x, indexing;
    int arr[50];
    printf("Enter the number of terms: ");
    scanf("%d",&n);
    printf("Enter the values: \n");
    for (i=0;i<n;i++) {
        scanf("%d",&arr[i]);}
    printf("Enter the value to be searched: ");
    scanf("%d",&x);
    for (i=0;i<n;i++) {
        if (arr[i] == x) {
            indexing = i;
            break;}}
    if (indexing = i) {
        printf("Value (%d) found at index (%d)",x,indexing);
    }
    else {
        printf("Not found");
    }
    return 0;
}
