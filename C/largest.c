#include <stdio.h>
int main() {
int n,i,val = 0;
int arr[50];
printf("Enter the number of terms: ");
scanf("%d",&n);
printf("Enter the values for the array: \n");
for (i=0;i<n;i++) {
    scanf("%d",&arr[i]);}
for (i=0;i<n;i++) {
    if (arr[i] >= val) {
        val = arr[i];}
    }
printf("The largest value is %d",val);
    return 0;
}
