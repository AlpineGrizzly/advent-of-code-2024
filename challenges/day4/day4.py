import sys

def print_debug_arr(arr):
    for y in range(0, len(arr)):
        for x in range(0, len(arr[0])):
            print(arr[y][x], end="")
        print("")

def print_array(array, x, y, word2find):
        for i in range(0, len(word2find)):
            print(array[y+i][x:x+len(word2find)])

def get_xmas_count_pt2(array):
    '''
    Get number of time a pair of X-MAS appear
    '''
    count = 0
    word2find = "MAS"

    print("Array length %dx%d" % (len(array[0]), len(array)))

    x_max = len(array[0])-len(word2find)
    y_max = len(array)-len(word2find)
    
    # Iterate through array len(set2find) times at a time and compare arrays
    for y in range(0, y_max+1):
        for x in range(0, x_max+1):            
            print("-----------Pre-check---------------")
            print_array(array, x, y, word2find)
            print("----------------------------------") 

            # Check for either a row and a column of MAS or 2 verticals of MAS
            # Combination of middle row and middle column
            row = array[y+1][x:x+len(word2find)]
            col = array[y][x+1] + array[y+1][x+1] + array[y+2][x+1]
#array#array[y][x:x+len(word2find)]

            print("rc value %s %s" % (row, col))
            if (row == word2find or row[::-1] == word2find) and (col == word2find or col[::-1] == word2find): 
                print("Found XMAS! ortho")
                count += 1# We have an xmas

            # Vert check
            lv = array[y][x] + array[y+1][x+1] + array[y+2][x+2]
            rv = array[y+2][x] + array[y+1][x+1] + array[y][x+2]
            
            print("lr value %s %s" % (lv, rv))
            if (lv == word2find or lv[::-1] == word2find) and (rv == word2find or rv[::-1] == word2find): 
                print("Found XMAS! slant")
                count += 1# We have an xmas
    return count

def get_xmas_count(array):
    '''
    Get number of times XMAS appears in a 2d string array
    '''
    word2find = "XMAS"
    count = 0
    
    print("Array length %dx%d" % (len(array[0]), len(array)))

    x_max = len(array[0])-len(word2find)
    y_max = len(array)-len(word2find)
    

    print("iterating %dx%d" % (x_max, y_max))
    # Iterate through array by increments of len(word2find) to ensure repeats arent counted
    debug_arr = [["."] * len(array[0]) for _ in range(len(array))]
    for y in range(0, y_max+1):
        for x in range(0, x_max+1):
            print("-----------Pre-check---------------")
            print_array(array, x, y, word2find)
            print("----------------------------------") 

            # Check rows
            for r in range(0, len(word2find)):
                row = array[y+r][x:x+len(word2find)]
                print("--row-> ", row) 
                if row == word2find or row[::-1] == word2find:
                    find_count = 0 
                    for n in range(0, len(row)):
                        if debug_arr[y+r][x+n] == ".":
                            debug_arr[y+r][x+n] = row[n]
                        else:
                            find_count += 1
                    if find_count != len(word2find):
                        print("Found row %dx%d %s" % (y+r, x, row))
                        count += 1
                    else:
                        print("Already found row %dx%d %s" % (y+r, x, row))

            # Check columns
            for c in range(0, len(word2find)): 
                col = array[y][x+c] + array[y+1][x+c] + array[y+2][x+c] + array[y+3][x+c]
                print("--col-> ", col) 
                if col == word2find or col[::-1] == word2find:
                    find_count = 0
                    for n in range(0, len(col)):
                        if debug_arr[y+n][x+c] == ".":
                            debug_arr[y+n][x+c] = col[n]
                        else:
                            find_count += 1
                    if find_count != len(word2find):
                        print("Found col %dx%d %s" % (y, x+c, col))
                        count += 1
                    else:
                        print("Already found col %dx%d %s" % (y, x+c, col))
 
            # Check left and right verticals
            left_vert, right_vert = "", ""
            for n in range(0, len(word2find)):
                left_vert += array[y+n][x+n]
                right_vert += array[y+len(word2find)-1-n][x+n]
           
            print("--lv-> ", left_vert) 
            if left_vert == word2find or left_vert[::-1] == word2find:
                # Check if its already been counted
                #find_count = 0 # if we hit 4, its already been counted
                for t in range(0, len(left_vert)):
                    if debug_arr[y+t][x+t] == ".": 
                        debug_arr[y+t][x+t] = left_vert[t]
                #    else: 
                #        find_count += 1
                #if find_count == len(word2find):
                print("Found lv %dx%d %s" % (y+t, x+t, left_vert))
                count += 1
                #else:
                #    print("Already Found lv %dx%d %s" % (y+t, x+t, left_vert))
             
            print("--rv-> ", right_vert) 
            if right_vert == word2find or right_vert[::-1] == word2find:
                #find_count = 0 
                for s in range(0, len(right_vert)):
                    if debug_arr[y+len(word2find)-1-s][x+s] == ".":
                         debug_arr[y+len(word2find)-1-s][x+s] = right_vert[s]
                #    else:
                #        find_count += 1
                #if find_count == len(word2find):
                print("Found rv %dx%d %s" % (y+len(word2find)-1-s, x+s, left_vert))
                count += 1
                #else:
                #    print("Already found rv %dx%d %s" % (y+len(word2find)-1-s, x+s, left_vert))
    
    print("-----------DEBUG ARR---------------")
    print_debug_arr(array)
    print("")
    print_debug_arr(debug_arr)
    print("----------------------------------") 
    print("")
    return count

def main():
    input_file = sys.argv[1]
    part = int(sys.argv[2])
    input_arr = [] 
    
    print("File selected is ", input_file)
    # Get number of lines in the input file and create two arrays of that sizes
    
    with open(input_file, "r") as file:
        for line in file:
            input_arr.append(line.rstrip('\n'))
            #print(line.rstrip('\n'))
    
    search_box = [["."] * len(input_arr[0]) for _ in range(len(input_arr))]
    search_box = input_arr

    print("\n")
    if part == 1:
        print("doing part 1 ") 
        for y in range(0, len(search_box)):
            for x in range(0, len(search_box[0])):
                print(search_box[y][x], end="")
            print("")
        print("Xmas count is ", get_xmas_count(search_box))
    elif part == 2:
        print("doing part 2 ") 
        # Do pt2
        print("Xmas count pt2 is ", get_xmas_count_pt2(search_box))        

if __name__ == '__main__':
    main()