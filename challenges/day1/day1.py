import numpy as np

def main():
    total_distance = 0

    # Get number of lines in the input file and create two arrays of that sizes
    with open("input.txt", "r") as file:
        lines = file.readlines()
        line_count = len(lines)

    arr1 = np.zeros(line_count)
    arr2 = np.zeros(line_count)

    # Read in values to each array
    with open("input.txt", "r") as file:
        for i in range(0, len(arr1)):
            arr1[i], arr2[i] = file.readline().split()
            #print(arr1[i], arr2[i])

    # Organize arrays
    arr1 = np.sort(arr1)
    arr2 = np.sort(arr2)

    # Find total distance between both arrays
    for i in range(0, len(arr1)):
        total_distance += abs(arr1[i]-arr2[i])

    print("Total distance is ", int(total_distance))  

    # Part two: Similiarity score
    sim_score = 0

    # Find similarity score for each list
    for i in range(0, len(arr1)):
        count = 0
        
        # Find how many times a number in the left list appears in the right lists
        for j in range(0, len(arr1)):
            if arr1[i] == arr2[j]:
                count += 1

        # Add to similarity score
        sim_score += arr1[i]*count

    print("Similarity score is ", int(sim_score))

if __name__ == '__main__':
    main()