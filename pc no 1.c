#include <stdio.h>
 main ()
{
     int a,b,c;

     printf(" Enter the first number:");
     scanf("%d",  &a);


     printf(" enter the second number:");
     scanf("%d",  &b);

     printf("\nEnter the value before swapping are:\n");
     printf("a=%d\n" , a);
     printf("b=%d\n" , b);

     c=a;
     a=b;
     b=c;

     printf("value of a is: %d\n" , a);
     printf("value of b is : %d\n", b);


    return 0 ;


}
