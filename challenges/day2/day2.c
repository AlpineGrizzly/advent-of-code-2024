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

int isSafe(int nums[], int array_size, int recurse) { 
    int increase = 0;
    int safe = 1;
    int delta;
    int problems2dampen = 0;
    int problem_node = 0; // store index of last unsafe node

    printf("*%d* ", nums[0]);
    // If all levels are (all increase or all decrease) && (any two adjacent levels differ by 1 <= x <= 3) == safe
    for (int i = 1; i < array_size && nums[i]; i++) { 
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
            printf("!%d! ", nums[i]);
            problem_node = i;
            problems2dampen++;
            safe = 0;
        }
    }

    // Check if removing the problem node would help
    printf("#%d-%d# ", problems2dampen, recurse);

    if (problems2dampen == 1 && recurse == 1) {
        // Check if removing the problem node would help 
        printf("\nREFACTOR? %d -- > ", problem_node);
        int clone_arr[MAX_LINE_SIZE-1]= {0};
        int idx_delta = 0;
        for (int i = 0; i < array_size && idx_delta < array_size-1; i++) {
            if (nums[i] == 0) { // end of array
                break;
            } else if (i == problem_node) { 
                continue;
            }

            clone_arr[idx_delta] = nums[i];
            printf("%d ", clone_arr[idx_delta]);
            idx_delta++;
        }
        printf("\n");
        // Try again? 
        if (isSafe(clone_arr, array_size-1, 0)) { 
            return 1;
        }
        return 0;
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
        if (isSafe(numbers,MAX_LINE_SIZE, 1)) {
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