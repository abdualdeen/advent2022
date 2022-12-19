
def main():
    calories = []
    with open('input.txt') as inputFile:
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
    print(calories) 
    print(calories[0] + calories[1] + calories[2]) # sum of top 3

if __name__=="__main__":
    main()