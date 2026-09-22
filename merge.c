#include<stdio.h>
int main()
{
int A[10],B[10],C[20];
int n,m,i;

printf("enter size of first array:");
scanf("%d",&n);

printf("enter elements of first arraY:\n");
for(i=0;i<n;i++)
{

scanf("%d",&A[i]);
C[i]=A[i];
}

printf("enter size of second array:");
scanf("%d",&m);
printf("enter elements of second array:\n");
for(i=0;i<m;i++)
{
scanf("%d",&B[i]);
C[n+i]=B[i];
}
printf("merged array:\n");
for(i=0;i<n+m;i++)
{
printf("%d",C[i]);
}
return 0;
}





