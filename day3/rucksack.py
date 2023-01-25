'''
a through z is 1 through 26
A through Z is 27 through 52
----------------------------
a group is 3 lines

'''
from queue import Empty


GROUP_LENGTH = 3

# given a list of strings it can find the common character
def findCommonItem(group):
    return set.intersection(*map(set, group))

# given 2 strings, it can find the common character.
def findCommonElement(list1, list2):
    return [element for element in list1 if element in list2][0]

def calculateItemSum(item):
    itemValue = 0
    itemAsciiValue = ord(item)
    if (itemAsciiValue > 96): # lower case
        itemValue = (itemAsciiValue - 96)
    else: # upper case
        itemValue = (itemAsciiValue - 38)
    # note: these magic numbers represent the ascii value needed to subtract to "normalize" their value to 1 through 26 for lowercase and 27 to 52 for uppercase
    return itemValue

def part1():
    items = []
    itemsSum = 0 # sum in ascii
    with open('input.txt') as inputFile:
        for line in inputFile:
            length = len(line)
            compartment1 = line[:int(length/2)]
            compartment2 = line[int(length/2):]

            item = findCommonElement(compartment1, compartment2)
            itemsSum += calculateItemSum(item)
            
            items.append(item)
        
    print(items)
    print(itemsSum)

def part2():
    items = []
    itemsSum = 0 # sum in ascii
    with open('/home/abdu/git/advent2022/day3/input.txt') as inputFile:
        lines = inputFile.read().splitlines()
        length = len(lines)
        i = 0
        while (i < length):
            group = lines[i:i+GROUP_LENGTH]
            commonItem = list(findCommonItem(group)) # make the set into the list so it works with the rest of the code.

            if (commonItem):
                itemsSum += calculateItemSum(commonItem[0])
                items.append(commonItem[0])

            i += GROUP_LENGTH # increment by three as we take 3 lines at a time.
            
        
    print(items)
    print(itemsSum)

def main():
    # part1()
    part2()


if __name__=="__main__":
    main()