
def main():
    calories = []
    with open('input2.txt') as inputFile:
        currentTotal = 0
        for line in inputFile:
            if (line == '\n'):
                # print(currentTotal)
                calories.append(currentTotal)
                currentTotal = 0 # reset currentTotal and count new set of calories.
            else:
                currentTotal += int(line) 

    # mutate the list
    calories.sort() # sort from lowest to highest
    calories.reverse() # reverse the list.
    print(calories) # first number is part 1.
    print(calories[0] + calories[1] + calories[2]) # part 2 of puzzle: sum of top 3

if __name__=="__main__":
    main()