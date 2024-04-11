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
    /*printf("give the position at which the element is to be deleted!!!!\n");
    scanf("%d",&pos);*/
    for(i=0;i<size-1;i++)
   {
       arr[i]=arr[i+1];
   }
      size--;
      printf("the new array is\n");
      for(i=0;i<size;i++)
   {
       printf("%d",arr[i]);
   }
}

