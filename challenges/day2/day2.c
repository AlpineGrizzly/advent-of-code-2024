#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define ARR_SIZE 256
#define MAX_LINE_SIZE 8

void resetArray(int arr[]) { 
    for (int i = 0; i < MAX_LINE_SIZE; i++) { 
        arr[i] = 0;
    }
}

int isSafe(int nums[]) { 
    int increase = 0;
    int safe = 1;
    int delta;

    printf("*%d* ", nums[0]);
    // If all levels are (all increase or all decrease) && (any two adjacent levels differ by 1 <= x <= 3) == safe
    for (int i = 1; i < MAX_LINE_SIZE && nums[i]; i++) { 
        delta = nums[i] - nums[i-1];
        if (i == 1) { 
            // Set our pattern
            increase = delta; // will be negative for decrease and pos for increase
        }

        if (nums[i] == 0) { // end of array
            break;
        }        

        // Was the delta in the valid range?
        if (delta*increase > 0 && ((abs(delta) >= 1 && abs(delta) <= 3))) { 
            printf("[%d] ", nums[i]);
        } else { 
            printf("!%d! %d %d", nums[i], delta, increase);
            return 0;
        }
    }

    return safe;

}

int main() { 
    FILE *f; // Pointer to file
    char line[ARR_SIZE]; // Buffer to hold each line
    int numbers[MAX_LINE_SIZE] = {0}; // hold detokenize numbers
    char *token; // tokenizer for space delimeted numbers
    int idx = 0; // Index for tokenizer
    int num_safe = 0; // Number of reports that are safes

    // Open input file 
    f = fopen("input.txt", "r"); 
    if (f == NULL) { 
        perror("Unable to open input file");
        return 1;
    }

    // Read line by line and determine if line is safe or unsafe
    while (fgets(line, sizeof(line), f) != NULL) { 
        // Retrieve numbers from line and store in int array
        token = strtok(line, " ");
        idx = -1;
        while (token != NULL) {
            idx++;
            numbers[idx] = atoi(token);
            token = strtok(NULL, " ");
        }

        // Determine if safe
        if (isSafe(numbers)) {
            printf("Safe!\n");
            num_safe++;
        } else { 
            printf("Unsafe!\n");
        }

        resetArray(numbers); // reset array to 0 
    }

    printf("%d reports are safe!\n", num_safe);

    return 0;
}