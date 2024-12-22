import numpy as np
import re

MUL="mul\([0-9]+,[0-9]+\)"
DISABLE="don't\(\)"
ENABLE="do\(\)"

def do_mul(equ):
    result = 0
    match = re.search("[0-9]+,[0-9]+", equ)
    
    if match:
        value1, value2 = match.group(0).split(",")
        result = int(value1)*int(value2)
    
    return result 

def main():
    total_sum = 0
    str_value = "" 
    print("GO")

    
    # Get number of lines in the input file and create two arrays of that sizes
    with open("input.txt", "r") as file:
        lines = file.readlines()

    # Pt 1
    values = re.findall(MUL, str(lines))
    for match in values:
        total_sum = total_sum + do_mul(match)
    
    print("Part 1 sum is ", total_sum)

    # Pt 2 
    total_sum = 0
    enabled=True # Boolean depending on value
    pattern = r"%s|%s|%s" % (MUL,DISABLE,ENABLE)
    print(pattern)
    values = re.findall(pattern, str(lines))
    for match in values:
        print(match)
        if MUL[0:3] in match:
            if enabled:
                total_sum = total_sum + do_mul(match)
            else:
                print("Skipping!")
        elif DISABLE.replace("\\", "") in match:
            print("DISABLED!")
            enabled=False
        elif ENABLE.replace("\\", "") in match:
            print("ENABLED!")
            enabled=True

    print("Part 2 sum is ", total_sum)


    

if __name__ == '__main__':
    main()
        