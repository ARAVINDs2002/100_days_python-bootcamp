#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int generateToken() {
    
    srand(time(NULL));

    // this fn generate a random number  according to each time
    int token = rand();

}

int main() {
    int token = generateToken();
printf("|---------------------------------------------------------------------------|\n");
printf("    YOUR  token  :%d\n", token);
printf("|---------------------------------------------------------------------------|\n");

    return 0;
}