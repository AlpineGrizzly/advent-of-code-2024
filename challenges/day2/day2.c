#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define ARR_SIZE 256
#define MAX_LINE_SIZE 8

int g_problems2dampen = 0;

void resetArray(int arr[]) { 
    for (int i = 0; i < MAX_LINE_SIZE; i++) { 
        arr[i] = 0;
    }
}

int isSafe(int nums[], int array_size) { 
    int increase = 0;
    int safe = 1;
    int delta;

    // If all levels are (all increase or all decrease) && (any two adjacent levels differ by 1 <= x <= 3) == safe
    for (int i = 1; i < array_size && nums[i]; i++) { 
        if (nums[i] == 0)// end of array
            break;

        delta = nums[i] - nums[i-1];

        if (i == 1)
            increase = delta; // will be negative for decrease and pos for increase

        // Was the delta in the valid range?
        if ( !(delta*increase > 0 && ((abs(delta) >= 1 && abs(delta) <= 3))) ) { 
            g_problems2dampen++;
            safe = 0;
        }
    }

    return safe;
}

int remove_node_check(int arr[], int node) {
    int new_arr_idx = 0;
    int new_arr[MAX_LINE_SIZE-1] = {0};

    for (int i = 0; i < MAX_LINE_SIZE; i++) { 
        if (i == node)
            continue;

        if (arr[i] == 0)
            break;

        // otherwise continue copying
        new_arr[new_arr_idx] = arr[i];
        new_arr_idx++;
    }

    return isSafe(new_arr, MAX_LINE_SIZE-1);
}

int isitActuallysafe(int nums[], int array_size) { 
    int safe = 0;

    if (isSafe(nums, array_size))
        safe = 1;
    else if (g_problems2dampen) {
        // Remove every node to see if a possible solution exists
        for (int i = 0; i < MAX_LINE_SIZE && !safe; i++) { 
            safe = remove_node_check(nums, i);
        }
    } else
        safe = 0;

    g_problems2dampen = 0;
    return safe;
}

int main() { 
    FILE *f; // Pointer to file
    char line[ARR_SIZE]; // Buffer to hold each line
    int numbers[MAX_LINE_SIZE] = {0}; // hold detokenize numbers
    char *token; // tokenizer for space delimeted numbers
    int idx = 0; // Index for tokenizer
    int num_safe = 0; // Number of reports that are safes
    int num_safe_act = 0; // Number of reports safe with dampener

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
        if (isSafe(numbers,MAX_LINE_SIZE))
            num_safe++;
        
        if (isitActuallysafe(numbers,MAX_LINE_SIZE))
            num_safe_act++;

        resetArray(numbers); // reset array to 0 
    }

    printf("%d reports are safe!\n", num_safe);
    printf("%d reports are safe with problem dampener!\n", num_safe_act);


    return 0;
}