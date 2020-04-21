#include <iostream>

using namespace std;

// solves a^2+2b^2=c^2s

int main(){
    int cap;
    printf("enter highest number to search: \n");
    cin >> cap;
    for(int a = 0; a < cap; a++){
        for(int b = 0; b < cap; b++){
            for(int c = 0; c < cap; c++){
                if((a * a) + (2 * b * b) == (c * c) && a<b && (c % a or a ==1)) {
                    printf ("a: %d b: %d c: %d \n", a, b, c);       
                }
            }
        }
    }

    return 0;
}