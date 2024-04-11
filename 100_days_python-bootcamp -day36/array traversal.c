/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

void main()
{
   int arr[10],i,j,n;
   printf("enter the total elements\n");
    scanf("%d",&n);
     printf("enter array elements\n");
   for(i=1;i<=n;i++)
   {
       scanf("%d",&arr[i]);
   }
   printf("element limit reached!!!!\n");
   printf("printing the entered elements....\n");
   for(i=1;i<=n;i++)
   {
       printf("%d\t",arr[i]);
   }
}
