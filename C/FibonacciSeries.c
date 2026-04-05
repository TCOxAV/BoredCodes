#include <stdio.h>
int main() {
    int n,i,t1=0,t2=1,t3;
    printf("Enter number of terms: ");
    scanf("%d",&n);
    for (i=1;i<n;i++) {
        printf("%d\n",t1);
        t3 = t2 + t1;
        t1 = t2;
        t2 = t3;
    }
    return 0;
}
