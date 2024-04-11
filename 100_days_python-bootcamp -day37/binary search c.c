#include <stdio.h>

void main() {
    int i,arr[10]={1,2,3,4,5,6,7,8,9,10},n,mid,first=0,last=9;
    printf("enter the search element");
    scanf("%d",&n);
    int flag=0;
    while(first<=last)
    {
        mid=(first+last)/2;
        if(n==arr[mid])
        {
            flag=1;
            break;
        }
        else if(arr[mid]<n)
        { 
            
            first=mid+1;
        }
        else
        {
            last=mid-1;
        }
    }
    if(flag==1)
    {
        printf("element found at pos %d",arr[mid]);
    }
    else
    {
        printf("not fpumd");
    }
   
}