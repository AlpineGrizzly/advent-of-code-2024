def get_xmas_count(array):
    '''
    Get number of times XMAS appears in a 2d string array
    '''
    word2find = "XMAS"
    count = 0

    # Iterate through array by increments of len(word2find) to ensure repeats arent counted
    for x in range(0, len(array[0])-len(word2find)+1):
        for y in range(0, len(array)-len(word2find)+1):
            #debug_arr = [len(word2find)][len(word2find)] 

            # Check all rows both forward and reversed
            for m in range(0, len(word2find)): 
                # Get row and column values 
                row = array[x+m][y:y+len(word2find)]
                col = array[x][y+m] + array[x+1][y+m] + array[x+2][y+m] + array[x+3][y+m]
                
                # Check all directions forward and reverse 
                if row == word2find or row[::-1] == word2find:
                    print("Found row ", row)
                    count += 1
                if col == word2find or col[::-1] == word2find:
                    print("Found col ", col)
                    count += 1

            
            # Check all both verticals 
            # Get vertical
            left_vert, right_vert = "", ""
            for n in range(0, len(word2find)):
                left_vert += array[x+n][y+n]
                right_vert += array[x+len(word2find)-1-n][y+n]
           
            if left_vert == word2find or left_vert[::-1] == word2find:
                print("Found lv rv", left_vert)
                count += 1
            if right_vert == word2find or right_vert[::-1] == word2find:
                print("Found rv", right_vert)
                count += 1

            print("-----------REAL ---------------")
            print(array[x][y:y+len(word2find)])
            print(array[x+1][y:y+len(word2find)])
            print(array[x+2][y:y+len(word2find)])
            print(array[x+3][y:y+len(word2find)])
            print("-------------------------------")
            print("")
    
    return count

def main():
    search_box = []
 
    # Get number of lines in the input file and create two arrays of that sizes
    with open("test_input.txt", "r") as file:
        for line in file:
            search_box.append(line.rstrip('\n'))

    print("Xmas count is ", get_xmas_count(search_box))        

if __name__ == '__main__':
    main()