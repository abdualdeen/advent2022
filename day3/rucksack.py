'''
a through z is 1 through 26
A through Z is 27 through 52
----------------------------
a group is 3 lines

'''
GROUP_LENGTH = 3

# given a list of strings it can find the common character
def findCommonItem(group):
    return [item for item in group[0].strip() if item in group[1].strip() and item in group[2].strip()]

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
    with open('input.txt') as inputFile:
        lines = inputFile.readlines()
        length = len(lines)
        iterations = length/GROUP_LENGTH # number of iterations to get through the file. divide 
        i = 0
        # print(length)
        while (i < iterations):
            group = lines[:i+3]
            commonItem = findCommonItem(group)
            
            itemsSum += calculateItemSum(commonItem)

            items.append(commonItem)
            i += 1
            break
            
        
    # print(items)
    # print(itemsSum)

def main():
    # part1()
    part2()


if __name__=="__main__":
    main()