

def main():
    with open('/home/vanishing/git/advent2022/day4/input.txt') as inputFile:
        numberContained = 0 # count the number of assignments where it is contained by another in the pair
        for line in inputFile:
            assignment1, assignment2 = line.split(',')
            min1, max1 = assignment1.split('-')
            min2, max2 = assignment2.split('-')

            # first, check if the 1st assignment is contained in the second. 
            if min1 >= min2 and max1 <= max2:
                numberContained += 1
                continue # no need to 
            
            # then check if the 2nd assignment is contained in the 1st
            if min2 >= min1 and max2 <= max1: 
                numberContained += 1
            
        print(numberContained)

   
if __name__ == "__main__":
    main()
