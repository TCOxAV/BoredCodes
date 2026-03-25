#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int guess, number, attempts = 0;
    int low = 1, high = 100;
    
    srand(time(0));
    number = rand() % 100 + 1;
    
    printf("🔢 GUESS THE NUMBER (1-100)\n");
    printf("==========================\n\n");
    
    do {
        printf("Guess [%d-%d]: ", low, high);
        scanf("%d", &guess);
        attempts++;
        
        if (guess < number) {
            printf("📈 Too low! ");
            if (guess > low) low = guess + 1;
        }
        else if (guess > number) {
            printf("📉 Too high! ");
            if (guess < high) high = guess - 1;
        }
        else {
            printf("\n🎉 CORRECT! You got it in %d attempts!\n", attempts);
        }
        
        if (guess != number) {
            printf("Try again\n\n");
        }
        
    } while (guess != number);
    
    return 0;
}
