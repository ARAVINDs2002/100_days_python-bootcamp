#include <stdio.h>

void main() {

   int arr[10],size,pos,i;
   printf("enter the total size\n");
   scanf("%d",&size);
    printf("enter the elements...\n");
   for(i=0;i<size;i++)
   {
       scanf("%d",&arr[i]);
   }
    
    if(size>0)
    {
      size--;
    }
      printf("the new array is\n");
      for(i=0;i<size;i++)
   {
       printf("%d",arr[i]);
   }
}

